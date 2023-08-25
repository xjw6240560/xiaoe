from base.base import Base
from selenium.webdriver.common.by import By
import time
import traceback
class LoginORrole(Base):
    #登录
    code_login = "//div//span[contains(text(),'验证码登录')]"
    username_input = "//input[@placeholder='请输入账户']"
    number_input = "//input[@placeholder='请输入手机号']"#手机号抽取系统
    password_input = "//input[@placeholder='请输入登录密码']"
    login_button = "//button[@class='el-button w-full el-button--primary']//span[text()='登录']"
    pictrue_input = "//input[@placeholder='请输入验证码']"
    pictrue = "//div[@class='verificationCode aui-padded-l-10']//img"
    alert = "//div[@role='alert']"#弹窗信息
    log_text = "//div[@role='alert']//p[contains(text(),'图形验证码错误')]"
    #注册
    register_user = "//button//span[text()='用户注册']"#点击用户注册
    register_tenderee = "//span[contains(text(),'招标人')]"#注册企业时选择招标人
    register_bidder = "//span[contains(text(),'投标人')]"#注册企业的时选择投标人
    register_tenderAgency = "//span[contains(text(),'招标代理')]"#注册企业的时候选择招标代理
    register_credit_code = "//input[@placeholder='请输入企业统一信用代码']"#社会统一信用代码
    register_enterpriseName = "//input[@placeholder='请输入企业名称']"#输入企业名称
    register_linkMan = "//input[@placeholder='请输入联系人']"#输入联系人
    register_mobile = "//input[@placeholder='请输入手机号']"#输入手机号
    register_imgCode = "//input[@placeholder='请输入图形码']"#输入图形验证码
    register_noteCode = "//input[@placeholder='请输入短信验证码']"#输入短信验证码
    register_password = "//input[@placeholder='请输入密码']"#输入密码
    register_affirm = "//button//span[contains(text(),'确 定')]"#确定按钮
    register_agreement = "//a[contains(text(),'用户协议')]/preceding-sibling::label/span"#同意用户协议

    #选择角色
    tenderee = "//div[@class='aui-margin-r-38 cursor-mouse']//div[text()='招标人']/preceding-sibling::div[@class='mask-layer']//img"#选择角色—招标人
    bidder = "//div[@class='aui-margin-r-38 cursor-mouse']//div[text()='投标人']/preceding-sibling::div[@class='mask-layer']//img"#投标人
    tenderAgency = "//div[@class='aui-margin-r-38 cursor-mouse']//div[text()='招标代理']/preceding-sibling::div[@class='mask-layer']//img"#招标代理

    #登录
    code_login_locator = (By.XPATH,code_login)
    username_locator = (By.XPATH, username_input)
    number_input_locator = (By.XPATH,number_input)
    password_locator = (By.XPATH, password_input)
    picture_locator = (By.XPATH, pictrue)
    alert_locator = (By.XPATH,alert)
    pictrue_input_locator = (By.XPATH, pictrue_input)
    login_btn_locator = (By.XPATH, login_button)
    log_text_locator = (By.XPATH, log_text)

    #注册
    register_user_locator = (By.XPATH,register_user)
    register_tenderee_locator = (By.XPATH,register_tenderee)
    register_bidder_locator = (By.XPATH,register_bidder)
    register_tenderAgency_locator = (By.XPATH,register_tenderAgency)
    register_credit_code_locator = (By.XPATH,register_credit_code)
    register_enterpriseName_locator = (By.XPATH,register_enterpriseName)
    register_linkMan_locator = (By.XPATH,register_linkMan)
    register_mobile_locator = (By.XPATH,register_mobile)
    register_imgCode_locator = (By.XPATH,register_imgCode)
    register_noteCode_locator = (By.XPATH,register_noteCode)
    register_password_locator = (By.XPATH,register_password)
    register_affirm_locator = (By.XPATH,register_affirm)
    register_agreement_locator = (By.XPATH,register_agreement)

    #选择角色
    tenderee_locator = (By.XPATH,tenderee)
    bidder_locator = (By.XPATH,bidder)
    tenderAgency_locator = (By.XPATH,tenderAgency)

    def send_number_input(self):#输入账号
        self.send_keys(self.number_input_locator,"15212345678")

    def send_password(self):#输入密码
        self.send_keys(self.pictrue_input_locator,"1")

    def login_button_click(self):#点击登录按钮
        self.click(self.login_btn_locator)

    def login(self,username,password):
        self.send_keys(self.username_locator,username)
        self.send_keys(self.password_locator,password)
        try:
            for i in range(200):
                self.savePictrue(self.picture_locator)
                yzm = self.getPicPassword()
                self.send_keys(self.pictrue_input_locator,yzm)
                self.click(self.login_btn_locator)
                time.sleep(0.5)
                text = self.get_attribute_value(attribute='class',locator=self.alert_locator)
                if text is not None:
                    time.sleep(1.2)
        except(Exception,BaseException):
            error = traceback.format_exc()
            print(error)
            pass

    def jiaoyi_login(self,role):#招标人或者招标代理选择
        if role == "0" :
            self.login(username=Base.username1[0],password="ndx111")
            self.tenderee_click()#点击招标人
        elif role == "1" :
            self.login(username=Base.username1[2],password=Base.password[1])
            self.tenderAgency_click()#点击招标代理
        else:
            print("角色错误"+role)

    def pictrue_input_send_keys(self):
        self.send_keys(self.pictrue_input_locator,"1")

    def code_login_click(self):#点击验证码登录
        self.click(self.code_login_locator)

    def register_user_click(self):#点击用户注册
        self.click(self.register_user_locator)

    def register_tenderee_click(self):#点击招标人
        self.click(self.register_tenderee_locator)

    def register_bidder_click(self):#点击投标人
        self.click(self.register_bidder_locator)

    def register_tenderAgency_click(self):#点击招标代理
        self.click(self.register_tenderAgency_locator)

    def register_credit_code_send_keys(self,creditCode):#输入社会统一信用代码
        self.send_keys(self.register_credit_code_locator,creditCode)

    def register_enterpriseName_send_keys(self,enterpriseName):#输入企业名称
        self.send_keys(self.register_enterpriseName_locator,enterpriseName)

    def register_linkMan_sends_keys(self):#输入联系人
        self.send_keys(self.register_linkMan_locator,"谢先生")

    def register_mobile_send_keys(self,mobile):#输入联系人手机号码
        self.send_keys(self.register_mobile_locator,mobile)

    def register_imgCode_send_keys(self):#输入图片验证码
        self.send_keys(self.register_imgCode_locator,"1")

    def register_noteCode_send_keys(self,noteCode):#输入短信验证码
        self.send_keys(self.register_noteCode_locator,noteCode)

    def register_password_send_keys(self):#输入密码
        self.send_keys(self.register_password_locator,"ndx111")

    def register_affirm_click(self):#点击确认
        self.click(self.register_affirm_locator)

    def register_agreement_click(self):#点击同意协议
        self.click(self.register_agreement_locator)

    def tenderee_click(self):#点击招标人角色
        self.click(self.tenderee_locator)

    def bidder_click(self):#点击投标人角色
        self.click(self.bidder_locator)

    def tenderAgency_click(self):#点击招标代理
        self.click(self.tenderAgency_locator)