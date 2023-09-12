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
    """
    抽取专家
    """
    def test_extract_expert(self):#抽取专家
        nowtimeday = self.base.get_date_day()#获取当前日期
        beforetime = self.base.query_now_date()#获取数据库时间
        if int(nowtimeday) > int(beforetime[0]) :
            self.base.update_now_date(nowtimeday)#更新最新的日期
        self.login.login()
        self.base.handle_skip(0)
        self.home_page.engineering_or_purchase_click(self.projectType_sql)
        self.home_page.projectNumber_input_send_keys(self.deal_testcase.projectNumber)
        self.home_page.search_project_click()#点击查找项目
        try:
            self.home_page.extract_expert_click()#点击抽取专家按钮
            self.home_page.affirm_click()#点击确定
        except:
            self.home_page.apply_select_click(self.projectType_sql)#选择抽取申请
            self.home_page.number_or_name_input_send_keys(self.deal_testcase.projectNumber)#输入项目编号
            self.home_page.search_click()#点击搜索
            self.home_page.in_project_click()#点击进入项目
        self.expert_extract.tender_linkMan_send_keys()#输入招标联系人
        self.expert_extract.link_number_send_keys()#输入联系电话
        self.expert_extract.predict_time_click()#点击选择时间
        self.expert_extract.onehour_click()#点击选择一个小时
        self.expert_extract.add_extract_condition_click()#点击抽取评委
        self.expert_extract.expert_classify_click()#点击专家分类
        self.expert_extract.expertsA_click()#点击专家测试库A
        self.expert_extract.expertsB_click()#点击专家测试库B
        self.expert_extract.expertsC_click()#点击专家测试库C
        self.expert_extract.expert_classify_click()#点击专家分类
        self.expert_extract.expert_send_keys('3')#输入专家数量
        self.expert_extract.add_affirm_click()#点击确认
        nowtime = self.base.query_now_date()
        for i in range(int(nowtime[1]),18):
            self.expert_extract.evaluation_time_send_keys(i)#输入时间
            result = self.expert_extract.is_room_occupy(i)#判断评标室是否被占用
            if result is not None:
                if result == "break":
                    self.base.update_now_date(nowdate=nowtimeday,hour= i )
                    break
                else:
                    continue
        self.expert_extract.save_judge_username_password(self.deal_testcase.projectNumber)
    """
    保存专家账号
    """
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


