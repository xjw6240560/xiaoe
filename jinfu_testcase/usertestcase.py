import time
import unittest
from jinfu_test_method.userTestMethod.bid_flow import Bidflow
class TestCasebaohanshenqing(unittest.TestCase):
    def setUp(self):
        self.bid = Bidflow()
        self.bid.open_login_url()

    def test_bid_flow(self):

        #登入进入用户端
        self.bid.login_plus()

        #跳转句柄
        self.bid.handle_skip()

        #选择保函申请
        self.bid.guarantee_apply_click()
        
        time.sleep(1)

        # self.bid.drive.close()

        #点击投标保证保函
        self.bid.bid_guarantee_click()
        
        time.sleep(2)

        #选择项目
        self.bid.project_select_click()
        
        time.sleep(5)

        # #点击申请保函
        # self.bid.apply_guarantee_click()
        # 
        # time.sleep(1)

        # #选择金融机构
        # self.bid.financing_institution_click()
        # 
        # time.sleep(1)
        #
        # #点击确定
        # self.bid.affirm_click()
        # 
        # time.sleep(1)
        #
        # #跳转句柄
        self.bid.handle_skip()
        # 
        # time.sleep(7)
        #
        # #点击同意本条内容
        # self.bid.consent_click()
        # 
        # time.sleep(2)
        #
        # #关闭同意本条内容
        # self.bid.consent_click()
        # 
        # time.sleep(1)
        #
        # #点击下一步
        # self.bid.next_click()
        
        # time.sleep(1)
        #
        # #点击平台签章
        # self.bid.signatrue_click()
        
        # time.sleep(1)
        #
        # #点击签章按钮
        # self.bid.deploy_click()
        # 
        # time.sleep(2)
        #
        # #点击投保单
        # self.bid.file_click()
        
        # time.sleep(1)
        #
        # #点击线上支付
        # self.bid.payment_click()
        
        # time.sleep(1)

    def tearDown(self):
        self.bid.close()


if __name__ == '__main__':
    unittest.main()
    # tests = [TestCasebaohanshenqing("test01_bid_login"),TestCasebaohanshenqing("test02_bid_flow")]
    # suite = unittest.TestSuite()
    # suite.addTest(tests)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # unittest.main()
