import unittest
from jinfu_test_method.userManagement.financingInstitution import FinancingInstitution
from jinfu_test_method.userManagement.enterpriseManament import EnterpriseManagement
from jinfu_test_method.userManagement.enterpriseCertification import EnterpriseCertification
import time
class BackgroundUserManagementTestCase(unittest.TestCase):
    def setUp(self):
        self.financingInstitution = FinancingInstitution()
        self.enterpriseManagement = EnterpriseManagement()
        self.enterpriseCertification = EnterpriseCertification

        #打开后台首页
        self.financingInstitution.open_backgroundUrl()

        #点击用户管理
        self.financingInstitution.userManagement_click()
        time.sleep(1)
    #金融机构测试
    def testFinancingInstitution(self):

        #点击金融机构
        self.financingInstitution.financingInstitution_click()
        
        time.sleep(1)

        #点击查看
        self.financingInstitution.examine_click()
        
        time.sleep(1)

        #点击返回
        self.financingInstitution.backtrack_click()
        
        time.sleep(1)

        #点击编辑
        self.financingInstitution.compile_click()
        
        time.sleep(1)

        #点击确认
        self.financingInstitution.affirm_click()
        
        time.sleep(1)

    #企业管理测试
    def testEnterpriseManagement(self):

        #点击企业管理
        self.enterpriseManagement.enterpriseManagement_click()
        time.sleep(1)

        #点击查看
        self.enterpriseManagement.examine_click()
        time.sleep(1)

        #点击返回
        self.enterpriseManagement.backtrack_click()
        time.sleep(1)

        #点击资质
        self.enterpriseManagement.certification_click()
        time.sleep(1)

    #企业资质测试
    def testEnterpriseCertification(self):

        #点击企业资质
        self.enterpriseCertification.enterpriseCertification_click()
        
        time.sleep(1)

        #点击新增
        self.enterpriseCertification.append_click()
        time.sleep(1)

        #点击企业名称
        self.enterpriseCertification.enterpriseName_click()
        
        time.sleep(1)

        #选择企业信息
        self.enterpriseCertification.enterpriseMessage_click()
        
        time.sleep(1)

        #输入证书名称
        self.enterpriseCertification.certificateName_send_keys()
        
        time.sleep(1)

        #输入证书编号
        self.enterpriseCertification.certificateNumber_send_keys()
        
        time.sleep(1)

        #点击资质等级
        self.enterpriseCertification.certificationClass_click()
        
        time.sleep(1)

        #选择证书
        self.enterpriseCertification.certificateSelect_locator()
        
        time.sleep(1)

        #点击证书编号
        self.enterpriseCertification.certificateNumber_click()
        
        time.sleep(1)

        #选择有效期
        self.enterpriseCertification.validity_click()
        
        time.sleep(1)

        #选择图片
        self.enterpriseCertification.picture_send_keys()
        
        time.sleep(1)

        #点击确定
        self.enterpriseCertification.affirm_click()
        
        time.sleep(1)

    #
    def tearDown(self):
        self.financingInstitution.close()

if __name__ == '__main__':
        unittest.main()