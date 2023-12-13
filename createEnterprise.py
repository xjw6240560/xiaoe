import time
import unittest
from xiaoeXapth_package.deal_or_bidOpen.home_page_or_workbench import Home_page_or_workbench
from xiaoeXapth_package.deal_or_bidOpen.bidOpen import BidOpen
from xiaoeXapth_package.deal_or_bidOpen.create_project import CreateProjectMethod
from xiaoeXapth_package.deal_or_bidOpen.login_registerORselect_role import LoginORrole
from xiaoeXapth_package.deal_or_bidOpen.evaluationBid_entrance import EvaluationBid_entrance
from xiaoeXapth_package.deal_or_bidOpen.expert import Expert
from base.base import Base


class Demo(unittest.TestCase):
    def setUp(self):
        self.base = Base()
        self.createProjectMethod = CreateProjectMethod()
        self.loginORrole = LoginORrole()
        self.home_page_or_workbench = Home_page_or_workbench()
        self.bidOpen = BidOpen()
        self.evaluationBid_entrance = EvaluationBid_entrance()
        self.expert = Expert()
        self.noteCode = self.loginORrole.get_noteCode_time()
        self.createProjectMethod.open_deal_url()

    def test_create_enterprise(self):  # 注册企业
        for i in range(len(self.base.username)):
            # enterpriseName = "测试企业" + str(i+1)
            enterpriseName = self.base.enterpriseName[i+1]
            self.loginORrole.register_user_click()  # 点击用户注册
            self.loginORrole.register_tenderAgency_click()  # 选择招标代理
            self.loginORrole.register_tenderee_click()  # 点击招标人
            self.loginORrole.register_bidder_click()  # 点击投标人
            code = self.loginORrole.random_code()
            mobile = "158" + self.loginORrole.get_mobile_time()
            self.loginORrole.register_credit_code_send_keys(str(code) + mobile)  # 输入社会统一信用代码
            self.loginORrole.register_enterpriseName_send_keys(enterpriseName)  # 输入企业名称
            self.loginORrole.register_linkMan_sends_keys()  # 输入联系人
            # self.loginORrole.register_mobile_send_keys(mobile)  # 输入联系人手机号
            self.loginORrole.register_mobile_send_keys(self.base.username[i+1])  # 输入联系人手机号
            self.loginORrole.register_imgCode_send_keys()  # 输入图片验证码
            self.loginORrole.register_noteCode_send_keys(self.noteCode)  # 输入短信验证码
            self.loginORrole.register_password_send_keys()  # 输入密码
            self.loginORrole.register_agreement_click()  # 点击同意协议
            self.loginORrole.register_affirm_click()  # 点击注册
            time.sleep(1)
            self.loginORrole.code_login_click()  # 点击验证码登录
            self.loginORrole.platform_click()  # 点击平台选择下拉框
            self.loginORrole.area_click(platform=0)  # 选择平台
            self.loginORrole.register_mobile_send_keys(self.base.username[i+1])
            # self.loginORrole.register_mobile_send_keys(mobile)
            self.loginORrole.pictrue_input_send_keys()
            self.loginORrole.register_noteCode_send_keys(self.noteCode)
            self.loginORrole.login_button_click()  # 点击登录
            time.sleep(2)
            self.loginORrole.improve_information(enterpriseName=enterpriseName)
            time.sleep(2)
            self.createProjectMethod.open_deal_url()

    def test_improve_information(self):  # 完善企业信息
        self.loginORrole.code_login_click()  # 点击验证码登录
        self.loginORrole.platform_click()  # 点击平台选择下拉框
        self.loginORrole.area_click(platform=0)  # 选择平台
        self.loginORrole.register_mobile_send_keys('15222222222')
        self.loginORrole.pictrue_input_send_keys()
        self.loginORrole.register_noteCode_send_keys(self.noteCode)
        self.loginORrole.login_button_click()  # 点击登录
        time.sleep(2)
        self.loginORrole.improve_information(enterpriseName='福建尤建科技有限公司')

    def tearDown(self):
        self.base.close()


if __name__ == '__main__':
    unittest.main()
