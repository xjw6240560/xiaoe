# 创建时间  2023-06-01 18:35
# 作者  小酒窝
from base.base import Base
import re
import time
from log.log import Logger
from base.mysql import Mysql
from selenium.webdriver.common.by import By
from xiaoe_testcase.deal_testcase import Deal_testcase


class Expert_extract(Base):
    deal_testcase = Deal_testcase()
    logger = Logger()
    mysql = Mysql()
    tender_linkMan = "//label[contains(text(),'招标联系人')]/following-sibling::div/div/input"  # 输入招标联系人
    link_number = "//label[contains(text(),'联系电话')]/following-sibling::div/div/input"  # 输入联系电话
    evaluation_time = "//label[contains(text(),'评标时间')]/following-sibling::div/div/input"
    predict_time = "//label[contains(text(),'预计评标时长（小时）')]/following-sibling::div/div/div/input"  # 点击预计时长
    onehour = "//ul/li/span[text() = '1']"  # 点击一个小时
    evaluation_room_input = "//label[contains(text(),'评标室')]/following-sibling::div/div/div/input"  # 点击评标室选择按钮
    evaluation_room1 = "//ul/li/span[contains(text(),'评标室1')]"  # 点击评标室1
    evaluation_room2 = "//ul/li/span[contains(text(),'评标室2')]"  # 点击评标室2
    add_extract_condition = "//div/button/span[contains(text(),'添加抽取条件')]"  # 点击添加抽取条件
    extract_result = "//div//button[3]//span[text()='专家抽取名单']"  # 点击工程专家抽取名单
    expert_classify = "//label[contains(text(),'专家分类')]/following-sibling::div/div/div[2]/span/span/i"  # 点击专家分类
    expertsA = "//li/span[contains(text(),'桥梁公路类别')]"  # 桥梁公路类别
    expertsB = "//li/span[contains(text(),'政采类别专家')]"  # 政采类别专家
    expertsC = "//li/span[contains(text(),'工程类专家')]"  # 工程类专家
    expert = "//label[contains(text(),'抽取人数')]/following-sibling::div/div/input[@placeholder='请输入整数']"  # 输入抽取专家数量
    add_affirm = "//button/span[contains(text(),'取消')]/../following-sibling::button[1]/span[contains(text(),'确认')]"  # 新增抽取条件确认
    edit = "//button/span[text() = '编辑']"  # 点击编辑
    delete = "//button/span[text() = '删除']"  # 点击删除
    extract_expert = "//button/span[contains(text(),'抽取专家')]"  # 点击抽取专家按钮
    errorTips1 = "//div[contains(text(),'提示')]/./following-sibling::div/div/div/p[1]"  # 报错提示
    errorTips2 = "//div[contains(text(),'提示')]/./following-sibling::div/div/div/p[1]"  # 报错提示
    error_confirm = "//div[contains(text(),'提示')]/./following-sibling::div/div/button/span[contains(text(),'确认')]"
    tender_linkMan_locator = (By.XPATH, tender_linkMan)
    link_number_locator = (By.XPATH, link_number)
    predict_time_locator = (By.XPATH, predict_time)
    onehour_locator = (By.XPATH, onehour)
    evaluation_time_locator = (By.XPATH, evaluation_time)
    evaluation_room_input_locator = (By.XPATH, evaluation_room_input)
    evaluation_room1_locator = (By.XPATH, evaluation_room1)
    evaluation_room2_locator = (By.XPATH, evaluation_room2)
    add_extract_condition_locator = (By.XPATH, add_extract_condition)
    extract_result_locator = (By.XPATH, extract_result)
    expert_classify_locator = (By.XPATH, expert_classify)
    expertsA_locator = (By.XPATH, expertsA)
    expertsB_locator = (By.XPATH, expertsB)
    expertsC_locator = (By.XPATH, expertsC)
    error_confirm_locator = (By.XPATH, error_confirm)
    expert_locator = (By.XPATH, expert)
    add_affirm_locator = (By.XPATH, add_affirm)
    edit_locator = (By.XPATH, edit)
    delete_locator = (By.XPATH, delete)
    extract_expert_locator = (By.XPATH, extract_expert)
    errorTips_locator1 = (By.XPATH, errorTips1)
    errorTips_locator2 = (By.XPATH, errorTips2)

    def tender_linkMan_send_keys(self):  # 输入招标联系人
        self.send_keys(self.tender_linkMan_locator, "谢先生")

    def link_number_send_keys(self):  # 输入联系电话
        self.send_keys(self.link_number_locator, "15212345678")

    def evaluation_time_send_keys(self, hours):  # 输入评标时长
        nowData = self.get_nowData(hours)  # 获取当前日期，年月日
        self.send_keys(self.evaluation_time_locator, nowData)

    def predict_time_click(self):  # 点击预计时长
        self.click(self.predict_time_locator)

    def onehour_click(self):  # 点击一个小时
        self.click(self.onehour_locator)

    def evaluation_room_input_click(self):  # 点击评标室选择按钮
        self.click(self.evaluation_room_input_locator)

    def evaluation_room1_click(self):  # 点击评标室1
        self.click(self.evaluation_room1_locator)

    def evaluation_room2_click(self):  # 点击评标室2
        self.click(self.evaluation_room2_locator)

    def add_extract_condition_click(self):  # 点击添加抽取条件
        self.click(self.add_extract_condition_locator)

    def extract_result_click(self):  # 点击抽取结果
        self.click(self.extract_result_locator)  # 点击工程抽取结果

    def save_judge_username_password(self, projectNumber):  # 保存评委账号和密码
        count = 0  # 统计专家个数
        for i in range(1, 100):
            expert_name = f"//button//span[text() = '专家抽取名单']/ancestor::div/following-sibling::div[2]/div/div/div/div//div[text() = '{i}']/ancestor::td/following-sibling::td[1]"  # 获取专家姓名
            expert_username = f"//button//span[text() = '专家抽取名单']/ancestor::div/following-sibling::div[2]/div/div/div/div//div[text() = '{i}']/ancestor::td/following-sibling::td[2]"  # 获取专家账号
            expert_status = f"//button//span[text() = '专家抽取名单']/ancestor::div/following-sibling::div[2]/div/div/div/div//div[text() = '{i}']/ancestor::td/following-sibling::td[7]"  # 获取专家状态
            password = "ndx111"

            expert_name_locator = (By.XPATH, expert_name)
            expert_username_locator = (By.XPATH, expert_username)
            expert_status_locator = (By.XPATH, expert_status)
            name = self.get_text(expert_name_locator)
            if name is None:
                break
            username = self.get_text(expert_username_locator)
            status = self.get_text(expert_status_locator)

            if status == "正常参加":
                try:
                    self.mysql.insert_expertData(projectNumber=projectNumber, username=username, password=password,
                                                 judgeName=name)
                    count = count + 1
                except:
                    print("------------评委个数为" + str(count) + "------------")
            elif status == "取消评标":
                print("评委：" + str(name) + "不符合要求!")
            else:
                print("评委状态异常：" + str(name))
                break

    def expert_classify_click(self):  # 点击专家分类
        self.click(self.expert_classify_locator)

    def expertsA_click(self):  # 点击专家库A
        self.click(self.expertsA_locator)

    def expertsB_click(self):  # 点击专家库B
        self.click(self.expertsB_locator)

    def expertsC_click(self):  # 点击专家库C
        self.click(self.expertsC_locator)

    def error_confirm_click(self):  # 报错点击确认
        self.click(self.error_confirm_locator)

    def expert_send_keys(self, number):  # 输入抽取专家数量
        self.send_keys(self.expert_locator, number)

    def add_affirm_click(self):  # 新增抽取条件确认
        self.click(self.add_affirm_locator)

    def edit_click(self):  # 点击编辑
        self.click(self.edit_locator)

    def delete_click(self):  # 点击删除
        self.click(self.delete_locator)

    def extract_expert_click(self):  # 点击抽取专家按钮
        self.click(self.extract_expert_locator)

    def errorTips1_get_text(self):  # 获取错误文本
        return self.get_text(self.errorTips_locator1)

    def errorTips2_get_text(self):  # 获取错误文本
        return self.get_text(self.errorTips_locator2)

    def is_room_occupy(self, hours):  # 判断评标室是否被占用
        nowData = self.get_nowData(hours)  # 获取当前日期，年月日
        self.evaluation_room_input_click()  # 点击选择评标室
        self.evaluation_room1_click()  # 点击选择评标室1
        self.extract_expert_click()  # 点击抽取专家按钮
        try:
            message = self.errorTips1_get_text()  # 获取错误信息
            room1 = re.compile('评标室[1,2]').findall(message)
            if room1[0] == "评标室1":
                self.error_confirm_click()  # 点击确认
                self.evaluation_room_input_click()  # 点击选择评标室
                self.evaluation_room2_click()  # 点击选择评标室2
                self.extract_expert_click()  # 点击抽取专家按钮
                time.sleep(0.5)
                try:
                    message = self.errorTips1_get_text()
                    room2 = re.compile('评标室[1,2]').findall(message)
                    self.error_confirm_click()  # 点击确认
                    return room2
                except:
                    self.logger.debugText(projectNumber=self.deal_testcase.projectNumber,
                                          errorText='专家抽取完成,评标室2:' + str(nowData))
                    return "break"
        except:
            self.logger.debugText(projectNumber=self.deal_testcase.projectNumber,
                                  errorText='专家抽取完成,评标室1:' + str(nowData))
            return "break"
