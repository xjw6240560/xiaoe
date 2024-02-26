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
import re
from selenium.webdriver.edge.service import Service
from xiaoe_data import *


class Base(Test_xiaoe_data):
    logger = Logger()
    # 直接创建Service实例
    path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe'
    ser = Service(executable_path=path)
    op = Options()
    op.page_load_strategy = 'eager'
    drive = webdriver.Edge(options=op, service=ser)
    drive.maximize_window()
    # drive.set_window_position(-2000, -2000)
    time1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert = "//div[@role='alert']"  # 弹窗信息
    alert_locator = (By.XPATH, alert)
    csv_place = r"C:\Users\86176\Desktop\pythonScriptGenerate\data.csv"  # 数据地址
    script_place = r"C:\Users\86176\Desktop\pythonScriptGenerate\pythonScript.txt"  # 存放xpath地址

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
        #        self.drive.maximize_window()
        time.sleep(1)

    def open_extract_system_url(self):  # 专家抽取系统
        """
        打开专家抽取系统登录页面
        :return:
        """
        login_url = self.extract_login_url
        self.drive.get(login_url)
        #        self.drive.maximize_window()
        time.sleep(1)

    def open_back_url(self):  # 总后台
        """
        打开总后台登录页面
        :return:
        """
        login_url = self.back_url
        self.drive.get(login_url)
        #        self.drive.maximize_window()
        time.sleep(1)

    def open_manage_url(self):
        """
        打开监管台登录页面
        :return:
        """
        login_url = "http://manage.han.com/#/"
        self.drive.get(login_url)
        #        self.drive.maximize_window()
        time.sleep(1)

    @staticmethod
    def clear_text(url):  # 清空文本
        open(url, 'w').close()

    def read_data_csv(self, begin, place, end=None):  # 读取数据csv非负数
        data = []
        begin = self.nonnegative_number(begin)  # 用于判断是否为非负数
        if end is None:
            begin, end = 0, begin
        elif begin > end:
            raise Exception("begin不能比end大！！！")
        with open(place, encoding='gbk') as f:
            result = csv.reader(f)
            for index, row in enumerate(result):
                if begin <= index + 1 <= end:
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

    @staticmethod
    def retry(func):  # 报错重新执行
        def wrapper(*args, **kwargs):
            for i in range(3):
                result = func(*args, **kwargs)
                if result is not False:
                    break

        return wrapper

    @staticmethod
    def nonnegative_number(number):  # 判断是否为非负数
        number = str(number)  # 用于去除开头的0
        if re.match('^\d*$', number):
            return int(number)
        else:
            raise Exception("你输入的不是正整数！！！")

    def text_enter(self):  # 文本换行
        with open(self.script_place, 'a+', encoding="gbk") as f:
            f.write("\n")

    def get_nowUrl(self):  # 获取当前页面的url
        nowUrl = self.drive.current_url
        return nowUrl

    def is_url(self, str1):  # 判断url是否包含str1
        result = EC.url_contains(str1)
        return result(self.drive)

    def open_expert_url(self):  # 专家
        login_url = self.expert_login_url
        self.drive.get(login_url)
        #        self.drive.maximize_window()
        time.sleep(1)

    def savePicture(self, locator):  # 保存图片
        # """
        # 保存图片到指定路径
        # :param locator:
        # :return:
        # """
        nowPath = self.now_path()
        pic = self.find_element(locator, 2)
        if pic is not False:
            time.sleep(0.2)
            pic_url = pic.get_attribute('src')
            request.urlretrieve(pic_url, nowPath + r'xiaoe_testcase\1.png')
        else:
            return pic

    def return_picture(self, locator):  # 返回验证码
        self.savePicture(locator)
        code = self.get_PicPassword()
        return code

    def is_disabled(self, locator):  # 判断按钮是否禁用
        element = self.find_element(locator, 3)
        time.sleep(0.2)
        text = element.get_attribute('disabled')
        return text

    @staticmethod
    def is_hide(element):  # 判断元素是否被隐藏
        text = element.get_attribute('style')
        if 'display: none;' in str(text):
            return True
        else:
            return False

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

    def find_element(self, locator, timeout, position=0):
        # """
        # 定位单个元素，如果定位成功返回元素本身，定位失败返回false
        # :param locator: 定位器，如（"id","id属性值"）
        # :param timeout: 等待时间
        # :return: 返回元素本身
        # """
        try:
            element = WebDriverWait(self.drive, timeout).until(EC.presence_of_all_elements_located(locator))
            isHide = self.is_hide(element=element[0])  # 判断元素是否被隐藏
            if element[0].is_enabled() & isHide is False:
                return element[position]
            else:
                return False
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
        if element is not False:
            time.sleep(0.5)
            element.click()
        else:
            return element

    def error_detemine(self, result, isFalseText, isNoneText, elseText='', projectNumber='', bidder=''):
        if result is False:
            self.logger.debugText(projectNumber=projectNumber, bidder=bidder,
                                  errorText=isFalseText)
        elif result is None:
            self.logger.debugText(projectNumber=projectNumber, bidder=bidder,
                                  errorText=isNoneText)
        else:
            self.logger.debugText(projectNumber=projectNumber, bidder=bidder,
                                  errorText=elseText)

    def js_click(self, locator):  # 利用js点击
        button = self.find_element(locator, 5)
        if button is not False:
            time.sleep(0.5)
            self.drive.execute_script("arguments[0].click();", button)
        else:
            return button

    def js_short_click(self, locator):  # js快速点击
        button = self.find_element(locator, 1)
        if button is not False:
            time.sleep(0.3)
            self.drive.execute_script("arguments[0].click();", button)
        else:
            return button

    def is_interactive(self, locator):  # 判断元素是否可交互
        # """
        # 判断元素是否可点击
        # :param locator:
        # :return:
        # """
        element = self.find_element(locator, 2)
        if element is False:
            return False
        else:
            return element.is_enabled()

    def short_click(self, locator):
        # """
        # 点击元素
        # :param locator:
        # :return:
        # """
        element = self.find_element(locator, 2)
        if element is not False:
            element.click()
        else:
            return element

    def send_keys(self, locator, text):
        """
        :param locator: 定位器
        :param text: 输入内容
        :return:
        """
        element = self.find_element(locator, 5)
        if element is not False:
            element.clear()
            time.sleep(0.15)
            element.send_keys(text)
        else:
            return element

    def short_send_keys(self, locator, text):  # 短的
        """
        :param locator: 定位器
        :param text: 输入内容
        :return:
        """
        element = self.find_element(locator, 0.1)
        if element is not False:
            result = self.is_disabled(locator=locator)
            if result == 'true':
                return False
            else:
                element.clear()
                element.send_keys(text)
        else:
            return element

    def js_send_keys(self, locator, text):  # 利用js发送
        button = self.find_element(locator, 5)
        if button is not False:
            time.sleep(0.5)
            self.drive.execute_script("arguments[0].value=" + str(text) + "", button)
        else:
            return button

    def js_short_send_keys(self, locator, text):  # 利用js发送
        button = self.find_element(locator, 1)
        if button is not False:
            time.sleep(0.5)
            self.drive.execute_script("arguments[0].value=" + str(text) + "", button)
        else:
            return button

    @staticmethod
    def random_uploadPicture():  # 随机上传图片格式
        result = random.randint(0, 2)
        if result == 0:
            fileUrl = r'file\background.jpeg'
        elif result == 1:
            fileUrl = r'file\测试电子回单.png'
        else:
            fileUrl = r'file\身份证国徽面.jpg'
        return fileUrl

    def get_text(self, locator, position=-1):  # 将鼠标移动到指定元素并获取文本
        """
        获取弹窗文本
        :param position:
        :param locator:
        :return:
        """
        time.sleep(1)
        element = self.find_element(locator=locator, timeout=1, position=position)
        action_chains = ActionChains(self.drive)
        try:
            action_chains.move_to_element(element).perform()
            message = element.text
            return message
        except:
            return None

    def roll_bottom(self):  # 滑动到最底部
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
        if element is not False:
            time.sleep(1)
            self.drive.execute_script('arguments[0].removeAttribute(\"readonly\")', element)
        elif element is False:
            return element
        else:
            self.logger.debugText(errorText=element)

    def js_xpath_modifyAttribute(self, locator, valueName='class', value='image-upload'):  # js修改属性
        element = self.find_element(locator, 5)
        if element is not False:
            self.drive.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", element, valueName, value)
        elif element is False:
            return element
        else:
            self.logger.debugText(errorText=element)

    def upload_file(self, fileType):  # 上传文件
        time.sleep(2)
        match fileType:
            case "pdf":
                send_keys(r"C:\Users\86176\Desktop\不同大小的文件和图片\招标文件.pdf")
            case "img":
                send_keys(r"C:\Users\86176\Desktop\不同大小的文件和图片\保证金.jpg")
            case "xezf":
                send_keys(r"C:\Users\86176\Desktop\不同大小的文件和图片\tender_file.xezf")
            case "xetf":
                send_keys(r"C:\Users\86176\Desktop\不同大小的文件和图片\深圳CA.xetf")
            case _:
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

    @staticmethod
    def get_nowData(hours):  # 获取当前时间加n个小时
        nowTime = datetime.datetime.now().replace(hour=0, minute=0, second=0)
        addTime = nowTime + datetime.timedelta(hours=hours)
        return addTime.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_date_day():  # 获取当前时间精确到天
        now_date_day = datetime.datetime.now().strftime("%Y%m%d")
        return now_date_day

    @staticmethod
    def get_nowTime(min):  # 获取当前时间加n分钟
        nowTime = datetime.datetime.now()
        addTime = nowTime + datetime.timedelta(minutes=min)
        return addTime.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_noteCode_time():  # 获取通用短信验证码
        noteCode = datetime.datetime.now().strftime("%y%m%d")
        return noteCode

    @staticmethod
    def get_mobile_time():  # 获取电话号码后8位数
        mobile = datetime.datetime.now().strftime("%d%H%M%S")
        return mobile

    def handle_skip(self, num):  # 跳转句柄
        time.sleep(0.5)
        n = self.drive.window_handles
        self.drive.switch_to.window(n[num])

    @staticmethod
    def random_code():  # 产生3个随机的大写字母
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
