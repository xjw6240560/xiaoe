from xiaoe_test_method.deal_login_method import Login
from xiaoe_data import test_deal_data
import time
import datetime
import unittest

import sys
class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a',encoding='utf-8')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger(stream=sys.stdout)

class Login_TeatCase(unittest.TestCase):

    def setUp(self):#打开交易平台登入页面
        self.login = Login()
        self.login.open_deal_url()
        print("--------------------------------------------"+datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')+"--------------------------------------------")

    def test_deal_login(self):

        for i in range(len(test_deal_data.usernameList)):
            for j in range(100):
                try:
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
                            print("-------------"+log+"------------")
                            print("账号：" + test_deal_data.usernameList[i])
                            print("密码：" + test_deal_data.passwordList[i])
                            print("###############################################################")
                            break
                except:
                    break




    def tearDown(self):
        self.login.close()

if __name__ == '__main__':
    unittest.main()

