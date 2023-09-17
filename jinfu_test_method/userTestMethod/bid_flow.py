from selenium.webdriver.common.by import By
import time
from base.base import Base
from user import bid_flow_xpth


def select(number): #number 为选择项目列表时前面的序号
    select = "//*[@id='routerView']/div/div/div[1]/div[3]/table/tbody/tr["+str(number)+"]/td[6]/div/a/span"
    return select


class Bidflow(Base):#

    usersname_locator = (By.XPATH,bid_flow_xpth.usersname)
    password_locator = (By.XPATH,bid_flow_xpth.password)
    pictrue_locator =(By.XPATH,bid_flow_xpth.pictrue)
    pic_input_locator = (By.XPATH,bid_flow_xpth.pic_input)
    login_button_locator = (By.XPATH,bid_flow_xpth.login_button)
    message_locator = (By.XPATH,bid_flow_xpth.message)
    guarantee_apply_locator = (By.XPATH, bid_flow_xpth.guarantee_apply)
    bid_guarantee_locator = (By.XPATH, bid_flow_xpth.bid_guarantee)
    select_locator = (By.XPATH,select(4))
    apply_guarantee_locator = (By.XPATH, bid_flow_xpth.apply_guarantee)
    financing_institution_locator = (By.XPATH, bid_flow_xpth.financing_institution)
    affirm_locator = (By.XPATH, bid_flow_xpth.affirm)
    consent_locator = (By.XPATH, bid_flow_xpth.consent)
    next_locator = (By.XPATH, bid_flow_xpth.next)
    signatrue_locator = (By.XPATH, bid_flow_xpth.signature)
    deploy_locator = (By.XPATH, bid_flow_xpth.deploy)
    file_locator = (By.XPATH, bid_flow_xpth.file)
    payment_locator = (By.XPATH, bid_flow_xpth.payment)

    #打开登入页面
    def open_login_url(self):
        self.open_jinfu_users()

    #登入用户平台
    def login(self):
        #输入账号
        self.send_keys(self.usersname_locator,"15212345678")
        #输入密码
        self.send_keys(self.password_locator,"ndx111")
        #保存验证码图片
        self.savePictrue(self.pictrue_locator)
        #识别验证码
        yzm = self.get_PicPassword()
        #输入验证码
        self.send_keys(self.pic_input_locator,yzm)
        #点击登入
        self.click(self.login_button_locator)

    def login_plus(self):
        try:
            for i in range(15):
                self.login()
                msg = self.get_message()
                if msg is None:
                    break
        except:
            pass

    def get_message(self):#获取弹窗提示信息

        msg = self.get_text(self.message_locator)
        if msg is not None:
            self.move_mouse(self.login_button_locator)
            time.sleep(3)
        return msg

    #点击保函申请
    def guarantee_apply_click(self):
        self.click(self.guarantee_apply_locator)

    #点击投标保证保函
    def bid_guarantee_click(self):
        self.click(self.bid_guarantee_locator)

    #选择项目
    def project_select_click(self):
        self.click(self.select_locator)#输入项目前面的序号

    #选择金融机构
    def financing_institution_click(self):
        self.click(self.financing_institution_locator)

    #点击确定
    def affirm_click(self):
        self.click(self.affirm_locator)

    #点击申请保函
    def apply_guarantee_click(self):
        self.click(self.apply_guarantee_locator)

    #点击跳转句柄
    def handle_skip(self):
        n = self.drive.window_handles
        self.drive.switch_to.window(n[-1])

    #点击同意本条内容
    def consent_click(self):
        self.click(self.consent_locator)

    #点击下一步
    def next_click(self):
        self.click(self.next_locator)

    #点击签章
    def signatrue_click(self):
        self.click(self.signatrue_locator)

    #点击确认部署
    def deploy_click(self):
        self.click(self.deploy_locator)

    #点击投保申请单
    def file_click(self):
        self.click(self.file_locator)

    #点击线上支付
    def payment_click(self):
        self.click(self.payment_locator)


if __name__ == '__main__':
    base = Base()



