from xiaoe_data import test_xiaoe_data
from xiaoe_test_method.deal_login_method import LoginTest
import time
import datetime
import unittest

import sys


class Login_TeatCase(unittest.TestCase):

    def setUp(self):  # 打开交易平台登入页面
        self.login = LoginTest()
        self.login.open_deal_url()
        print("--------------------------------------------" + datetime.datetime.now().strftime(
            '%Y-%m-%d  %H:%M:%S') + "--------------------------------------------")

    def test_deal_login(self):
        for i in range(len(self.login.username)):
            for j in range(100):
                self.login.username_send_keys(i)
                self.login.password_send_keys(i)
                self.login.verification_send_keys()
                self.login.loginButton_click()
                self.login.mouse_susepension()
                log = self.login.get_alert_text()
                self.login.move_mouse_login_button()
                time.sleep(3)
                if log is not None:
                    if log != "图形验证码错误":
                        break

    def tearDown(self):
        self.login.close()


if __name__ == '__main__':
    unittest.main()
