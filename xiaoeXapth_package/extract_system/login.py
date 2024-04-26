# 创建时间  2023-05-29 14:51
# 作者  小酒窝
from selenium.webdriver.common.by import By
from base.base import Base
import time


class Login(Base):
    base = Base()
    username = "//input[@placeholder = '请输入账户']"  # 登录账号
    password = "//input[@placeholder = '请输入登录密码']"  # 登录密码
    picture_input = "//input[@placeholder = '请输入验证码']"  # 图片验证码输入框
    picture_img = "//div[@class = 'verificationCode aui-padded-l-10']/img"  # 图片验证码
    login_button = "//div[@class = 'login-showBtn' and  contains(text(),'登录')]"  # 登录按钮

    username_locator = (By.XPATH, username)
    password_locator = (By.XPATH, password)
    picture_input_locator = (By.XPATH, picture_input)
    picture_img_locator = (By.XPATH, picture_img)
    login_button_locator = (By.XPATH, login_button)

    def username_send_keys(self, areaNo):  # 登录账号
        if areaNo in (0, 1, 2, 3):
            self.send_keys(self.username_locator, self.extract_username[areaNo])
        else:
            self.logger.debugText(errorText='平台编号错误（0：小额，1：淮安，2：三明）：' + str(areaNo))

    def password_send_keys(self):  # 登录密码
        self.send_keys(self.password_locator, self.extract_password)

    def picture_input_send_keys(self):  # 图片验证码输入框
        picCode = self.return_picture(self.picture_img_locator)
        self.send_keys(self.picture_input_locator, picCode)

    def login_button_click(self):  # 登录按钮
        self.click(self.login_button_locator)

    def login(self, areaNo):  # 登录
        self.username_send_keys(areaNo)  # 输入账号
        self.password_send_keys()  # 输入密码
        while True:
            self.picture_input_send_keys()  # 输入图片验证码
            self.login_button_click()  # 点击登录
            time.sleep(0.5)
            if self.base.get_nowUrl() != self.base.extract_login_url:
                break
            else:
                continue
# if __name__ == '__main__':
#     login = Login()
#     login.test_login()
