#创建时间  2023-06-01 17:15
#作者  小酒窝
from base.base import Base
from selenium.webdriver.common.by import By
from xiaoe_testcase.deal_testcase import Deal_testcase
class Home_page(Base):
    deal_testcase = Deal_testcase()
    engineering = "//p[contains(text(),'工程项目')]/../following-sibling::div[contains(text(),'点击进入')]"#工程项目点击进入
    purchase = "//p[contains(text(),'政采项目')]/../following-sibling::div[contains(text(),'点击进入')]"#政采项目点击进入
    projectNumber_input = "//p[contains(text(),'招标项目编号')]/following-sibling::div/input"#点击招标项目编号
    projectName = "//p[contains(text(),'招标项目名称')]/following-sibling::div/input"#点击招标项目名称
    search_project = "//button/span[contains(text(),'查找项目')]"#点击查找项目按钮
    extract_expert = "//button//span[contains(text(),'抽取专家')]"#点击抽取专家按钮
    affirm = "//span[text()='确认']"
    engineering_extract_apply = "//div/p[contains(text(),'工程类抽取申请')]"#点击工程抽取申请
    purchase_extract_apply = "//div/p[contains(text(),'政采类抽取申请')]"#点击政采抽取申请
    number_or_name_input = "//div/input[@placeholder='项目名称或者编号']"#点击项目编号和名称输入框
    search = "//button/span[text()='搜索']"#点击搜索按钮
    in_project = "//div[contains(text(),'')]/../following-sibling::td[3]/div/button/span[contains(text(),'进入项目')]"#点击进入项目

    engineering_locator = (By.XPATH,engineering)
    purchase_locator = (By.XPATH,purchase)
    projectNumber_input_locator = (By.XPATH,projectNumber_input)
    projectName_locator = (By.XPATH,projectName)
    search_project_locator = (By.XPATH,search_project)
    extract_expert_locator = (By.XPATH,extract_expert)
    affirm_locator = (By.XPATH,affirm)
    engineering_extract_apply_locator = (By.XPATH,engineering_extract_apply)
    purchase_extract_apply_locator = (By.XPATH,purchase_extract_apply)
    number_or_name_input_locator = (By.XPATH,number_or_name_input)
    search_locator = (By.XPATH,search)
    in_project_locator = (By.XPATH,in_project)

    def engineering_or_purchase_click(self,projectType):#工程或者政采项目点击进入
        if projectType == "engineering":
            self.click(self.engineering_locator)
        elif projectType == "purchase":
            self.click(self.purchase_locator)
        else:
            print("项目类型错误："+projectType)


    def projectNumber_input_send_keys(self,projectNumber):#输入招标项目编号
        self.send_keys(self.projectNumber_input_locator,projectNumber)

    def projectName_click(self):#点击招标项目名称
        self.click(self.projectName_locator)

    def search_project_click(self):#点击查找项目按钮
        self.click(self.search_project_locator)

    def extract_expert_click(self):#点击抽取专家按钮
        self.click(self.extract_expert_locator)

    def apply_select_click(self,projectType):#工程或者政采抽取申请点击
        if projectType == "engineering":
            self.click(self.engineering_extract_apply_locator)#点击工程抽取申请
        elif projectType == "purchase":
            self.click(self.purchase_extract_apply_locator)#点击政采抽取申请
        else:
            print("项目类型错误："+projectType)

    def engineering_extract_apply_click(self):#点击工程抽取申请
        self.click(self.engineering_extract_apply_locator)

    def purchase_extract_apply_click(self):#点击政采抽取申请
        self.click(self.purchase_extract_apply_locator)

    def number_or_name_input_send_keys(self,projectNumber):#项目编号和名称输入框
        self.send_keys(self.number_or_name_input_locator,projectNumber)

    def search_click(self):#点击搜索按钮
        self.click(self.search_locator)

    def in_project_click(self):#点击进入项目
        self.click(self.in_project_locator)

    def affirm_click(self):#点击确认按钮
        self.click(self.affirm_locator)

