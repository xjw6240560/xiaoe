from background import financingInstitution
from selenium.webdriver.common.by import By

from background import directory_Method
from base.base import Base


class FinancingInstitution(Base):
    #编辑定位器和页面属性
    click_userManagement_locator = (By.XPATH, directory_Method.userManagement)
    financingInstitution_locator = (By.XPATH, financingInstitution.financingInstitution)
    examine_locator = (By.XPATH, financingInstitution.examine)
    backtrack_locator = (By.XPATH, financingInstitution.backtrack)
    compile_locator = (By.XPATH, financingInstitution.compile)
    affirm_locator = (By.XPATH, financingInstitution.affirm)

    #   """封装操作"""
    #点击用户管理
    def userManagement_click(self):
        self.click(self.click_userManagement_locator)

    #点击金融机构
    def financingInstitution_click(self):
        self.click(self.financingInstitution_locator)

    #点击查看
    def examine_click(self):
        self.click(self.examine_locator)

    #点击返回
    def backtrack_click(self):
        self.click(self.backtrack_locator)

    #点击编辑
    def compile_click(self):
        self.click(self.compile_locator)

    #点击确认
    def affirm_click(self):
        self.click(self.affirm_locator)


    if __name__ == '__main__':
        Base = Base()
        # Base.open_houtaiurl()
