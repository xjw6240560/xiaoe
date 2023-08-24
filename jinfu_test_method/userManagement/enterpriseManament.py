from background import enterpriseManagement
from selenium.webdriver.common.by import By

from background import directory_Method
from base.base import Base


class EnterpriseManagement(Base):
    userManagement_locator = (By.XPATH, directory_Method.userManagement)
    enterpriseManagement_locator = (By.XPATH, enterpriseManagement.enterpriseManagement)
    examine_locator = (By.XPATH, enterpriseManagement.examine)
    backtrack_locator = (By.XPATH, enterpriseManagement.backtrack)
    certification_locator = (By.XPATH, enterpriseManagement.certification)

    #点击用户管理
    def userManagement_click(self):
        self.click(self.userManagement_locator)

    #点击企业管理
    def enterpriseManagement_click(self):
        self.click(self.enterpriseManagement_locator)

    #点击查看
    def examine_click(self):
        self.click(self.examine_locator)

    #点击返回
    def backtrack_click(self):
        self.click(self.backtrack_locator)

    #点击资质
    def certification_click(self):
        self.click(self.certification_locator)

if __name__ == '__main__':
    Base = Base()