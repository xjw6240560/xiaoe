from base.base import Base
from selenium.webdriver.common.by import By
import time
from log.log import Logger
import random
import traceback
from xiaoeXapth_package.deal_or_bidOpen.evaluationBid_entrance import EvaluationBid_entrance


class Expert(Base):
    evaluationBid_entrance = EvaluationBid_entrance()
    logger = Logger()
    username_input = "//input[@placeholder='请输入账号']"  # 账号输入框
    password_input = "//input[@placeholder='请输入密码']"  # 密码输入框
    img = "//input[@placeholder='请输入图形码']/ancestor::div[@class='w-full aui-padded-r-10']/following-sibling::div/img"  # 图片验证码
    img_input = "//input[@placeholder='请输入图形码']"  # 图形验证码输入框
    login_button = "//button/span[contains(text(),'登录')]"  # 登录按钮
    know = "//button//span[contains(text(),'我已知悉')]"  # 协议
    electGroup = "//button//span[contains(text(),'推选组长')]"  # 推选组长
    score01_input = "//div[text()='1']/ancestor::td/following-sibling::td[4]/div/div/div/input"  # 第一个评分点xpath用于判断是否已经评标完成
    result_pass01 = "//div[text()='1']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='通过']"
    group = "//div//span[contains(text(),'当选组长')]/../preceding-sibling::div/../preceding-sibling::p[@class='aui-font-weight-700 aui-000000 aui-padded-t-4']"
    review1 = "//p[contains(text(),'开始评标')]/following-sibling::div/p[1]/button"  # 初步评审
    review2 = "//p[contains(text(),'开始评标')]/following-sibling::div/p[2]/button"  # 技术评审
    review3 = "//p[contains(text(),'开始评标')]/following-sibling::div/p[3]/button"  # 最终评审
    review4 = "//p[contains(text(),'开始评标')]/following-sibling::div/p[4]/button"
    score1 = "//div[text()='1']/ancestor::td/following-sibling::td[4]/div/div/div/input"  # 分值1
    score2 = "//div[text()='2']/ancestor::td/following-sibling::td[4]/div/div/div/input"  # 分值1
    result_1_Pass = "//div[text()='1']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='通过']"
    result_1_NoPass = "//div[text()='1']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='不通过']"
    result_2_Pass = "//div[text()='2']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='通过']"
    result_2_NoPass = "//div[text()='2']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='不通过']"
    enterprise_input = "//input[@placeholder='请选择']"  # 点击企业输入框
    submit_result = "//div[contains(text(),'提交评审结果')]"  # 点击提交审核结果
    submitResult_affirm = "//div[text()='确认']"
    judgeSignature = "//button//span[contains(text(),'确认评标报告')]"
    judgeAffirm = "//button//span[contains(text(),'评委确认')]"

    username_input_locator = (By.XPATH, username_input)
    password_input_locator = (By.XPATH, password_input)
    img_locator = (By.XPATH, img)
    img_input_locator = (By.XPATH, img_input)
    login_button_locator = (By.XPATH, login_button)
    know_locator = (By.XPATH, know)
    electGroup_locator = (By.XPATH, electGroup)
    group_locator = (By.XPATH, group)
    score01_locator = (By.XPATH, score01_input)
    result_pass01_locator = (By.XPATH, result_pass01)
    review1_locator = (By.XPATH, review1)
    review2_locator = (By.XPATH, review2)
    review3_locator = (By.XPATH, review3)
    review4_locator = (By.XPATH, review4)
    score1_locator = (By.XPATH, score1)
    score2_locator = (By.XPATH, score2)
    result_1_Pass_locator = (By.XPATH, result_1_Pass)
    result_1_NoPass_locator = (By.XPATH, result_1_NoPass)
    result_2_Pass_locator = (By.XPATH, result_2_Pass)
    result_2_NoPass_locator = (By.XPATH, result_2_NoPass)
    enterprise_input_locator = (By.XPATH, enterprise_input)
    submit_result_locator = (By.XPATH, submit_result)
    submitResult_affirm_locator = (By.XPATH, submitResult_affirm)
    judgeSignature_locator = (By.XPATH, judgeSignature)
    judgeAffirm_locator = (By.XPATH, judgeAffirm)

    def login(self, username, password, projectNumber):
        self.open_expert_url()
        self.send_keys(self.username_input_locator, username)
        self.send_keys(self.password_input_locator, password)
        for j in range(150):
            try:
                self.savePictrue(self.img_locator)
                pic = self.get_PicPassword()
                self.send_keys(self.img_input_locator, pic)
                self.click(self.login_button_locator)  # 点击登录按钮
                time.sleep(0.2)
                message = self.get_text(self.alert_locator)
                if str(message).find('成功') < 0:
                    self.logger.debugText(projectNumber=projectNumber, errorText=str(message),
                                          bidder=username)  # 记录专家是否登录成功
            except:
                time.sleep(0.5)
                if self.get_nowUrl() == self.expert_projectList_url:
                    self.logger.debugText(projectNumber=projectNumber, errorText='专家登录成功！',
                                          bidder=username)  # 记录专家是否登录成功
                    break

    def protocol_agree(self, username, projectNumber):  # 同意协议
        isAgree = self.select_isAgree(username, projectNumber)
        time.sleep(0.5)
        if isAgree[0] == "disAgree":
            self.click(self.know_locator)
            self.update_isAgree("consent", username, projectNumber)
        elif isAgree[0] == "consent":
            self.logger.debugText(projectNumber=projectNumber, errorText='用户协议已同意！',
                                  bidder=username)  # 记录是否点击用户协议
        else:
            self.logger.debugText(projectNumber=projectNumber, errorText='专家协议类型错误！',
                                  bidder=username)  # 记录是否点击用户协议

    def in_project(self, projectNumber):  # 点击进入项目
        self.handle_skip(-1)
        self.in_project_click(projectNumber=projectNumber)
        time.sleep(0.5)
        message = self.get_text(self.alert_locator)
        if message is not None:
            self.logger.debugText(projectNumber=projectNumber, errorText=str(message))
        if self.is_url(self.expert_projectList_url):  # 判断有没有进入专家平台
            time.sleep(3)
            self.in_project_click(projectNumber=projectNumber)

    def electGroup_click(self):  # 点击推选组长
        self.js_click(self.electGroup_locator)  # 点击推选组长

    def elect_click(self, name):  # 点击推选
        choose = "//p[contains(text(),'" + name + "')]/following-sibling::div/button/span[contains(text(),'推选')]"  # 推选
        choose_locator = (By.XPATH, choose)
        result = self.js_click(choose_locator)  # 点击推选
        return result

    def select_group(self, username, password, name, projectNumber):  # 选择组长
        if len(username) > 0:
            for i in range(len(username)):
                self.login(username=username[i], password=password[i], projectNumber=projectNumber)  # 登录专家端
                self.in_project(projectNumber=projectNumber)  # 点击进入项目
                self.protocol_agree(username=username[i], projectNumber=projectNumber)  # 同意用户协议
                time.sleep(1)
                self.electGroup_click()  # 点击推选组长
                try:
                    time.sleep(0.3)
                    a = random.randint(0, len(username) - 1)  # 随机生成推选评委
                    self.elect_click(name=name[a])  # 点击推选
                except (Exception, BaseException):
                    error = traceback.format_exc()
                    if str(error).find('javascript') > 0:
                        self.logger.debugText(projectNumber=projectNumber, errorText='未找到推选按钮或者评委已经推选！',
                                              bidder=username[i])
                    else:
                        self.logger.debugText(projectNumber=projectNumber, errorText=error,
                                              bidder=username[i])
        else:
            print('没有保存评委:' + str(len(username)))

    def in_project_click(self, projectNumber):
        in_project = "//div[contains(text(),'" + str(
            projectNumber) + "')]/../following-sibling::td[4]/div/button/span[contains(text(),'进入项目')]"
        in_project_locator = (By.XPATH, in_project)
        time.sleep(0.5)
        self.js_click(in_project_locator)

    def get_group(self):  # 获取组长评委
        review = self.get_text(self.group_locator)
        return review

    def alert_getClass(self):  # 获取弹窗类型
        errortext = self.get_attribute_value(locator=self.alert_locator, attribute='class')
        return errortext

    def review_click(self, buttonCount):  # 专家选择评标类型
        time.sleep(0.2)
        if buttonCount == 1:
            try:
                self.click(self.review1_locator)
            except:
                print('评标类型1不存在')
        elif buttonCount == 2:
            try:
                self.click(self.review2_locator)
            except:
                print('评标类型2不存在')
        elif buttonCount == 3:
            try:
                self.click(self.review3_locator)
            except:
                print('评标类型3不存在')
        elif buttonCount == 4:
            try:
                self.click(self.review4_locator)
            except:
                print('评标类型4不存在')
        else:
            print("评标类型输入有误" + str(buttonCount))

    def enterprise_input_click(self):  # 点击选择企业输入框
        self.js_click(self.enterprise_input_locator)
        time.sleep(0.5)

    def choose_enterprise(self, num):  # 选择企业
        js_code = 'document.getElementsByClassName("el-select-dropdown__wrap el-scrollbar__wrap")[0].scrollBy(0, ' + str(
            30) + ')'
        self.drive.execute_script(js_code)
        choose_enterprise = "//div//ul//li[" + str(num) + "]/span"  # 选择企业
        choose_enterprise_locator = (By.XPATH, choose_enterprise)
        time.sleep(0.1)
        self.short_click(choose_enterprise_locator)

    def score_send_keys(self, projectNumber, ratingPointCount=100):  # 输入分值
        count = 0  # 用来统计评分点个数
        global score_locator
        for i in range(1, int(ratingPointCount) + 1):
            score_input = "//div[text()='" + str(i) + "']/ancestor::td/following-sibling::td[4]/div/div/div/input"
            score_locator = (By.XPATH, score_input)
            score = random.randint(20, 40)
            try:  # 用来判断有多少个评分点
                time.sleep(0.5)
                self.short_send_keys(score_locator, score)
                count = count + 1
            except:
                if i == 1:
                    raise Exception("不是分值类型")
                else:
                    self.update_ratingPoint_count(ratingPointCount=count, ratingType='0', projectNumber=projectNumber)
                    break

    def result_NoPass_or_pass_click(self, projectNumber, ratingPointCount=100):  # 选择不通过
        count = 0
        for i in range(1, int(ratingPointCount) + 1):
            result_pass = "//div[text()='" + str(
                i) + "']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='通过']"
            result_Nopass = "//div[text()='" + str(
                i) + "']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='不通过']"
            result_pass_locator = (By.XPATH, result_pass)
            result_Nopass_locator = (By.XPATH, result_Nopass)
            result = random.randint(1, 2)
            time.sleep(0.1)
            try:  # 用来判断有多少个评分点
                if result == 1:
                    self.click(result_Nopass_locator)
                else:
                    self.click(result_pass_locator)
                count = count + 1
            except:
                if i == 1:
                    raise Exception("不是通过式！")
                else:
                    self.update_ratingPoint_count(ratingPointCount=count, ratingType='1', projectNumber=projectNumber)
                    break

    def enterprise_review(self, projectNumber, enterprise_count=1000):  # 企业评审
        count = 0  # 用来累计企业个数
        for j in range(1, int(enterprise_count) + 1):
            result = self.query_projectData(projectNumber)
            ratingPointCount = result[7]
            ratingType = result[8]
            self.enterprise_input_click()
            time.sleep(0.1)
            try:  # 用来判断有多少家企业
                self.choose_enterprise(j)
                count = count + 1
            except:
                self.update_enterprise_count(enterpriseCount=str(count), projectNumber=projectNumber)
                break

            """
            ratingPointCount 如果等于0的话说明没有评标（默认为0）
            """
            if ratingPointCount == '0':
                try:
                    if self.is_interactive(self.score01_locator) is True:  # 判断元素是否可交互
                        self.score_send_keys(projectNumber)
                    else:
                        self.logger.debugText(projectNumber=projectNumber, errorText='分值式元素不可交互!')
                        break
                except:
                    if self.is_interactive(self.result_pass01_locator) is True:
                        self.result_NoPass_or_pass_click(projectNumber)
                    else:
                        self.logger.debugText(projectNumber=projectNumber, errorText='分值式元素不可交互!')
                        break
            else:
                if ratingType == '0':
                    self.score_send_keys(projectNumber=projectNumber, ratingPointCount=ratingPointCount)
                elif ratingType == '1':
                    self.result_NoPass_or_pass_click(projectNumber=projectNumber, ratingPointCount=ratingPointCount)

    def submit_result_click(self):  # 点击提交审核结果
        self.click(self.submit_result_locator)

    def submitResult_affirm_click(self):  # 点击确认
        self.click(self.submitResult_affirm_locator)

    def judgeSignature_click(self):  # 点击评委签章
        self.js_click(self.judgeSignature_locator)

    def examine1(self, num):  # 返回查看的xpath
        signature_examine1 = "//div[text()='" + str(
            num) + "']/ancestor::td/following-sibling::td[4]/div/button/span[contains(text(),'查看')]"
        return signature_examine1

    def examine2(self, num):  # 返回查看的xpath
        signature_examine2 = "//div[text()='" + str(
            num) + "']/ancestor::td/following-sibling::td[3]/div/button/span[contains(text(),'查看')]"
        return signature_examine2

    def signature_examine(self, projectNumber, username, evaluationReportNumber=20):  # 点击评委查看和确认
        global i
        for i in range(1, evaluationReportNumber):
            signature_examine1 = self.examine1(i)
            signature_examine2 = self.examine2(i)
            signature_examine_locator1 = (By.XPATH, signature_examine1)
            signature_examine_locator2 = (By.XPATH, signature_examine2)
            if i == 1:
                time.sleep(0.5)
                self.js_short_click(signature_examine_locator1)
            else:
                time.sleep(0.5)
                try:
                    self.js_short_click(signature_examine_locator2)  # 点击查看
                except :
                    try:
                        self.js_short_click(signature_examine_locator1)  # 点击查看
                    except :
                        self.logger.debugText(projectNumber=projectNumber, errorText='第一个专家确认评标结果完成！！！',
                                              bidder=username)
                        return i
            time.sleep(0.1)
            self.roll_Id("pdfFile-dialog")  # 根据id滑动窗体到底部
            time.sleep(0.5)
            self.click(self.judgeAffirm_locator)  # 评委确认
            message = self.get_text(self.alert_locator)
            if str(message).find('成功') > 0:
                self.logger.debugText(errorText='第' + str(i) + '条报告:' + message)
        else:
            self.logger.debugText(projectNumber=projectNumber, errorText='专家确认评标结果完成！！！',
                                  bidder=username)
