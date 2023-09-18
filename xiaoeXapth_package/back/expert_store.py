# -*- coding: utf-8 -*-
# @Time : 2023-09-18 15:18
# @Author : 皮卡丘
from base.base import Base
import time
import traceback
from xiaoeXapth_package.deal_or_bidOpen.home_page_or_workbench import Home_page_or_workbench
from selenium.webdriver.common.by import By


class Expert_store(Base):
    base = Base()
    home_page_or_workbench = Home_page_or_workbench()
    mobile = "//input[@placeholder='请输入手机号码']"  # 输入手机号码
    passsword = "//input[@placeholder='请输入密码']"  # 输入密码
    picCode_input = "//input[@placeholder='请输入图形验证码']"  # 输入图片验证码
    pic_img = '//*[@id="loginForm"]/form/div[3]/div/div/div[2]/img'  # 验证码图片
    confirm = "//span[contains(text(),' 确 定 ')]"  # 点击确定
    expert_manage = "//span[contains(text(),'专家库管理')]"  # 点击专家库管理
    store_expert = "//span[contains(text(),'在库专家')]"  # 点击在库专家
    add_expert = "//span[contains(text(),'新增专家 ')]"  # 点击新增专家
    expert_name = "//input[@placeholder='请输入专家姓名']"  # 输入专家姓名
    expert_mobile = "//input[@placeholder='请输入联系电话']"  # 输入专家联系电话
    expert_idCard = "//input[@placeholder='请输入身份证号']"  # 输入专家身份证号
    expert_pwd = "//input[@placeholder='请输入6-16位登录密码']"  # 输入专家密码
    expert_work = "//input[@placeholder='请输入工作单位']"  # 输入工作单位
    in_expert = "//input[@placeholder='请选择专家库']"  # 点击专家库
    test_store = "//span[contains(text(),'测试1')]"  # 点击测试1仓库

    mobile_locator = (By.XPATH, mobile)
    passsword_locator = (By.XPATH, passsword)
    picCode_input_locator = (By.XPATH, picCode_input)
    pic_img_locator = (By.XPATH, pic_img)
    confirm_locator = (By.XPATH, confirm)
    expert_manage_locator = (By.XPATH, expert_manage)
    store_expert_locator = (By.XPATH, store_expert)
    add_expert_locator = (By.XPATH, add_expert)
    expert_name_locator = (By.XPATH, expert_name)
    expert_mobile_locator = (By.XPATH, expert_mobile)
    expert_idCard_locator = (By.XPATH, expert_idCard)
    expert_pwd_locator = (By.XPATH, expert_pwd)
    expert_work_locator = (By.XPATH, expert_work)
    in_expert_locator = (By.XPATH, in_expert)
    test_store_locator = (By.XPATH, test_store)

    def mobile_send_keys(self):  # 输入手机号码
        self.send_keys(self.mobile_locator, '15212345678')

    def passsword_send_keys(self):  # 输入密码
        self.send_keys(self.passsword_locator, 'ndx111')

    def picCode_input_send_keys(self):  # 输入图片验证码
        code = self.return_picture(self.pic_img_locator)
        self.send_keys(self.picCode_input_locator, code)

    def confirm_click(self):  # 点击确定
        self.click(self.confirm_locator)

    def expert_manage_click(self):  # 点击专家库管理
        self.click(self.expert_manage_locator)

    def store_expert_click(self):  # 点击在库专家
        self.click(self.store_expert_locator)

    def add_expert_click(self):  # 点击新增专家
        self.click(self.add_expert_locator)

    def expert_name_send_keys(self, expertName):  # 输入专家姓名
        self.send_keys(self.expert_name_locator, expertName)

    def expert_mobile_send_keys(self, expertMobile):  # 输入专家联系电话
        self.send_keys(self.expert_mobile_locator, expertMobile)

    def expert_idCard_send_keys(self, expertIdCard):  # 输入专家身份证号
        self.send_keys(self.expert_idCard_locator, expertIdCard)

    def expert_pwd_send_keys(self):  # 输入专家密码
        self.send_keys(self.expert_pwd_locator, 'ndx111')

    def expert_work_send_keys(self):  # 输入工作单位
        self.send_keys(self.expert_work_locator, '福建省厦门市湖里区')

    def in_expert_click(self):  # 点击专家库
        self.click(self.in_expert_locator)

    def test_store_click(self):  # 点击测试1仓库
        self.click(self.test_store_locator)

    def login_back(self):  # 登录总后台
        self.mobile_send_keys()  # 输入手机号
        self.passsword_send_keys()  # 输入密码
        try:
            for i in range(200):
                self.picCode_input_send_keys()  # 输入验证码
                self.confirm_click()  # 点击确定
                time.sleep(0.5)
                if self.is_url(self.back_url) is not True:
                    break
        except(Exception, BaseException):
            error = traceback.format_exc()
            print(error)
            pass

    def create_expert(self, expertName, expertMobile, expertIdCard):  # 创建专家
        self.add_expert_click()  # 点击添加专家
        self.expert_name_send_keys(expertName)  # 输入专家名字
        self.expert_mobile_send_keys(expertMobile)  # 输入专家手机号
        self.expert_idCard_send_keys(expertIdCard)  # 输入专家身份证号
        self.expert_pwd_send_keys()  # 输入专家密码
        self.expert_work_send_keys()  # 输入专家工作单位
        self.in_expert_click()  # 点击专家库
        self.test_store_click()  # 点击测试1仓库
        self.base.click(self.expert_pwd_locator)  # 点击密码
        self.confirm_click()  # 点击确认
        errortext = self.home_page_or_workbench.errorMessage_text(type='warning')
        return errortext
