#创建时间  2023-05-29 14:51
#作者  小酒窝
from selenium.webdriver.common.by import By
from base.base import Base
class Login(Base):
    usname = "//input[@placeholder = '请输入账户']"
    password = "//input[@placeholder = '请输入登录密码']"
    pictrue_input = "//input[@placeholder = '请输入验证码']"
    login_button = "//div[@class = 'login-showBtn' and  contains(text(),'登录')]"

    usname_locator = (By.XPATH,usname)
    password_locator = (By.XPATH,password)
    pictrue_input_locator = (By.XPATH,pictrue_input)
    login_button_locator = (By.XPATH,login_button)

    def usname_send_keys(self):
        self.send_keys(self.usname_locator)

    def password_send_keys(self):
        self.send_keys(self.password_locator)

    def pictrue_input_send_keys(self):
        self.send_keys(self.pictrue_input_locator)

    def login_button_click(self):
        self.click(self.login_button_locator)