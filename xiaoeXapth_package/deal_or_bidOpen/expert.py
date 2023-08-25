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
    username_input = "//input[@placeholder='请输入账号']"#账号输入框
    password_input = "//input[@placeholder='请输入密码']"#密码输入框
    img = "//input[@placeholder='请输入图形码']/ancestor::div[@class='w-full aui-padded-r-10']/following-sibling::div/img"#图片验证码
    img_input = "//input[@placeholder='请输入图形码']"#图形验证码输入框
    login_button = "//button/span[contains(text(),'登录')]"#登录按钮
    alert = "//div[@role='alert']"#报错信息
    know = "//button//span[contains(text(),'我已知悉')]"#协议
    electGroup = "//button//span[contains(text(),'推选组长')]"#推选组长
    group = "//div//span[contains(text(),'当选组长')]/../preceding-sibling::div/../preceding-sibling::p[@class='aui-font-weight-700 aui-000000 aui-padded-t-4']"
    review1 = "//p[contains(text(),'开始评标')]/following-sibling::div/p[1]/button"#初步评审
    review2 = "//p[contains(text(),'开始评标')]/following-sibling::div/p[2]/button"#技术评审
    review3 = "//p[contains(text(),'开始评标')]/following-sibling::div/p[3]/button"#最终评审
    review4 = "//p[contains(text(),'开始评标')]/following-sibling::div/p[4]/button"
    score1 = "//div[text()='1']/ancestor::td/following-sibling::td[4]/div/div/div/input"#分值1
    score2 = "//div[text()='2']/ancestor::td/following-sibling::td[4]/div/div/div/input"#分值1
    result_1_Pass = "//div[text()='1']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='通过']"
    result_1_NoPass = "//div[text()='1']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='不通过']"
    result_2_Pass = "//div[text()='2']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='通过']"
    result_2_NoPass = "//div[text()='2']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='不通过']"
    enterprise_input = "//input[@placeholder='请选择']"#点击企业输入框
    submit_result = "//div[contains(text(),'提交评审结果')]"#点击提交审核结果
    submitResult_affirm = "//div[text()='确认']"
    judgeSignature = "//button//span[contains(text(),'确认评标报告')]"
    judgeAffirm = "//button//span[contains(text(),'评委确认')]"

    username_input_locator = (By.XPATH,username_input)
    password_input_locator = (By.XPATH,password_input)
    img_locator = (By.XPATH,img)
    img_input_locator = (By.XPATH,img_input)
    login_button_locator = (By.XPATH,login_button)
    alert_locator = (By.XPATH,alert)
    know_locator = (By.XPATH,know)
    electGroup_locator = (By.XPATH,electGroup)
    group_locator = (By.XPATH,group)
    review1_locator = (By.XPATH,review1)
    review2_locator = (By.XPATH,review2)
    review3_locator = (By.XPATH,review3)
    review4_locator = (By.XPATH,review4)
    score1_locator = (By.XPATH,score1)
    score2_locator = (By.XPATH,score2)
    result_1_Pass_locator= (By.XPATH,result_1_Pass)
    result_1_NoPass_locator = (By.XPATH,result_1_NoPass)
    result_2_Pass_locator= (By.XPATH,result_2_Pass)
    result_2_NoPass_locator = (By.XPATH,result_2_NoPass)
    enterprise_input_locator = (By.XPATH,enterprise_input)
    submit_result_locator = (By.XPATH,submit_result)
    submitResult_affirm_locator = (By.XPATH,submitResult_affirm)
    judgeSignature_locator = (By.XPATH,judgeSignature)
    judgeAffirm_locator = (By.XPATH,judgeAffirm)


    def login(self,username,password,projectNumber):
        self.open_expert_url()
        self.send_keys(self.username_input_locator,username)
        self.send_keys(self.password_input_locator,password)
        isAgree = self.select_isAgree(username,projectNumber)
        for j in range(150):
            try:
                self.savePictrue(self.img_locator)
                pic = self.getPicPassword()
                self.send_keys(self.img_input_locator, pic)
                self.click(self.login_button_locator)  # 点击登录按钮
                errortext = self.alert_getClass()#获取错误提示弹窗类型
                if errortext != self.successClass:
                    time.sleep(1)
            except(Exception, BaseException):
                self.in_project_click(projectNumber=projectNumber)
                if self.is_url(self.expert_projectList_url):  # 判断有没有进入专家平台
                    time.sleep(3)
                    self.in_project_click(projectNumber=projectNumber)
                else:
                    try:
                        if isAgree[0] == "disAgree":
                            self.click(self.know_locator)
                            self.update_isAgree("consent", username, projectNumber)
                            break
                        elif isAgree[0] == "consent":
                            break
                        else:
                            print("专家协议类型错误" + isAgree[0])
                    except:
                        self.update_isAgree("consent", username, projectNumber)
                        break
                # text = traceback.format_exc()
                # self.logger.debugText(projectNumber=projectNumber,bidder=username,errorText=text)
                # if self.is_url(self.expert_login_url) is not True:#判断是否登陆成功


    def electGroup_click(self):#点击推选组长
        self.click(self.electGroup_locator)#点击推选组长

    def elect_click(self,name):#点击推选
        choose = "//p[contains(text(),'"+name+"')]/following-sibling::div/button/span[contains(text(),'推选')]"#推选
        choose_locator = (By.XPATH,choose)
        self.click(choose_locator)#点击推选

    def select_group(self,username,password,name,projectNumber):#选择组长
        if len(username) > 0:
            for i in range(len(username)):
                self.login(username=username[i],password=password[i],projectNumber=projectNumber)
                self.electGroup_click()#点击推选组长
                try:
                    a =random.randint(0,len(username)-1)#随机生成推选评委
                    self.elect_click(name=name[a])#点击推选
                    time.sleep(0.2)
                except (Exception, BaseException):
                    exstr = traceback.format_exc()
                    print(exstr)
        else:
            print('没有保存评委:'+str(len(username)))

    def in_project_click(self,projectNumber):
        in_project = "//div[contains(text(),'"+str(projectNumber)+"')]/../following-sibling::td[4]/div/button/span[contains(text(),'进入项目')]"
        in_project_locator = (By.XPATH,in_project)
        self.click(in_project_locator)

    def get_group(self):#获取组长评委
        review = self.get_text(self.group_locator)
        return review

    def alert_getClass(self):#获取弹窗类型
        errortext = self.get_attribute_value(locator=self.alert_locator,attribute='class')
        return errortext

    def review_click(self,buttonCount):#专家选择评标类型
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
            print("评标类型输入有误"+ str(buttonCount))

    def enterprise_input_click(self):#点击选择企业输入框
        self.click(self.enterprise_input_locator)
        time.sleep(0.5)

    def choose_enterprise(self,num):#选择企业
        js_code = 'document.getElementsByClassName("el-select-dropdown__wrap el-scrollbar__wrap")[0].scrollBy(0, '+str(30)+')'
        self.drive.execute_script(js_code)
        choose_enterprise = "//div//ul//li["+str(num)+"]/span"#选择企业
        choose_enterprise_locator = (By.XPATH,choose_enterprise)
        time.sleep(0.1)
        self.short_click(choose_enterprise_locator)

    def score_send_keys(self,projectNumber,ratingPointCount = 100):#输入分值
        count = 0#用来统计评分点个数
        for i in range(1,int(ratingPointCount)+1):
            score_input = "//div[text()='"+str(i)+"']/ancestor::td/following-sibling::td[4]/div/div/div/input"
            score_locator = (By.XPATH,score_input)
            score = random.randint(20,40)
            try:#用来判断有多少个评分点
                time.sleep(0.5)
                if self.is_interactive(score_locator) is True:#判断元素是否可交互
                    self.short_send_keys(score_locator,score)
                else:
                    print('分值式元素不可交互!')
                    break
                count = count + 1
            except:
                if i == 1:
                    raise Exception("不是分值类型")
                else:
                    self.update_ratingPoint_count(ratingPointCount=count,ratingType='0',projectNumber=projectNumber)
                    break

    def result_NoPass_or_pass_click(self,projectNumber,ratingPointCount = 100):#选择不通过
        count = 0
        for i in range(1,int(ratingPointCount)+1):
            result_pass = "//div[text()='"+str(i)+"']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='通过']"
            result_Nopass = "//div[text()='"+str(i)+"']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='不通过']"
            result_pass_locator = (By.XPATH,result_pass)
            result_Nopass_locator = (By.XPATH,result_Nopass)
            result = random.randint(1,2)
            time.sleep(0.1)
            try:#用来判断有多少个评分点
                if self.is_interactive(result_pass_locator)is True:
                    if result == 1:
                        self.click(result_Nopass_locator)
                    else:
                        self.click(result_pass_locator)
                else:
                    print('通过是方式元素不可交互!')
                count = count + 1
            except:
                if i == 1:
                    raise Exception("不是通过式！")
                else:
                    self.update_ratingPoint_count(ratingPointCount= count,ratingType='1',projectNumber=projectNumber)
                    break

    def enterprise_review(self,projectNumber,enterprise_count = 1000):#企业评审
        count = 0#用来累计企业个数
        for j in range(1,int(enterprise_count)+1):
            result = self.query_projectData(projectNumber)
            ratingPointCount = result[7]
            ratingType = result[8]
            self.enterprise_input_click()
            time.sleep(0.1)
            try:#用来判断有多少家企业
                self.choose_enterprise(j)
                count = count + 1
            except:
                self.update_enterprise_count(enterpriseCount=str(count),projectNumber=projectNumber)
                break

            """
            ratingPointCount 如果等于0的话说明没有评标（默认为0）
            """
            if ratingPointCount == '0':
                try:
                    self.score_send_keys(projectNumber)
                except:
                    self.result_NoPass_or_pass_click(projectNumber)
            else:
                if ratingType == '0':
                    self.score_send_keys(projectNumber=projectNumber,ratingPointCount=ratingPointCount)
                elif ratingType == '1':
                    self.result_NoPass_or_pass_click(projectNumber=projectNumber,ratingPointCount=ratingPointCount)

    def submit_result_click(self):#点击提交审核结果
        self.click(self.submit_result_locator)

    def submitResult_affirm_click(self):#点击确认
        self.click(self.submitResult_affirm_locator)

    def judgeSignature_click(self):#点击评委签章
        self.click(self.judgeSignature_locator)

    def examine1(self,num):#返回查看的xpath
        signature_examine1 = "//div[text()='"+str(num)+"']/ancestor::td/following-sibling::td[4]/div/button/span[contains(text(),'查看')]"
        return signature_examine1

    def examine2(self,num):#返回查看的xpath
        signature_examine2 = "//div[text()='"+str(num)+"']/ancestor::td/following-sibling::td[3]/div/button/span[contains(text(),'查看')]"
        return signature_examine2

    def signature_examine(self,evaluationReportNumber = 20):#点击评委查看和确认
            global i
            for i in range(1,evaluationReportNumber):
                signature_examine1 = self.examine1(i)
                signature_examine2 = self.examine2(i)
                signature_examine_locator1 = (By.XPATH,signature_examine1)
                signature_examine_locator2 = (By.XPATH,signature_examine2)
                if i ==1:
                    time.sleep(0.5)
                    self.short_click(signature_examine_locator1)
                    time.sleep(0.2)
                else:
                    time.sleep(0.5)
                    try:
                        self.short_click(signature_examine_locator2)#点击查看
                    except:
                        try:
                            self.short_click(signature_examine_locator1)#点击查看
                        except:
                            break
                time.sleep(0.1)
                self.roll_Id("pdfFile-dialog")#根据id滑动窗体到底部
                time.sleep(0.5)
                self.click(self.judgeAffirm_locator)#评委确认
            return i





