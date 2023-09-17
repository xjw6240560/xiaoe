from selenium.webdriver.common.by import By
from base.base import Base
from xiaoe_data.test_xiaoe_data import Test_xiaoe_data
import time
from xiaoeXapth_package.deal_or_bidOpen.login_registerORselect_role import LoginORrole
from selenium.webdriver.common.action_chains import ActionChains


class LoginTest(Base):
    loginORrole = LoginORrole()
    test_xiaoe_data = Test_xiaoe_data()
    """
    创建测试数据
    分别对应长度正常、小于、大于
    """

    def username_send_keys(self, i):
        self.send_keys(self.loginORrole.username_locator, self.test_xiaoe_data.username[int(i)])

    def password_send_keys(self, i):
        self.send_keys(self.loginORrole.password_locator, self.test_xiaoe_data.password[int(i)])

    def verification_send_keys(self):  # 输入验证码
        self.savePictrue(self.loginORrole.picture_locator)  # 保存验证码图片
        verification = self.get_PicPassword()  # 识别图片验证码
        self.send_keys(self.loginORrole.pictrue_input_locator, verification)  # 输入验证码

    def loginButton_click(self):
        self.click(self.loginORrole.login_btn_locator)

    def mouse_susepension(self):  # 鼠标悬浮在弹窗上
        self.move_mouse(self.loginORrole.alert_locator)

    def get_alert_text(self):  # 获取弹窗文本
        msg = self.get_text(self.loginORrole.alert_locator)
        time.sleep(1)
        return msg

    def move_mouse_login_button(self):
        self.move_mouse(self.loginORrole.login_btn_locator)


if __name__ == '__main__':
    base = Base()
