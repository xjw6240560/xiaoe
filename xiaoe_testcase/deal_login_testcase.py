# from xiaoe_data import test_xiaoe_data
# from xiaoeXapth_package.deal_or_bidOpen.login_registerORselect_role import LoginORrole
# import time
# import datetime
# import unittest
#
# import sys
#
#
# class Login_TeatCase(unittest.TestCase):
#
#     def setUp(self):  # 打开交易平台登入页面
#         self.login = LoginORrole
#         self.login.open_deal_url()
#         print("--------------------------------------------" + datetime.datetime.now().strftime(
#             '%Y-%m-%d  %H:%M:%S') + "--------------------------------------------")
#
#     def test_deal_login(self):
#
#         for i in range(len(self.login.username)):
#             for j in range(100):
#                 try:
#                     self.login.username_send_keys(i)
#                     self.login.password_send_keys(i)
#                     self.login.verification_send_keys()
#                     self.login.loginButton_click()
#                     self.login.mouse_susepension()
#                     log = self.login.get_alert_text()
#                     self.login.move_mouse_login_button()
#                     time.sleep(3)
#                     if log is not None:
#                         if log != "图形验证码错误":
#                             print("-------------" + log + "------------")
#                             print("账号：" + test_deal_data.usernameList[i])
#                             print("密码：" + test_deal_data.passwordList[i])
#                             print("###############################################################")
#                             break
#                 except:
#                     break
#
#     def tearDown(self):
#         self.login.close()
#
#
# if __name__ == '__main__':
#     unittest.main()
