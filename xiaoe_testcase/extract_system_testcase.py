#创建时间  2023-06-01 15:00
#作者  小酒窝
import unittest
import time
from base.base import Base
from xiaoeXapth_package.extract_system.login import Login
from xiaoe_testcase.deal_testcase import Deal_testcase
from xiaoeXapth_package.extract_system.expert_extract import Expert_extract
from xiaoeXapth_package.extract_system.home_page import Home_page
class Extract_system(unittest.TestCase):

    def setUp(self):
        self.base = Base()
        self.login = Login()
        self.home_page = Home_page()
        self.expert_extract = Expert_extract()
        self.deal_testcase = Deal_testcase()
        self.extract_system_login = Login()
        #查询项目信息
        try:
            self.result1 = self.base.query_projectData(self.deal_testcase.projectNumber)
            self.projectType_sql = self.result1[0]
            self.tenderOrganizationType_sql = self.result1[1]
            self.evaluationBidWay = self.result1[2]
            self.judgesCount =self.result1[3]
            self.tenderWay_sql = self.result1[4]
            self.applyNumber = self.result1[5]
        except:
            print("项目信息查询失败")
        self.base.open_extract_system_url()#打开专家抽取系统

    def test_extract_expert(self):#抽取专家
        self.login.login()
        self.base.handle_skip(0)
        self.home_page.engineering_or_purchase_click(self.deal_testcase.projectType_sql)
        self.home_page.number_or_name_input_send_keys(self.deal_testcase.projectNumber)
        self.home_page.search_project_click()#点击查找项目
        self.home_page.in_project_click()#点击进入项目
        self.expert_extract.tender_linkMan_send_keys()#输入招标联系人
        self.expert_extract.link_number_send_keys()#输入联系电话
        # self.expert_extract.
    def test_save_expert(self):#保存专家账号
        self.login.login()
        self.base.handle_skip(0)
        self.home_page.apply_select_click(self.projectType_sql)
        self.home_page.number_or_name_input_send_keys(self.deal_testcase.projectNumber)#输入项目名称
        self.home_page.search_click()#点击搜索
        time.sleep(0.3)
        self.home_page.in_project_click()#点击进入项目
        self.expert_extract.extract_result_click()#点击抽取结果
        self.expert_extract.save_judge_username_password(self.deal_testcase.projectNumber)


    def tearDown(self):
        self.base.close()

if __name__ == '__main__':
    unittest.main()


