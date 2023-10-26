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
    number = "//thead/tr/th/div[contains(text(),'序号')]"  # 登录之后的列表序号，用于断言是否登陆成功
    know = "//p[contains(text(),'温馨提示')]/following-sibling::div/button//span[contains(text(),'我已知悉')]"  # 协议
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
    number_locator = (By.XPATH, number)
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
            save_pic_result = self.savePictrue(self.img_locator)
            if save_pic_result is None:
                pic = self.get_PicPassword()
                self.send_keys(self.img_input_locator, pic)
                self.click(self.login_button_locator)  # 点击登录按钮
                time.sleep(0.2)
                message = self.get_text(self.alert_locator)
                # if str(message).find('成功') < 0:
                #     self.logger.debugText(projectNumber=projectNumber, errorText=str(message),
                #                           bidder=username)  # 记录专家是否登录成功
                number_result = self.find_element(self.number_locator, 2)  # 登录之后的列表序号，用于判断是否登陆成功
                if number_result is not False:
                    self.logger.debugText(projectNumber=projectNumber, bidder=username, errorText='专家登录成功！')
                    break
                else:
                    self.logger.debugText(projectNumber=projectNumber, bidder=username, errorText=message)
                    # break
            elif save_pic_result is False:
                self.logger.debugText(projectNumber=projectNumber, bidder=username, errorText='未找到图片二维码！！！')

    def protocol_agree(self, username, projectNumber):  # 同意协议
        isAgree = self.select_isAgree(username, projectNumber)
        if isAgree[0] == "disAgree":
            self.click(self.know_locator)
        elif isAgree[0] == "consent":
            self.logger.debugText(projectNumber=projectNumber, errorText='用户协议已同意！',
                                  bidder=username)  # 记录是否点击用户协议
        else:
            self.logger.debugText(projectNumber=projectNumber, errorText='专家协议类型错误！' + str(isAgree),
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
        return self.click(self.electGroup_locator)  # 点击推选组长

    def elect_click(self, name):  # 点击推选
        choose = "//p[contains(text(),'" + name + "')]/following-sibling::div/button/span[contains(text(),'推选')]"  # 推选
        choose_locator = (By.XPATH, choose)
        result = self.click(choose_locator)  # 点击推选
        return result

    def select_group(self, username, password, name, projectNumber):  # 选择组长
        if len(username) > 0:
            for i in range(len(username)):
                self.login(username=username[i], password=password[i], projectNumber=projectNumber)  # 登录专家端
                self.in_project(projectNumber=projectNumber)  # 点击进入项目
                self.protocol_agree(username=username[i], projectNumber=projectNumber)  # 同意用户协议
                electGroup_result = self.electGroup_click()  # 点击推选组长
                if electGroup_result is None:
                    self.update_isAgree("consent", username[i], projectNumber)  # 更新用户协议数据库
                time.sleep(0.3)
                a = random.randint(0, len(username) - 1)  # 随机生成推选评委
                result = self.elect_click(name=name[a])  # 点击推选
                if result is False:
                    self.logger.debugText(projectNumber=projectNumber, errorText='未找到推选按钮或者评委已经推选！',
                                          bidder=username[i])
                elif result is None:
                    self.logger.debugText(projectNumber=projectNumber, errorText='评委推选成功！',
                                          bidder=username[i])
                else:
                    self.logger.debugText(projectNumber=projectNumber, errorText=result,
                                          bidder=username[i])
        else:
            print('没有保存评委:' + str(len(username)))

    def in_project_click(self, projectNumber):
        in_project = "//div[contains(text(),'" + str(
            projectNumber) + "')]/../following-sibling::td[4]/div/button/span[contains(text(),'进入项目')]"
        in_project_locator = (By.XPATH, in_project)
        time.sleep(0.5)
        self.short_click(in_project_locator)

    def get_group(self):  # 获取组长评委
        review = self.get_text(self.group_locator)
        return review

    def alert_getClass(self):  # 获取弹窗类型
        errortext = self.get_attribute_value(locator=self.alert_locator, attribute='class')
        return errortext

    def review_click(self, buttonCount):  # 专家选择评标类型
        time.sleep(0.2)
        if buttonCount == 1:
            self.click(self.review1_locator)
        elif buttonCount == 2:
            self.click(self.review2_locator)
        elif buttonCount == 3:
            self.click(self.review3_locator)
        elif buttonCount == 4:
            self.click(self.review4_locator)
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
        return self.js_short_click(choose_enterprise_locator)

    def score_send_keys(self, projectNumber):  # 输入分值
        # noinspection PyGlobalUndefined
        global score_locator, score
        for i in range(1, 100):
            score_input = "//div[text()='" + str(i) + "']/ancestor::td/following-sibling::td[4]/div/div/div/input"
            score_num = "//table/tbody/tr[" + str(i) + "]/td[3]/div[@class='cell']"
            score_locator = (By.XPATH, score_input)
            score_num_locator = (By.XPATH, score_num)
            max_score = self.get_text(locator=score_num_locator, position=0)  # 获取最大的分值
            if str(max_score).isdigit():  # 判断是不是数字
                score = random.randint(0, int(max_score))
                score_result = self.short_send_keys(score_locator, score)
                if score_result is False:
                    break
            else:
                if i == 1:
                    return '不是分值类型！'
                else:
                    self.logger.debugText(errorText='分值类型评标完成')
                    break

    def result_NoPass_or_pass_click(self, projectNumber):  # 选择不通过
        # noinspection PyGlobalUndefined
        global rtn_result
        for i in range(1, 100):
            result_pass = "//div[text()='" + str(
                i) + "']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='通过']"
            result_Nopass = "//div[text()='" + str(
                i) + "']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='不通过']"
            result_pass_locator = (By.XPATH, result_pass)
            result_Nopass_locator = (By.XPATH, result_Nopass)
            rm_pass_num = random.randint(1, 2)
            if rm_pass_num == 1:
                rtn_result = self.js_short_click(result_Nopass_locator)
            elif rm_pass_num == 2:
                rtn_result = self.js_short_click(result_pass_locator)
            else:
                print(rm_pass_num)
            if rtn_result is False:
                break

    def enterprise_review(self, projectNumber, enterprise_count=1000):  # 企业评审
        count = 0  # 用来累计企业个数
        for j in range(1, int(enterprise_count) + 1):
            self.enterprise_input_click()
            time.sleep(0.1)
            enterprise_text = self.choose_enterprise(j)
            count = count + 1
            if enterprise_text is not False:
                score_text = self.score_send_keys(projectNumber)
                if score_text == '不是分值类型！':
                    self.result_NoPass_or_pass_click(projectNumber)
            else:
                self.update_enterprise_count(enterpriseCount=str(count), projectNumber=projectNumber)
                break

    def submit_result_click(self):  # 点击提交审核结果
        return self.js_click(self.submit_result_locator)

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
                if self.is_interactive(signature_examine_locator2):
                    self.js_short_click(signature_examine_locator2)  # 点击查看
                elif self.is_interactive(signature_examine_locator1):
                    self.js_short_click(signature_examine_locator1)  # 点击查看
                else:
                    self.logger.debugText(projectNumber=projectNumber, bidder=username,
                                          errorText='第一个专家评标报告确认完成！')
                    return i
            time.sleep(0.1)
            self.roll_Id("pdfFile-dialog")  # 根据id滑动窗体到底部
            time.sleep(0.5)
            self.js_click(self.judgeAffirm_locator)  # 评委确认
            message = self.get_text(self.alert_locator)
            if str(message).find('成功') > 0:
                self.logger.debugText(errorText='第' + str(i) + '条报告:' + message)
        else:
            self.logger.debugText(projectNumber=projectNumber, errorText='专家确认评标结果完成！！！',
                                  bidder=username)
