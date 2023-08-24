from background import accountManagement
from selenium.webdriver.common.by import By

from background import directory_Method
from base.base import Base


class AccountManagement(Base):
    accountManagement_locator = (By.XPATH, accountManagement.accountManagement)
    accountManagementInputBox_locator = (By.XPATH, accountManagement.accountInputBox)
    seatch_locator = (By.XPATH, accountManagement.search)
    mobile_locator = (By.XPATH, accountManagement.mobile)
    examine_locator = (By.XPATH, accountManagement.examine)

    def userManagement_click(self):#点击用户管理
        self.click(By.XPATH, directory_Method.userManagement)

    def accountManagement_click(self):#点击账户管理
        self.click(accountManagement.accountManagement)

    def accountInput_send_keys(self):#输入账户名
        self.send_keys(By.XPATH, accountManagement.accountInputBox, "152")

    def search_click(self):#点击搜索
        self.click(By.XPATH, accountManagement.search)

    def accountInputBox_clear(self):#清空账户输入框
        self.clear(By.XPATH, accountManagement.accountInputBox)

    def mobileInput_send_keys(self):#输入手机号
        self.send_keys(By.XPATH, accountManagement.mobile, "15212345678")

    def examine_click(self):#查看
        self.clear(By.XPATH, accountManagement.examine)
        self.drive.quit()
