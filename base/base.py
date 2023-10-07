import os.path
import time
import csv
import datetime
from urllib import request
from log.log import Logger
from selenium.webdriver.common.action_chains import ActionChains
import ddddocr
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.options import Options
from pywinauto.keyboard import send_keys
from selenium.webdriver.common.by import By
import random
import traceback
import pymysql
import re
from selenium.webdriver.edge.service import Service
from xiaoe_data.test_sanming_data import Test_sanming_data
from xiaoe_data.formal_sanming_data import Formal_sanming_data
from xiaoe_data.test_xiaoe_data import Test_xiaoe_data
from xiaoe_data.formal_xiaoe_data import Formal_xiaoe_data
from xiaoe_data.test_han_data import Test_han_data
from xiaoe_data.formal_han_data import Formal_han_data


class Base(Formal_sanming_data):
    logger = Logger()
    # 直接创建Service实例
    ser = Service()
    ser.path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe'
    op = Options()
    # 使用无头模式
    op.add_argument('--headless')
    # 禁用GPU，防止无头模式出现莫名的BUG
    op.add_argument('--disable-gpu')
    op.page_load_strategy = 'eager'
    drive = webdriver.Edge(options=op, service=ser)
    drive.maximize_window()
    time1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert = "//div[@role='alert']"  # 弹窗信息
    alert_locator = (By.XPATH, alert)
    csv_place = r"C:\Users\86176\Desktop\pythonScriptGenerate\data.csv"  # 数据地址
    script_place = r"C:\Users\86176\Desktop\pythonScriptGenerate\pythonScript.txt"  # 存放xpath地址

    def open_userUrl_cookie(self):
        # """
        # 打开登录地址传入cookie，再打开首页地址
        # :param login_url: 登录地址
        # :param cust: cookie值
        # :param JSESSIONID: cookie值
        # :param sys: cookie值
        # :param url: 首页地址
        # :return:
        # """
        login_url = "http://uservue2.jinfu.baohan.com/#/login"
        url = "http://uservue2.jinfu.baohan.com/#/"
        JSESSIONID = {'name': 'JSESSIONID', 'value': 'DFD74E585E4BACEB9581151A2FAE20F6'}
        cust = {'name': 'baohan-jinfu-cust',
                'value': 'eyJhbGciOiJIUzI1NiIsImNhbGciOiJERUYifQ.eNpsjjEOwjAMRe_iGVCSNin0EEyMWRLiQlBJq7aRQIiZmRMgcQIOwHEY4Ba4lUAMbNZ79vc_QBst5MCl4CJJpcqmMAITHbHn7fo6nR_3C5HYYjPxoaiIHzRgMLZEDXnXRBxp8I5mkdFUVisf5mbbS_0bq4Fs-Ihv9oAbNOX8v-ofL_Z1r9iRivi2pQrWVGsTxhtqFAniroacq0ylkgnGact0A5BcpgPYdJ7OZrZAKxx1cpjKpZoyJ5kSSeZmEgtM4PgGAAD__w.nkJO-_sVGvkihzhjUieDjPFhMBtIMWEWLp65UH2BYsM'}
        #       captcha = {'name':'baohan-jinfu-captcha','value':'F2WIMMZD7N1TP3L8W0SDLTLYCYIH9T2R'}
        #       sys = {'name':'baohan-jinfu-sys','value':'eyJhbGciOiJIUzI1NiIsImNhbGciOiJERUYifQ.eNqsmktT40YQx7-LiiMhGBYDvrE2S1FLgtdA5RByGEtjM2Q8o8xjjXdrj8k1j1MuqVSuOaRSleN-ni0q3yItWTaWLat7TC5gST0PzXT_f9Mzeh9Z349aUeNgr9FsHB0fHTSj7Yj5BO59-vvHf7__5fHP3-COt9zsCDXQcP_9bcQV60t-G7Wc8Xz7NhIJ_H7RhF9SD4X6ko2yh7eL1d5G8FTNHszrzm-nzNqvtEnyR1t7bKuxu_V68HrSPGGfv7o-7_XGZxN3-bDT2Bnd3Lyz-2-OZPvNfpebzs755OXRxb0-27sSe4c-r81oyS1U9TV0NNVjbkoXbZ1Mu6BTblqx9sZdsLH1wt1GH7arrYR6q0XMWwl3TMj1dlIzdWmS7JewNfWlRic-dl8wxYacZns9STFL-KO6krmBNqOXQspA807-cgGF2t46PeLmBnyj5dOEOU4reE4czsUy02ENKdGdDhyUkZzasx6PuUjdSQx-oVzLsrfEglc8Nty95hO0uSyIzIg5oVVbgt-LwQQZ84USF2CIWGeRCq_udKwlOl6WSd7jqTau9Z3nZtLj1ktXb59PN1rxxIIStFLw71qjLFYplXlKo4vB3IqltjVt34HndqF3HeZY4bzZT1qB-rmahvWIK2yqYjDhZnPzgVBMxYLJEyl1nDsIVoVkYoSP42JgY8Z5p1IjLG_lQUOxfOOZFHPvr3eSpVIDUbwo0th8bM6VdcJ5SplYK2dY7AAsecQp0CjEjVLOLFOot3EFVOTcCDVsa-iQAWHCZ6svkjPPDNTP0Y4MZ4btO6YUx0M_LTTimo9SEDE8CmcQrJ-uJwRiI1diIKG3cwqC0kJ_L81NAHJyHg654iaoSMHEOHOF4mIDNoZQ65w0yqtkpNs_cZHeqyUuhhR9IiM-_FVsxN2yTEfMvsRHhE9PdEz0FVy0czHqsMnpQ3aXwEkaAKkePQMh1b4ExHqtKfEQljDxXHnIsHM6pdoGQA6FFYWKaCU5FyHtqcsCSlhEbBeoSAdoGYuwkAynItZYJRaRNUMFFZGUpYBivdU6JmKvUKJifRMrUKwPxxUk1pvPgejt3cmQCUWhIhF0BRapgb6Ix1q_WWEikzL7f-WY8zYYjEW7nZAFpeXOwZyH4VAPBhK8pbgMAeNAgwyMb9IwONJx-sQ3zFuq2BYENknO-uQmUMt8ABoSsSWAbeaZp7UyOAMcikGPw7IEMyyMSjhLi6kikyyYOSYfUGxVsFzs2VBDiYaM6GJYUrMwOvnKOAMh_rZNcpp1bKvvYSXZ8B2DVbahCl3QDed6Nd-AXzBzbEIkHNZMReIXlvURUj6q-j5hDnGS5eQvhFigtmZytmkq12cuvuvxgVfJBplceJYF961WDJoP3xak0n-ZFNRyJWiECXo9Yub7ddTNOsRdSmqeOVmAkofIODmvosgzrKyKkLTPqwkTeU7PWjLTE-_uSEIftC9X0vkLZOG_ZkeP5IGVOo9lbhUyjylUofIo7apFHgTunsfoiqCk9IXKBkg9uNi8eBvGbqjNJED7aQO-Umy5GzMJsThI6l114fgMfmFnEWWGTLfwu96xcR1aV2iSZSMSWY2tQcmUzNgU10GhS9odGukEAqtbnGSS9BR1pSWZ_F-FT2dTCOOK6BZRsgyHqrrjhCRZ-SHWaVlfNpOwDg_dRYFgfDW7j6XTlYIEvNAqJJ4LiUIne51IQYvdqU5lGweWKlPZ9GJeXytVNmQLZukG0tOFFaiUF3ARurEB_patDdtMxl4i-K0L7Ut49sw4IgdlifD5lxmXpiPs9BMNSilSbPGN0r7nQF1KZLarwug50TDdCqEGAunEfCUQaANS5Vob-YNXfZG5M2XmQk9TyacQFbNEEZF1MzVl_dWdHhNnCqY2FwVMDNY4cdirkdxi3atRx7T0etMFQvCC-znAOLfW51octrZt5wepYX62qX_0IONmll-LEScfscOy5CRNZdiMb5wdZGlSUIYwneh80zY3QlYGxFqH3M02OfIouTHSBr8TrS26TtKXCGjWQVgtELMM0gEMfa0RmnGEb1gFHbIEnKoEgWuTTwwCz16C9tXIG2m0nTPKUQt-oIJ9Soemieh2HBh8U3wdm48YPIYnOywZZSeXxZP5l7uP_3x8_Pj7419_PP70w6eff80Kf4i2I2Ft1Ir6TEOUfnYP4-XhJn9Io1ajebh73Dg8aOyDFXPZjeZxc6-R37h3AoodN44PGown_cMBexHz-PioyZv7_d14sPeCxYe70Yf_AAAA__8.me0fs_yG4if-_Qim23FqBdESf9YTxbVHRC-e0-8Q79I'}

        self.drive.get(login_url)  # 打开登陆地址
        self.drive.add_cookie(cust)  # 传入登录需要的cookie
        self.drive.add_cookie(JSESSIONID)
        #        self.drive.add_cookie(captcha)
        time.sleep(1)
        # self.drive.add_cookie(sys)
        # n=drive.window_handles
        # drive.switch_to.window(n[-1])
        self.drive.get(url)
        time.sleep(2)

    def open_backgroundUrl(self):
        # """
        # 打开登录地址传入cookie，再打开首页地址
        # :param login_url: 登录地址
        # :param cust: cookie值
        # :param JSESSIONID: cookie值
        # :param sys: cookie值
        # :param url: 首页地址
        # :return:
        # """
        login_url = "http://op.jinfu.baohan.com/#/login"
        url = "http://op.jinfu.baohan.com/#/"
        cust = {'name': 'baohan-jinfu-cust',
                'value': 'eyJhbGciOiJIUzI1NiIsImNhbGciOiJERUYifQ.eNpsjjGOwjAQRe8yNaxi4jh2DkFF6WZm7YBRcKIklkCIeus9ARIn4AAch4K9xU6QQFtsN3pv5s8_wpAIKhDFQiihjS4UzACTY_a4Xn6-vu-3M5M0-P4jxLplfrTgI1LjLVRjn_zMQnA8L0qemnYd4hJ3k7R_Yy2wjS_xzn7i3mOz_F9Nj1eHblLZiYuEYeAKhO0G43zLjRJDv--gEqrMtJG5VLyF4wSUKYx-gu0Y-MxjJjJyztWSJEpFuXOfRpVIOq8FEZx-AQAA__8.OjVewq0w1iH8yxUWgdGhbBHUctvm5FnsDtREpgpICNM'}
        captcha = {'name': 'baohan-jinfu-captcha', 'value': 'F2WIMMZD7N1TP3L8W0SDLTLYCYIH9T2R'}
        sys = {'name': 'baohan-jinfu-sys',
               'value': 'eyJhbGciOiJIUzI1NiIsImNhbGciOiJERUYifQ.eNqsms1y2zYQx9-Fk6PrRrIjS7w5UuLxxK0V2Z4e6h4gEpLhQgALgFGUTI7ttR-nXjqdXnvodKbHPE_G07fokqIUUaK4C6YXWwQXHwR3_78FwLeBTcdBGLSetFudVrfXfdIJDgKWxlD24e8f__3-l4c_f4OS1HJzKNREQ_nb24ArNpb8NgidSfnBbSBi-H3cgV9ST4X6ks2ym7ebzd4GcFetbqzbzosTZu1X2sT5rUdt9qj1-NGLyYtF55R9_vz6fDSany3c5evD1uHs5uaNPXrZlf2XR0NuBofni6fdi3t91r4S7ZM0b81oyS009TUMNNFzbkoXfR0vh6ATbsJIp8ZdsLlNhbsN3h1UW8EfNZTMTbSZPRVSDrhjQoZSWGKlfmqdnnFzA9MYpknMHKdVPFevtIh4mLApscaliaGEbj80Ok4jF8ZccuqoRjziInGnEUyfcqFlr4gVr3hkuHvBF2h3ma-ZGXNCq74E9xCTBTLfGzUuwBCxzhwaHt3pSEtktiyTfMQTbVz4XcrNYsRtKl29ff6ikWYXFoIFN8rcOYRpA5-5NDeI74B99mRk-03_DyOpbY3tHXjwEEY7YI4VTpz9pFWof29fMAV2M66w1xaBCTfNzSdCMRUJJk-l1FHuLFgTkokZ8paizfCuN80HlBhheZgHD8XyZcqkWEcBtf281kQUD4l0tp6Xc2WdcCmlTqSVMyxyoMN55CnQKcSFEs4sU6incQUQ4dwINe1rGJABgcLf1FjEZykz0D5HBzJdGfbvmFIck4CkUIprPktAyjA9FiTVlpqppVrXP1eyVOilF9NsrxcJ98BTxjRP8wKBUfbWi4sGKKRjagVCPZlI8I3i0geJEw0hP79J_LBIH-EWFGOPOfmIRcyvdqFIVfptPFLrlUC5qvQsFo4EzFhfwUU_V6UBWzx7nZUS0EnsqKAjytAUd7YSCetjoQTCpHiHZMA5nVBtPcBm8vnG5pfEQyZloYoWwyIsFOreT4mLiO0GGL0Itw4E0PNv-yS32cfI-n4rEYnkDhWERPS7AGS91T4-LpOyEaTWzPJrMeNEWNb3tsNKcJB13T50ONVm4cFOWmwLT8H_SFMsBynhlCqDm2Cl1tlB7JQrbryqFJgdMxfdjfgkVXEDyvqgaMVZnzrLafepsaYrLM61YnJIpuxHVOKTWYVLbJTbmMTsS3jEjPeD8cpBlyArkSXAEe2mwOJMx_DIw2ILBMMj1moJkIiYlwgJchSt9YKMSfIKdhtpTSt-IjV1FgSWoytJTifmcpft0gyEXW63EdhJpuwuPC8Q5uxZWJLUvBKeWPZQQU-kygqf6CxU8xNE_p5HLpsILJMq8XPK3Upwcy28MXWpUy1PrQdIcS0rlqGpvTudMqEo9MRmuETPZcIxTB2bswUNnjGXHsSEgHISCc89zCw6xdampYjLugOnaAaxQYMtzdrZ2GURHUQEPBAwUoCBSoUiVyNyIfM5Mg5QOm1rtHeFKlFvDKGKxjAwxD6Oaji46nAek5iQ71o_K-t3M0QM6lxhHyGwB6tmg5TPV-VZcpRaT1DAIlYrn2VKgQ7Uh_fBA3ocLvlxbm3KM7Ej4gPtcocYNOhWAINAi_oEZWPTEn5hRyFlWvisEHL1hynN_mPvfw8Alt1hIK9T9Eu4R9FRqj5SFh8lCftU_UI1JVMeouSkaixU3GckyeGNstBPySWlzCLOUyXQyFupAjaRNaKwXONZqhZksYX57I4eYMPbPb_YKkDmThB3BTbSSCkv4AIL3W2B8FEHw51ZnHltqawC_P_kOhKmPhsxm8akMMPdsjrQaodcfRZIPlCuiDKKT--LIIgOGG3d6qIUP6QT-or48Qme7eqrtNtSAsMbgibf9uszGaUSSSSrv-vwSCsz2T5N3R3FozwdCN9e2nUc0svE8zFE3LbOjYGIp0kiF95R5fdsTYlS7FF47U8UmOvnh7XeCXzTc4irOz0nDnC5U-nnUf7DompYaWjgRnngNliE-I8Qc4qKScu3kXMjJIchttrQL2mt0yWZLsdo1kJQZWKCQtrhoku774rG_-jH68zH47DHC0FNPp_wPAzy2nQjb7jRNtsoxz34oQ72nSC6DEX38cDgm-Lr2HzG4DbcOWTxLNsYLu6sv9x9-Of9w_vfH_764-GnHz78_GtW-V1wEAhrgzAYMw1R-tk9zFcKhfx1EoStzsnjXve412mDFXNZQafX6XbzgnsnoFp73Buzo2jCT05ax1EnGrePnrCo3e5NjnvHjB0H7_4DAAD__w.LnTQas-C-G6g3ccW0rVl5_scbFGtjAEQoTFDGSCNNJY'}

        self.drive.get(login_url)  # 打开登陆地址
        self.drive.add_cookie(cust)  # 传入登录需要的cookie
        self.drive.add_cookie(captcha)
        time.sleep(1)
        # self.drive.add_cookie(sys)
        # n=drive.window_handles
        # drive.switch_to.window(n[-1])
        self.drive.get(url)
        time.sleep(2)

    def open_jinfu_users(self):
        """
        打开金服用户端登录页面
        :return:
        """
        login_url = "http://uservue2.jinfu.baohan.com/#/login"
        self.drive.get(login_url)  # 打开登陆地址
        self.drive.maximize_window()

    def deal_cookie_login(self):
        # """
        # 打开登录地址传入cookie，再打开首页地址
        # :param login_url: 登录地址
        # :param cust: cookie值
        # :param JSESSIONID: cookie值
        # :param sys: cookie值
        # :param url: 首页地址
        # :return:
        # """
        login_url = "http://user.han.com/#/login"
        url = "http://user.han.com/#/"
        cust = {'name': 'baohan-han-cust-supervise',
                'value': 'eyJhbGciOiJIUzI1NiIsImNhbGciOiJERUYifQ.eNp0jjsOwjAQRO-yNSACTrLOIago3axjA0bBjvKRQIgj0CM6LkDNgUBcgzUNEoJu9GZnZ_bQ9hoKeJ6vj-PlfjvBAKg3X6RvbTNyfhGY7xVYT7qyCoqu6e1AgTOscxZVWDo_o0301OeDAvb8b9xYqv4kYut8V0dreuAVrm25X1NYkR-uHYWdY2q3NRRJhuNEiFRKPqMughxR4BusO8e5bKKFnU4wsUhC5lIbRIk6S0tDi3GZweEFAAD__w.8lMUEtx-tBT_Jgr-tPVViAPvdCBYM33LZJB4-C-sRE0'}
        JSESSIONID = {'name': 'JSESSIONID', 'value': '7BFCB67F65C8D857A1DDBCEDD2BBBDF3'}
        expert = {'name': 'baohan-han-cust-expert',
                  'value': 'eyJhbGciOiJIUzI1NiIsImNhbGciOiJERUYifQ.eNpsjjsOwjAMhq-CPAPKq0naQzAxZnHbAEElrfqQQFU3jsAdGDkVEsfARUJiYLO-z_79j9ANOWQgJJM8MYlVsAQcSkKvx_V5vy04gaHz7TrEXU14dOAj5pV3kPXt4JcOQkmz4IbGqt6HuMHTbN1PqgOS8cu_0R_aeqw2f838dntpZqMmqhG6jgrkWB8wro4B60sg6s8NZFxbxhOt0pTWsJ-BsVazDzj2ge6URrGTSSmsLJRkhS2MNsL7PJWptSWD6Q0AAP__.vYrQOs83H7uo0OLFrZTI4nL8NtUg8rcOGMRkDkow7HY'}
        customer = {'name': 'baohan-han-cust-customer',
                    'value': 'eyJhbGciOiJIUzI1NiIsImNhbGciOiJERUYifQ.eNpsjz0OwjAMRu_iuaA2bdKUQ3RizOKQFIJKWvVHoqoYkTgAAxunQ1wDBwnEwGa9Z_n7PEM_alhBwpnMBc9SlkAEOBpij8vtcb48r3ciY2-7pfNVQ3xWYD3q2ipYDd1oIwXO0Jxwmupm63yJhyDV71kFZP1HfG-_cWexLv-rELye2qDYiYq4vqcKGpsd-sXeYTM5ovbYUr6QsRSM55LWcAggL7gQb7AfXHhTa6NthcIUOosLhlWqN6kxUqDJeYJwegEAAP__.K2jJuM3mJBgzBm7Wgcz-bNH0bjK1d7KmXCnzqNKzG3U'}

        self.drive.get(login_url)  # 打开登陆地址
        self.drive.add_cookie(cust)  # 传入登录需要的cookie
        self.drive.add_cookie(JSESSIONID)
        self.drive.add_cookie(expert)
        self.drive.add_cookie(customer)
        time.sleep(1)
        # self.drive.add_cookie(sys)
        # n=drive.window_handles
        # drive.switch_to.window(n[-1])
        self.drive.get(url)
        time.sleep(2)

    def open_deal_url(self):  # 交易平台
        """
        打开交易平台登录页面
        :return:
        """
        login_url = self.deal_login_url
        self.drive.get(login_url)
        self.drive.maximize_window()
        time.sleep(1)

    def open_extract_system_url(self):  # 专家抽取系统
        """
        打开专家抽取系统登录页面
        :return:
        """
        login_url = self.extract_login_url
        self.drive.get(login_url)
        self.drive.maximize_window()
        time.sleep(1)

    def open_back_url(self):  # 总后台
        """
        打开总后台登录页面
        :return:
        """
        login_url = self.back_url
        self.drive.get(login_url)
        self.drive.maximize_window()
        time.sleep(1)

    def open_manage_url(self):
        """
        打开监管台登录页面
        :return:
        """
        login_url = "http://manage.han.com/#/"
        self.drive.get(login_url)
        self.drive.maximize_window()
        time.sleep(1)

    def connect_mysql(self):
        """连接mysql数据库"""
        try:
            conn = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='root',
                db='ceshi',
                charset='utf8'
            )
            cursor = conn.cursor()  # 创建游标
            return conn, cursor
        except (Exception, BaseException):
            error = traceback.format_exc()
            self.logger.info(error)

    def close_conn(self, conn, cursor):
        conn.close()
        cursor.close()

    def insert_and_update_sql(self, sql, *args):  # 添加数据
        conn, cursor = self.connect_mysql()  # 连接数据库
        try:
            cursor.execute(sql, args)
            conn.commit()
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.info(error)
            conn.rollback()
        self.close_conn(conn=conn, cursor=cursor)

    def query_sql(self, sql, *args):  # 查询数据查询
        conn, cursor = self.connect_mysql()  # 连接数据库
        try:
            cursor.execute(sql, args)
            result = cursor.fetchall()
            return result
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.info(error)
        self.close_conn(conn=conn, cursor=cursor)

    def query_now_date(self):  # 获取专家抽取时间
        sql = 'select nowdate,hour from get_now_date'
        try:
            result = self.query_sql(sql)
            return result[0]
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(error)

    def insert_expertData(self, projectNumber, username, password, judgeName):  # 插入专家账号密码
        conn, cursor = self.connect_mysql()
        sql = 'insert into expert (projectNumber,username,password,judgeName) values(%s,%s,%s,%s)'
        try:
            cursor.execute(sql, (projectNumber, username, password, judgeName))
            conn.commit()
        except (Exception, BaseException) as e:
            error = traceback.format_exc()
            if str(e).find('Duplicate entry') > 0:
                self.logger.debugText(projectNumber, '评委已经添加！')
            else:
                self.logger.debugText(projectNumber, error)
            conn.rollback()
        conn.close()
        cursor.close()

    def update_evaluationBidWay(self, evaluationBidWay, judgeNumber, projectNumber):  # 更新评标办法类型和评委个数
        conn, cursor, = self.connect_mysql()
        sql = 'update project set evaluationBidWay = %s , judgeNumber = %s where projectNumber = %s'
        try:
            cursor.execute(sql, (evaluationBidWay, judgeNumber, projectNumber))
            conn.commit()
            print("评标类型和评委个数更新成功！")
        except (Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)
            conn.rollback()
        conn.close()
        cursor.close()  #

    def update_isAgree(self, isAgree, username, projectNumber):  # 更新专家协议是否确认
        sql = 'update expert set isAgree = %s where username = %s and projectNumber = %s'
        try:
            self.insert_and_update_sql(sql, isAgree, username, projectNumber)
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)

    def update_now_date(self, nowdate, hour=0):
        sql = 'update get_now_date set nowdate = %s,hour = %s  where id = 0'
        try:
            self.insert_and_update_sql(sql, nowdate, hour)
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(error)

    def update_enterprise_count(self, enterpriseCount, projectNumber):  # 更新企业数量
        sql = 'update project set enterpriseCount = %s where projectNumber = %s'
        try:
            self.insert_and_update_sql(sql, enterpriseCount, projectNumber)
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)

    def update_evaluationReportNumber(self, evaluationReportNumber, projectNumber):  # 更新评标报告
        result = self.query_projectData(projectNumber=projectNumber)
        sql = 'update project set evaluationReportNumber = %s where projectNumber = %s'
        try:
            if result[9] < evaluationReportNumber:
                self.insert_and_update_sql(sql, evaluationReportNumber, projectNumber)
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)

    def update_ratingPoint_count(self, ratingPointCount, ratingType, projectNumber):  # 更新评分点数量
        result = self.query_projectData(projectNumber=projectNumber)
        number = result[7]  # 报名人数
        sql = 'update project set ratingPointCount = %s,ratingType = %s where projectNumber = %s'
        try:
            if int(number) < int(ratingPointCount):
                self.insert_and_update_sql(sql, ratingPointCount, ratingType, projectNumber)
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)

    def update_applyNumber(self, applyNumber, projectNumber):  # 更新报名人数
        result = self.query_projectData(projectNumber=projectNumber)
        number = result[5]  # 报名人数
        sql = 'update project set applyNumber = %s where projectNumber = %s'
        try:
            if number < applyNumber:
                self.insert_and_update_sql(sql, applyNumber, projectNumber)
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)

    def clear_text(self, url):  # 清空文本
        open(url, 'w').close()

    def read_data_csv(self, begin, place, end=None):  # 读取数据csv非负数
        data = []
        begin = self.nonnegative(begin)  # 用于判断是否为非负数
        if end is None:
            begin, end = 0, begin
        elif begin > end:
            raise Exception("begin不能比end大！！！")
        with open(place, encoding='gbk') as f:
            result = csv.reader(f)
            for index, row in enumerate(result):
                if index + 1 >= begin and index + 1 <= end:
                    data.append(row)
            return data

    # def write_data_csv(self,date,hours = '0'):#向csv文本写入数据
    #     with open(r"C:\Users\86176\Desktop\pythonScriptGenerate\freeDate.csv") as f:
    #         data=[row for row in csv.reader(f)]
    #         with open(r"C:\Users\86176\Desktop\pythonScriptGenerate\freeDate.csv","a+") as h:
    #             w = csv.writer(h)
    #             data[0][1] = hours
    #             data[0][0] = date
    #             self.clear_text(r"C:\Users\86176\Desktop\pythonScriptGenerate\freeDate.csv")
    #             for row in data:
    #                 w.writerow(row)

    def nonnegative(self, number):  # 判断是否为非负数
        number = str(number)  # 用于去除开头的0
        if re.match('^\d*$', number):
            return int(number)
        else:
            raise Exception("你输入的不是正整数！！！")

    def text_enter(self):  # 文本换行
        with open(self.script_place, 'a+', encoding="gbk") as f:
            f.write("\n")

    def query_projectData(self, projectNumber):  # 查询项目数据
        sql = 'select projectType,tenderOrganizationType,evaluationBidWay,judgeNumber,tenderWay,applyNumber,enterpriseCount,ratingPointCount,ratingType,evaluationReportNumber from project where projectNumber = %s'
        try:
            result = self.query_sql(sql, projectNumber)
            return result[0]
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)

    def select_expert(self, projectNumber):  # 查询专家数据库
        expert_name = []
        expert_username = []
        expert_password = []
        conn, cursor = self.connect_mysql()  # 连接数据库
        sql = 'select username,password,judgeName from expert where projectNumber = %s'
        try:
            cursor.execute(sql, projectNumber)
            result = cursor.fetchall()
            for i in result:
                expert_username.append(i[0])
                expert_password.append(i[1])
                expert_name.append(i[2])
            return expert_username, expert_password, expert_name
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)
        conn.close()
        cursor.close()

    def select_expert_username(self, projectNumber, judgeName):  # 查询专家身份证号
        conn, cursor = self.connect_mysql()  # 连接数据库
        sql = 'select username from expert where projectNumber = %s and judgeName = %s'
        try:
            cursor.execute(sql, (projectNumber, judgeName))
            expert_username = cursor.fetchone()
            return expert_username
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)
        conn.close()
        cursor.close()

    def select_isAgree(self, username, projectNumber):
        conn, cursor = self.connect_mysql()  # 连接数据库
        sql = 'select isAgree from expert where username = %s and projectNumber = %s'
        try:
            cursor.execute(sql, (username, projectNumber))
            expert_isAgree = cursor.fetchone()
            return expert_isAgree
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)
        conn.close()
        cursor.close()

    def get_nowUrl(self):  # 获取当前页面的url
        nowUrl = self.drive.current_url
        return nowUrl

    def is_url(self, str1):  # 判断url是否包含str1
        result = EC.url_contains(str1)
        return result(self.drive)

    def open_expert_url(self):  # 专家
        login_url = self.expert_login_url
        self.drive.get(login_url)
        self.drive.maximize_window()
        time.sleep(1)

    def savePictrue(self, locator):  # 保存图片
        # """
        # 保存图片到指定路径
        # :param locator:
        # :return:
        # """
        nowPath = self.now_path()
        pic = self.find_element(locator, 2)
        pic_url = pic.get_attribute('src')
        request.urlretrieve(pic_url, nowPath + r'xiaoe_testcase\1.png')

    def return_picture(self, locator):  # 返回验证码
        self.savePictrue(locator)
        code = self.get_PicPassword()
        return code

    def is_disabled(self, locator):  # 判断按钮是否禁用
        pic = self.find_element(locator, 3)
        time.sleep(0.2)
        text = pic.get_attribute('disabled')
        return text

    def get_attribute_value(self, locator, attribute):  # 获取属性值
        element = self.find_element(locator=locator, timeout=2)
        time.sleep(0.2)
        text = element.get_attribute(attribute)
        return text

    def frame(self, locator):  # 表单定位
        frame = self.find_element(locator, 3)
        self.drive.switch_to.frame(frame)

    @staticmethod
    def now_path():  # 获取当前路径
        path = os.path.abspath(os.path.dirname(__file__)).split('base')[0]
        return path

    def get_PicPassword(self):  # 识别图片验证码
        # """
        # 识别验证码
        # :return:
        # """
        nowPath = self.now_path()
        path = nowPath + r"xiaoe_testcase\1.png"
        ocr = ddddocr.DdddOcr()
        with open(path, 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        return res

    def find_element_alert(self, locator, timeout):
        # """
        # 定位单个元素，如果定位成功返回元素本身，定位失败返回false
        # :param locator: 定位器，如（"id","id属性值"）
        # :param timeout: 等待时间
        # :return: 返回元素本身
        # """
        try:
            element = WebDriverWait(self.drive, timeout).until(EC.presence_of_all_elements_located(locator))
            return element[len(element) - 1]
        except:
            print(str(locator) + "元素未找到!!!")
            return False

    def find_element(self, locator, timeout):
        # """
        # 定位单个元素，如果定位成功返回元素本身，定位失败返回false
        # :param locator: 定位器，如（"id","id属性值"）
        # :param timeout: 等待时间
        # :return: 返回元素本身
        # """
        try:
            element = WebDriverWait(self.drive, timeout).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(str(locator) + "元素未找到!!!")
            return False

    def click(self, locator):
        # """
        # 点击元素
        # :param locator:
        # :return:
        # """
        element = self.find_element(locator, 5)
        time.sleep(0.3)
        element.click()

    def js_click(self, locator):  # 利用js点击
        button = self.find_element(locator, 5)
        time.sleep(0.5)
        self.drive.execute_script("arguments[0].click();", button)
        return button

    def js_short_click(self, locator):  # js快速点击
        button = self.find_element(locator, 1)
        self.drive.execute_script("arguments[0].click();", button)
        return button

    def is_interactive(self, locator):  # 判断元素是否可交互
        # """
        # 判断元素是否可点击
        # :param locator:
        # :return:
        # """
        element = self.find_element(locator, 2)
        return element.is_enabled()

    def short_click(self, locator):
        # """
        # 点击元素
        # :param locator:
        # :return:
        # """
        element = self.find_element(locator, 2)
        element.click()

    def send_keys(self, locator, text):
        """
        :param locator: 定位器
        :param text: 输入内容
        :return:
        """
        element = self.find_element(locator, 5)
        element.clear()
        time.sleep(0.15)
        element.send_keys(text)

    def short_send_keys(self, locator, text):  # 短的
        """
        :param locator: 定位器
        :param text: 输入内容
        :return:
        """
        element = self.find_element(locator, 0.1)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):  # 将鼠标移动到指定元素并获取文本
        """
        获取弹窗文本
        :param locator:
        :return:
        """
        element = self.find_element_alert(locator, 1)
        action_chains = ActionChains(self.drive)
        try:
            action_chains.move_to_element(element).perform()
            message = element.text
            return message
        except:
            return None

    def roll_bottom(self):  # 滚动到最底部
        js = "var q =document.documentElement.scrollTop=10000"
        self.drive.execute_script(js)

    def roll_className(self, classname, distance):  # 指定窗口classname滑动
        """
        :param classname: 指定窗口的classname
        :param distance: 需要滑动的距离
        :return:
        """
        js_code = 'document.getElementsByClassName("' + str(classname) + '")[0].scrollBy(0, ' + str(distance) + ')'
        self.drive.execute_script(js_code)

    def roll_Id(self, id, distance=100000):  # 根据指定元素id进行滑动
        # """
        # :param classname: 指定窗口的id
        # :param distance: 需要滑动的距离
        # :return:
        # """
        js_code = 'document.getElementById("' + str(id) + '").scrollBy(0, ' + str(distance) + ')'
        self.drive.execute_script(js_code)

    def js_xpath_removeAttribute(self, locator):  # js移除属性
        element = self.find_element(locator, 5)
        self.drive.execute_script('arguments[0].removeAttribute(\"readonly\")', element)

    def js_xpath_modifyAttribute(self, locator, valueName='class', value='image-upload'):  # js修改属性
        element = self.find_element(locator, 5)
        time.sleep(1)
        self.drive.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", element, valueName, value)

    def upload_file(self, fileType):  # 上传文件
        time.sleep(2)
        if fileType == "pdf":
            send_keys(r"C:\Users\86176\Desktop\不同大小的文件和图片\招标文件.pdf")
        elif fileType == "img":
            send_keys(r"C:\Users\86176\Desktop\不同大小的文件和图片\保证金.jpg")
        elif fileType == "xezf":
            send_keys(r"C:\Users\86176\Desktop\不同大小的文件和图片\tender_file.xezf")
        elif fileType == "xetf":
            send_keys(r"C:\Users\86176\Desktop\不同大小的文件和图片\深圳CA.xetf")
        else:
            self.logger.debugText(errorText="文件类型错误：" + fileType)
        send_keys("{VK_RETURN}")

    def move_mouse(self, locator):  # 鼠标移动到指定元素
        """
        将鼠标移动到指定元素并悬浮
        :param locator:
        :return:
        """
        element = self.find_element(locator, 3)
        action_chains = ActionChains(self.drive)
        time.sleep(0.2)
        action_chains.move_to_element(element).perform()

    @staticmethod
    def get_nowTime_formatting():  # 获取当前时间没有符号的
        nowTime_noSumbol = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return nowTime_noSumbol

    def get_nowData(self, hours):  # 获取当前时间加n个小时
        timenow = datetime.datetime.now().replace(hour=0, minute=0, second=0)
        addTime = timenow + datetime.timedelta(hours=hours)
        return addTime.strftime("%Y-%m-%d %H:%M:%S")

    def get_date_day(self):  # 获取当前时间精确到天
        now_date_day = datetime.datetime.now().strftime("%Y%m%d")
        return now_date_day

    def get_nowtime(self, min):  # 获取当前时间加n分钟
        timenow = datetime.datetime.now()
        addTime = timenow + datetime.timedelta(minutes=min)
        return addTime.strftime("%Y-%m-%d %H:%M:%S")

    def get_noteCode_time(self):  # 获取通用短信验证码
        noteCode = datetime.datetime.now().strftime("%y%m%d")
        return noteCode

    def get_mobile_time(self):  # 获取电话号码后8位数
        mobile = datetime.datetime.now().strftime("%d%H%M%S")
        return mobile

    def handle_skip(self, num):  # 跳转句柄
        time.sleep(0.5)
        n = self.drive.window_handles
        self.drive.switch_to.window(n[num])

    def random_code(self):  # 产生3个随机的大写字母
        char1 = ''
        for i in range(3):
            b = chr(random.randint(65, 90))
            char1 = char1 + b
        return char1

    @staticmethod
    def random_score():  # 产生1到50随机数
        number = random.randint(1, 51)
        return number

    def clear(self, locator):
        """
        清空文本框
        :param locator:
        :return:
        """
        element = self.find_element(locator, 10)
        element.clear()

    def close(self):
        """
        关闭浏览器
        :return:
        """
        self.drive.quit()


if __name__ == '__main__':
    base = Base()
    base.now_path()
