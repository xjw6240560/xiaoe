from base.base import Base
from selenium.webdriver.common.by import By
import time
import random
from xiaoeXapth_package.deal_or_bidOpen.evaluationBid_entrance import EvaluationBid_entrance

class Expert(Base):
    evaluationBid_entrance = EvaluationBid_entrance()
    username_input = "//input[@placeholder='请输入账号']"#账号输入框
    password_input = "//input[@placeholder='请输入密码']"#密码输入框
    img = "//input[@placeholder='请输入图形码']/ancestor::div[@class='w-full aui-padded-r-10']/following-sibling::div/img"#图片验证码
    img_input = "//input[@placeholder='请输入图形码']"#图形验证码输入框
    login_button = "//button/span[contains(text(),'登录')]"#登录按钮
    log = "//div[@role='alert']/p"#报错信息
    know = "//button//span[contains(text(),'我已知悉')]"#协议
    electGroup = "//button//span[contains(text(),'推选组长')]"#推选组长
    group = "//div//span[contains(text(),'当选组长')]/../preceding-sibling::div/../preceding-sibling::p[@class='aui-font-weight-700 aui-000000 aui-padded-t-4']"
    review1 = "//p[contains(text(),'开始评标')]/following-sibling::div/p[1]/button"#初步评审
    review2 = "//p[contains(text(),'开始评标')]/following-sibling::div/p[2]/button"#技术评审
    review3 = "//p[contains(text(),'开始评标')]/following-sibling::div/p[3]/button"#最终评审
    review4 = "//button//span[contains(text(),'资格评审')]"#资格评审
    score1 = "//div[text()='1']/ancestor::td/following-sibling::td[4]/div/div/div/input"#分值1
    score2 = "//div[text()='2']/ancestor::td/following-sibling::td[4]/div/div/div/input"#分值1
    result_1_Pass = "//div[text()='1']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='通过']"
    result_1_NoPass = "//div[text()='1']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='不通过']"
    result_2_Pass = "//div[text()='2']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='通过']"
    result_2_NoPass = "//div[text()='2']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='不通过']"
    enterprise_input = "//input[@placeholder='请选择']"#点击企业输入框
    submit_result = "//div[contains(text(),'提交评审结果')]"#点击提交审核结果
    submitResult_affirm = "//div[text()='确认']"
    judgeSignature = "//button//span[contains(text(),'评委签章')]"
    judgeAffirm = "//button//span[contains(text(),'评委确认')]"

    username_input_locator = (By.XPATH,username_input)
    password_input_locator = (By.XPATH,password_input)
    img_locator = (By.XPATH,img)
    img_input_locator = (By.XPATH,img_input)
    login_button_locator = (By.XPATH,login_button)
    log_locator = (By.XPATH,log)
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


    def login(self,username,password):
        self.open_expert_url()
        self.send_keys(self.username_input_locator,username)
        self.send_keys(self.password_input_locator,password)
        isAgree = self.select_isAgree(username)
        try:
            for j in range(15):
                self.savePictrue(self.img_locator)
                time.sleep(0.1)
                pic = self.getPicPassword()
                self.send_keys(self.img_input_locator,pic)
                self.click(self.login_button_locator)#点击登录按钮
                time.sleep(0.5)
                nowUrl = self.get_nowUrl()#获取当前url地址
                if str(nowUrl) != "http://expert.jiaoyi.com/#/login":
                    if isAgree[0] == "disAgree" :
                        self.click(self.know_locator)
                        self.update_isAgree(username,"consent")
                        break
                    elif isAgree[0] == "consent":
                        print("专家协议同意已经确认过"+isAgree)
                        break
                    else:
                        print("专家协议类型错误"+isAgree)
        except:
            pass

    def electGroup_click(self):#点击推选组长
        self.click(self.electGroup_locator)#点击推选组长

    def elect_click(self,judgeCount):#点击推选
        num = random.randint(1,judgeCount)
        choose = "//p[contains(text(),'评委"+str(num)+"')]/following-sibling::div/button/span[contains(text(),'推选')]"#推选
        # choose = "//p[contains(text(),'评委1')]/following-sibling::div/button/span[contains(text(),'推选')]"#推选
        choose_locator = (By.XPATH,choose)
        self.click(choose_locator)#点击推选

    def select_group(self,username,password,judgesCount):#选择组长
        for i in range(len(username)):
            self.login(username=username[i],password=password[i])
            self.electGroup_click()#点击推选组长
            try:
                self.elect_click(judgesCount)#点击推选
            except:
                print("已经推荐过了")


    def get_group(self):#获取组长评委
        review = self.get_text(self.group_locator)
        print("---------------------"+review+"---------------------")

    def review_click(self,evaluationBidWay):#专家选择评标类型
        time.sleep(0.2)
        if evaluationBidWay == 0:
            try:
                text3 = self.is_disabled(self.review3_locator)
            except:
                text3 = '评标类型3不存在'
                print('评标类型3不存在')

            try:
                text2 = self.is_disabled(self.review2_locator)
            except:
                text2 = '评标类型2不存在'
                print('评标类型2不存在')
            if text3 is not None:
                if text2 is not None:
                    self.click(self.review1_locator)
                    return 1
                else:
                    self.click(self.review2_locator)
                    return 2
            else:
                self.click(self.review3_locator)
                return 3
        elif evaluationBidWay in (1,2,3):
            self.click(self.review4_locator)
            return 3
        else:
            print("评标类型输入有误"+ evaluationBidWay)

    def enterprise_input_click(self):#点击选择企业输入框
        self.click(self.enterprise_input_locator)
        time.sleep(0.2)

    def choose_enterprise(self,num):#选择企业
        js_code = 'document.getElementsByClassName("el-select-dropdown__wrap el-scrollbar__wrap")[0].scrollBy(0, '+str(30)+')'
        self.drive.execute_script(js_code)
        choose_enterprise = "//div//ul//li["+str(num)+"]"#选择企业
        choose_enterprise_locator = (By.XPATH,choose_enterprise)
        time.sleep(0.1)
        self.click(choose_enterprise_locator)

    def score_send_keys(self,input_count = 100):#输入分值
        count = 1#用来统计评分点个数
        for i in range(1,input_count):
            score_input = "//div[text()='"+str(i)+"']/ancestor::td/following-sibling::td[4]/div/div/div/input"
            score_locator = (By.XPATH,score_input)
            score = random.randint(20,40)
            try:#用来判断有多少个评分点
                time.sleep(0.15)
                self.send_keys(score_locator,score)
            except:
                if i == 1:
                    raise ValueError("不是分值类型")
                break
            count = count + 1
        return count

    def result_NoPass_or_pass_click(self,input_count = 100):#选择不通过
        count = 1
        for i in range(1,input_count):
            result_pass = "//div[text()='"+str(i)+"']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='通过']"
            result_Nopass = "//div[text()='"+str(i)+"']/ancestor::td/following-sibling::td[3]/div/div/div/label/span[text()='不通过']"
            result_pass_locator = (By.XPATH,result_pass)
            result_Nopass_locator = (By.XPATH,result_Nopass)
            result = random.randint(1,2)
            time.sleep(0.1)
            try:#用来判断有多少个评分点
                if result == 1:
                    self.click(result_Nopass_locator)
                else:
                    self.click(result_pass_locator)
            except:
                print("通过评分点"+str(i)+"未找到")
                break
            count = count + 1
        return count

    def enterprise_review(self,type,enterprise_count = 1000,input_count = 0):#企业评审
        count = 1#用来累计企业个数
        for j in range(1,enterprise_count):
            self.enterprise_input_click()
            time.sleep(0.1)
            try:#用来判断有多少家企业
                self.choose_enterprise(j)
                count = count + 1
            except:
                print("总共有"+str(count-1)+"家企业")
                break

            if type in (1,2):
                if input_count == 0:
                    input_count = self.score_send_keys()
                else:
                    self.score_send_keys(input_count)
            elif type == 3:
                if input_count == 0:
                    input_count = self.result_NoPass_or_pass_click()
                else:
                    self.result_NoPass_or_pass_click(input_count)
        return count,input_count

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

    def signature_examine(self,evaluationBidWay):#点击评委查看和确认
        if evaluationBidWay == 0:
            for i in range(1,8):
                signature_examine1 = self.examine1(i)
                signature_examine2 = self.examine2(i)
                if i == 1 or i == 4:
                    signature_examine_locator1 = (By.XPATH,signature_examine1)
                else:
                    signature_examine_locator1 = (By.XPATH,signature_examine2)
                self.click(signature_examine_locator1)#点击查看
                time.sleep(0.1)
                self.roll_Id("pdfFile-dialog")#根据id滑动窗体到底部
                time.sleep(0.2)
                self.click(self.judgeAffirm_locator)#评委确认
        elif evaluationBidWay in (1,2,3):
            for j in range(1,4):
                signature_examine1 = self.examine1(j)
                signature_examine2 = self.examine2(j)
                if j == 1 or j ==2 :
                    signature_examine_locator2 = (By.XPATH,signature_examine1)
                else:
                    signature_examine_locator2 = (By.XPATH,signature_examine2)
                time.sleep(0.1)
                self.click(signature_examine_locator2)#点击查看
                self.roll_Id("pdfFile-dialog")#根据id滑动窗体到底部
                time.sleep(0.2)
                self.click(self.judgeAffirm_locator)#评委确认
        else:
            print("评标方式传值错误")




