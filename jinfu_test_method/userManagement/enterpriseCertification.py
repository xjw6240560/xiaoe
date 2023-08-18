from background import enterpriseCertification
from selenium.webdriver.common.by import By

from background import directory_Method
from base.base import Base


class EnterpriseCertification(Base):
    userManagement_locator = (By.XPATH, directory_Method.userManagement)
    enterpriseCertification_locator = (By.XPATH, enterpriseCertification.enterpriseCertification)
    append_locator = (By.XPATH, enterpriseCertification.append)
    enterpriseName_locator = (By.XPATH, enterpriseCertification.enterpriseName)
    enterpriseMessage_locator = (By.XPATH, enterpriseCertification.enterpriseMessage)
    certificateName_locator = (By.XPATH, enterpriseCertification.certificateName)
    certificateNumber_locator = (By.XPATH, enterpriseCertification.certificateNumber)
    certificationClass_locator = (By.XPATH, enterpriseCertification.certificationClass)
    certificateSelect_locator = (By.XPATH, enterpriseCertification.certificateSelect)
    validity_locator = (By.XPATH, enterpriseCertification.validity)
    picture_locator = (By.XPATH, enterpriseCertification.picture)
    affirm_locator = (By.XPATH, enterpriseCertification.affirm)


    #点击用户管理
    def userManagement_click(self):
        self.click(self.userManagement_locator)

    #点击企业资质
    def enterpriseCertification_click(self):
        self.click(self.enterpriseCertification_locator)

    #点击新增
    def append_click(self):
        self.click(self.append_locator)

    #点击企业名称
    def enterpriseName_click(self):
        self.click(self.enterpriseName_locator)

    #选择企业名称
    def enterpriseMessage_click(self):
        self.click(self.enterpriseMessage_locator)

    #输入证书名称
    def certificateName_send_keys(self):
        self.send_keys(self.certificateName_locator,"建筑工程证书")

    #输入证书编号
    def certificateNumber_send_keys(self):
        self.send_keys(self.certificateNumber_locator,"HIU2037946")

    #点击证书编号
    def certificateNumber_click(self):
        self.click(self.certificateNumber_locator)

    #点击资质等级
    def certificationClass_click(self):
        self.click(self.certificationClass_locator)

    #选择证书
    def certificateName_click(self):
        self.click(self.certificateName_locator)

    #选择有效期
    def validity_click(self):
        self.click(self.validity_locator)

    #选择图片
    def picture_send_keys(self):
        self.send_keys(self.picture_locator, enterpriseCertification.picture_position)

    #点击确定
    def affirm_click(self):
        self.click(self.affirm_locator)

if __name__ == '__main__':
    Base = Base()