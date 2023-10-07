from base.base import Base
from selenium.webdriver.common.by import By
import time
import traceback


class LoginORrole(Base):
    base = Base()
    # 登录
    code_login = "//div//span[contains(text(),'验证码登录')]"
    username_input = "//input[@placeholder='请输入账户']"
    number_input = "//input[@placeholder='请输入手机号']"  # 手机号抽取系统
    password_input = "//input[@placeholder='请输入登录密码']"
    login_button = "//button[@class='el-button w-full el-button--primary']//span[text()='登录']"
    pictrue_input = "//input[@placeholder='请输入验证码']"
    pictrue = "//div[@class='verificationCode aui-padded-l-10']//img"
    log_text = "//div[@role='alert']//p[contains(text(),'图形验证码错误')]"
    # 注册
    register_user = "//button//span[text()='用户注册']"  # 点击用户注册
    register_tenderee = "//span[contains(text(),'招标人')]"  # 注册企业时选择招标人
    register_bidder = "//span[contains(text(),'投标人')]"  # 注册企业的时选择投标人
    register_tenderAgency = "//span[contains(text(),'招标代理')]"  # 注册企业的时候选择招标代理
    register_credit_code = "//input[@placeholder='请输入企业统一信用代码']"  # 社会统一信用代码
    register_enterpriseName = "//input[@placeholder='请输入企业名称']"  # 输入企业名称
    register_linkMan = "//input[@placeholder='请输入联系人']"  # 输入联系人
    register_mobile = "//input[@placeholder='请输入手机号']"  # 输入手机号
    register_imgCode = "//input[@placeholder='请输入图形码']"  # 输入图形验证码
    register_noteCode = "//input[@placeholder='请输入短信验证码']"  # 输入短信验证码
    register_password = "//input[@placeholder='请输入密码']"  # 输入密码
    register_affirm = "//button//span[contains(text(),'确 定')]"  # 确定按钮
    register_agreement = "//a[contains(text(),'用户协议')]/preceding-sibling::label/span"  # 同意用户协议

    # 选择角色
    tenderee = "//div[@class='aui-margin-r-38 cursor-mouse']//div[text()='招标人']/preceding-sibling::div[@class='mask-layer']//img"  # 选择角色—招标人
    bidder = "//div[@class='aui-margin-r-38 cursor-mouse']//div[text()='投标人']/preceding-sibling::div[@class='mask-layer']//img"  # 投标人
    tenderAgency = "//div[@class='aui-margin-r-38 cursor-mouse']//div[text()='招标代理']/preceding-sibling::div[@class='mask-layer']//img"  # 招标代理

    # 完善企业信息
    business_license = "//label[contains(text(),'企业营业执照:')]/following-sibling::div/div/div/input"  # 点击营业执照上传
    registered_capital = "//label[contains(text(),'注册资本')]/following-sibling::div/div/input"  # 输入注册资本
    address = "//label[contains(text(),'详细地址')]/following-sibling::div/div/textarea"  # 输入详细地址
    identity_card01 = "/html/body/div/div/div[2]/div/form/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/input"  # 点击法人身份证人像面
    identity_card02 = "/html/body/div/div/div[2]/div/form/div[2]/div/div/div[1]/div/div[2]/div[2]/div/div/div/div/input"  # 点击法人身份证国徽面
    legalPersonName = "//label[contains(text(),'法人姓名')]/following-sibling::div/div/input"  # 输入法人姓名
    legalPersonIdCardNo = "//label[contains(text(),'法人身份证号:')]/following-sibling::div/div/input"  # 输入法人身份证号
    legalPersonMobile = "/html/body/div/div/div[2]/div/form/div[2]/div/div/div[4]/div/div[1]/input"  # 输入法人手机号
    bankOpenPermit = "//label[contains(text(),'开户许可证:')]/following-sibling::div/div/div/input"  # 点击开户许可证
    enterpriseName = "//label[contains(text(),'开户户名:')]/following-sibling::div/div/input"  # 输入开户户名
    bankDot = "//label[contains(text(),'开户支行:')]/following-sibling::div/div/input"  # 输入开户支行
    bankCardNo = "//label[contains(text(),'银行账号:')]/following-sibling::div/div/input"  # 输入银行账号
    idCardNo = "//label[contains(text(),'经办人身份证号:')]/following-sibling::div/div/input"  # 输入经办人身份证号
    mobile = "/html/body/div/div/div[2]/div/form/div[4]/div[2]/div/div[3]/div/div/input"  # 输入经办人手机号
    email = "//label[contains(text(),'邮箱:')]/following-sibling::div/div/input"  # 输入经办人邮箱
    graphic_code = "//label[contains(text(),'图形码')]/following-sibling::div/div/div/input"  # 输入图形码
    code = "//label[contains(text(),'验证码')]/following-sibling::div/div/div/input"  # 输入验证码
    submit = "//span[contains(text(),'提交')]"  # 点击提交

    # 登录
    code_login_locator = (By.XPATH, code_login)
    username_locator = (By.XPATH, username_input)
    number_input_locator = (By.XPATH, number_input)
    password_locator = (By.XPATH, password_input)
    picture_locator = (By.XPATH, pictrue)
    pictrue_input_locator = (By.XPATH, pictrue_input)
    login_btn_locator = (By.XPATH, login_button)
    log_text_locator = (By.XPATH, log_text)

    # 注册
    register_user_locator = (By.XPATH, register_user)
    register_tenderee_locator = (By.XPATH, register_tenderee)
    register_bidder_locator = (By.XPATH, register_bidder)
    register_tenderAgency_locator = (By.XPATH, register_tenderAgency)
    register_credit_code_locator = (By.XPATH, register_credit_code)
    register_enterpriseName_locator = (By.XPATH, register_enterpriseName)
    register_linkMan_locator = (By.XPATH, register_linkMan)
    register_mobile_locator = (By.XPATH, register_mobile)
    register_imgCode_locator = (By.XPATH, register_imgCode)
    register_noteCode_locator = (By.XPATH, register_noteCode)
    register_password_locator = (By.XPATH, register_password)
    register_affirm_locator = (By.XPATH, register_affirm)
    register_agreement_locator = (By.XPATH, register_agreement)

    # 选择角色
    tenderee_locator = (By.XPATH, tenderee)
    bidder_locator = (By.XPATH, bidder)
    tenderAgency_locator = (By.XPATH, tenderAgency)

    # 完善企业信息
    business_license_locator = (By.XPATH, business_license)
    registered_capital_locator = (By.XPATH, registered_capital)
    address_locator = (By.XPATH, address)
    identity_card01_locator = (By.XPATH, identity_card01)
    identity_card02_locator = (By.XPATH, identity_card02)
    legalPersonName_locator = (By.XPATH, legalPersonName)
    legalPersonIdCardNo_locator = (By.XPATH, legalPersonIdCardNo)
    legalPersonMobile_locator = (By.XPATH, legalPersonMobile)
    bankOpenPermit_locator = (By.XPATH, bankOpenPermit)
    enterpriseName_locator = (By.XPATH, enterpriseName)
    bankDot_locator = (By.XPATH, bankDot)
    bankCardNo_locator = (By.XPATH, bankCardNo)
    idCardNo_locator = (By.XPATH, idCardNo)
    mobile_locator = (By.XPATH, mobile)
    email_locator = (By.XPATH, email)
    graphic_code_locator = (By.XPATH, graphic_code)
    code_locator = (By.XPATH, code)
    submit_locator = (By.XPATH, submit)

    def send_number_input(self):  # 输入账号
        self.send_keys(self.number_input_locator, "15212345678")

    def send_password(self):  # 输入密码
        self.send_keys(self.pictrue_input_locator, "1")

    def login_button_click(self):  # 点击登录按钮
        self.click(self.login_btn_locator)

    def login(self, username, password):
        self.send_keys(self.username_locator, username)
        self.send_keys(self.password_locator, password)
        try:
            for i in range(200):
                self.savePictrue(self.picture_locator)
                yzm = self.get_PicPassword()
                self.send_keys(self.pictrue_input_locator, yzm)
                self.click(self.login_btn_locator)
                time.sleep(0.5)
                if self.is_url(self.deal_login_url) is not True:
                    self.logger.debugText(errorText='登陆成功！', bidder=username)
                    break
        except(Exception, BaseException):
            self.logger.debugText(errorText='登陆成功！', bidder=username)
            error = traceback.format_exc()
            pass

    def jiaoyi_login(self, role):  # 招标人或者招标代理选择
        if role == "0":
            self.login(username=Base.username1[0], password="ndx111")
            self.tenderee_click()  # 点击招标人
        elif role == "1":
            self.login(username=Base.username1[2], password=Base.password[1])
            self.tenderAgency_click()  # 点击招标代理
        else:
            print("角色错误" + role)

    def pictrue_input_send_keys(self):
        self.send_keys(self.pictrue_input_locator, "1")

    def code_login_click(self):  # 点击验证码登录
        self.click(self.code_login_locator)

    def register_user_click(self):  # 点击用户注册
        self.click(self.register_user_locator)

    def register_tenderee_click(self):  # 点击招标人
        self.click(self.register_tenderee_locator)

    def register_bidder_click(self):  # 点击投标人
        self.click(self.register_bidder_locator)

    def register_tenderAgency_click(self):  # 点击招标代理
        self.click(self.register_tenderAgency_locator)

    def register_credit_code_send_keys(self, creditCode):  # 输入社会统一信用代码
        self.send_keys(self.register_credit_code_locator, creditCode)

    def register_enterpriseName_send_keys(self, enterpriseName):  # 输入企业名称
        self.send_keys(self.register_enterpriseName_locator, enterpriseName)

    def register_linkMan_sends_keys(self):  # 输入联系人
        self.send_keys(self.register_linkMan_locator, "谢先生")

    def register_mobile_send_keys(self, mobile):  # 输入联系人手机号码
        self.send_keys(self.register_mobile_locator, mobile)

    def register_imgCode_send_keys(self):  # 输入图片验证码
        self.send_keys(self.register_imgCode_locator, "1")

    def register_noteCode_send_keys(self, noteCode):  # 输入短信验证码
        self.send_keys(self.register_noteCode_locator, noteCode)

    def register_password_send_keys(self):  # 输入密码
        self.send_keys(self.register_password_locator, "ndx111")

    def register_affirm_click(self):  # 点击确认
        self.click(self.register_affirm_locator)

    def register_agreement_click(self):  # 点击同意协议
        self.click(self.register_agreement_locator)

    def tenderee_click(self):  # 点击招标人角色
        self.click(self.tenderee_locator)

    def bidder_click(self):  # 点击投标人角色
        self.js_click(self.bidder_locator)

    def tenderAgency_click(self):  # 点击招标代理
        self.click(self.tenderAgency_locator)

    # 完善企业信息
    def business_license_send_keys(self):  # 点击营业执照上传
        self.js_xpath_modifyAttribute(self.business_license_locator)
        self.send_keys(self.business_license_locator,
                       r'C:\Users\86176\Desktop\不同大小的文件和图片\mypictures\测试营业执照.jpg')

    def registered_capital_send_keys(self):  # 输入注册资本
        self.send_keys(self.registered_capital_locator, '200')

    def address_send_keys(self):  # 输入详细地址
        self.send_keys(self.address_locator, '高林中路108号')

    def identity_card01_send_keys(self):  # 点击法人身份证人像面
        self.js_xpath_modifyAttribute(self.identity_card01_locator)
        self.send_keys(self.identity_card01_locator,
                       r'C:\Users\86176\Desktop\不同大小的文件和图片\mypictures\身份证头像面.jpg')

    def identity_card02_send_keys(self):  # 点击法人身份证国徽面
        self.js_xpath_modifyAttribute(self.identity_card02_locator)  # 修改js属性
        self.send_keys(self.identity_card02_locator,
                       r'C:\Users\86176\Desktop\不同大小的文件和图片\mypictures\身份证国徽面.jpg')

    def legalPersonName_send_keys(self):  # 输入法人姓名
        self.send_keys(self.legalPersonName_locator, '谢先生')

    def legalPersonIdCardNo_send_keys(self):  # 输入法人身份证号
        self.send_keys(self.legalPersonIdCardNo_locator, '361003193505091274')

    def legalPersonMobile_send_keys(self):  # 输入法人手机号
        self.send_keys(self.legalPersonMobile_locator, '15212345678')

    def bankOpenPermit_send_keys(self):  # 点击开户许可证
        self.js_xpath_modifyAttribute(self.bankOpenPermit_locator)  # 修改js属性
        self.send_keys(self.bankOpenPermit_locator,
                       r'C:\Users\86176\Desktop\不同大小的文件和图片\mypictures\测试经营许可证.jpg')

    def enterpriseName_send_keys(self, enterprise):  # 输入开户户名
        self.send_keys(self.enterpriseName_locator, enterprise)

    def bankDot_send_keys(self):  # 输入开户支行
        self.send_keys(self.bankDot_locator, '建设银行报业支行')

    def bankCardNo_send_keys(self):  # 输入银行账号
        self.send_keys(self.bankCardNo_locator, '100086')

    def idCardNo_send_keys(self):  # 输入经办人身份证号
        self.send_keys(self.idCardNo_locator, '360481192401176199')

    def mobile_send_keys(self):  # 输入经办人手机号
        self.send_keys(self.mobile_locator, '15212345678')

    def email_send_keys(self):  # 输入经办人邮箱
        self.send_keys(self.email_locator, '1234@qq.com')

    def graphic_code_send_keys(self):  # 输入图形码
        self.send_keys(self.graphic_code_locator, '1')

    def code_send_keys(self, code):  # 输入验证码
        self.send_keys(self.code_locator, code)

    def submit_click(self):  # 点击提交
        self.click(self.submit_locator)

    def improve_information(self, enterpriseName):  # 完善信息
        self.business_license_send_keys()  # 点击企业营业执照
        self.registered_capital_send_keys()  # 输入注册资本
        self.address_send_keys()  # 输入详细地址
        self.identity_card01_send_keys()  # 点击法人身份证人像面
        time.sleep(0.5)
        self.identity_card02_send_keys()  # 点击法人身份证国徽面
        self.legalPersonName_send_keys()  # 输入法人姓名
        self.legalPersonIdCardNo_send_keys()  # 输入法人身份证号
        self.legalPersonMobile_send_keys()  # 输入法人手机号
        self.bankOpenPermit_send_keys()  # 点击开户许可证
        time.sleep(1)
        self.enterpriseName_send_keys(enterprise=enterpriseName)  # 输入开户户名
        self.bankDot_send_keys()  # 输入开户支行
        self.bankCardNo_send_keys()  # 输入银行账号
        self.idCardNo_send_keys()  # 输入经办人身份证号
        self.email_send_keys()  # 输入经办人邮箱
        self.graphic_code_send_keys()  # 输入图形码
        code = self.get_noteCode_time()
        self.code_send_keys(code)  # 输入验证码
        self.submit_click()  # 点击提交
