from base.base import Base
from selenium.webdriver.common.by import By
import time
import traceback
class EvaluationBid_entrance(Base):
    nowEvaluationBidWay = "//span[contains(text(),'当前评标办法')]/../div/div/input"#当前评标办法input
    evaluationBidWay_affirm = "//span[contains(text(),'取消')]/../following-sibling::button/span[contains(text(),'确定')]"#评标办法点击确定
    addScore = "//div[contains(text(),'新增评分点') and @style='']"#新增评分点
    scoreInput = "//div[3]//div//form//div//label[contains(text(),'评分点')]/./following-sibling::div/div/input"#输入评分点
    noMust = "//label//span[contains(text(),'否')]"#不是必须的
    yesMust = "//label//span[contains(text(),'是')]"#是必须的
    reviewStandard = "//div[3]//div/form/div[3]/div/div/textarea"#评审标准输入框
    addScoreSave = "//div[3]//div//div[contains(text(),'保存')]"#新增评分点保存
    cutEvaluationBidWay = "//div[contains(text(),'储存模板')]/preceding-sibling::div[@class='operate-item set-cursor' and  contains(text(),'切换评标办法')]"#切换评标办法
    clickEvaluationBidWay = "//label[contains(text(),'评标办法')]/following-sibling::div/div/div/input[@placeholder='请选择']"#点击请选择
    selectEvaluationBidWay = "//span[contains(text(),'皮卡丘')]"#选择评标办法"皮卡丘"
    cutEvaluationBidWayAffirm = "//p[contains(text(),'切换评标办法')]/following-sibling::div/div[contains(text(),'确定')]"#点击确定
    saveEvaluationBidWay = "//div[contains(text(),'储存模板')]/preceding-sibling::div[@class='operate-item set-cursor' and  contains(text(),'保存评标办法')]"
    saveEvaluationBidWayAffirm = "//span[contains(text(),'保存评标办法')]/../following-sibling::div/div[contains(text(),'确认')]"#确认保存评标办法
    close = "//p[contains(text(),'切换评标办法')]/preceding-sibling::i"#关闭弹窗
    affirmJudge = "//li[contains(text(),'确定评委')]"#确定评委
    addJudge = "//div[contains(text(),'下载评委名单')]/preceding-sibling::div[@class='set-btn set-cursor' and contains(text(),'添加评委')]"#点击添加评委
    judgeNumber = "//div[contains(text(),'下载评委名单')]/following-sibling::div[@class='set-btn set-cursor' and contains(text(),'评委账号管理')]"#评委账号管理
    judgePassword = "//div[text()='1']/ancestor::td/following-sibling::td[3]/div"#密码
    judgeName = "//label[contains(text(),'评委姓名')]/following-sibling::div/div/input"#评委姓名
    unit = "//label[contains(text(),'所在单位')]/following-sibling::div/div/input"#所在单位
    title = "//label[contains(text(),'职称')]/following-sibling::div/div/input"#职称
    mobile = "//label[contains(text(),'手机号码')]/following-sibling::div/div/input"#手机号码
    addJudgeSave = "//p[contains(text(),'添加评委')]/following-sibling::div/div[contains(text(),'保存')]"#保存

    nowEvaluationBidWay_locator = (By.XPATH,nowEvaluationBidWay)
    evaluationBidWay_affirm_locator = (By.XPATH,evaluationBidWay_affirm)
    addScore_locator = (By.XPATH,addScore)
    scoreInput_locator = (By.XPATH,scoreInput)
    noMust_locator = (By.XPATH,noMust)
    yesMust_locator = (By.XPATH,yesMust)
    reviewStandard_locator = (By.XPATH,reviewStandard)
    addScoreSave_locator = (By.XPATH,addScoreSave)
    cutEvaluationBidWay_locator = (By.XPATH,cutEvaluationBidWay)
    clickEvaluationBidWay_locator = (By.XPATH,clickEvaluationBidWay)
    selectEvaluationBidWay_locator = (By.XPATH,selectEvaluationBidWay)
    cutEvaluationBidWayAffirm_locator = (By.XPATH,cutEvaluationBidWayAffirm)
    saveEvaluationBidWay_locator = (By.XPATH,saveEvaluationBidWay)
    saveEvaluationBidWayAffirm_locator = (By.XPATH,saveEvaluationBidWayAffirm)
    close_locator = (By.XPATH,close)
    affirmJudge_locator = (By.XPATH,affirmJudge)
    addJudge_locator = (By.XPATH,addJudge)
    judgeNumber_locator = (By.XPATH,judgeNumber)
    judgePassword_locator = (By.XPATH,judgePassword)
    judgeName_locator = (By.XPATH,judgeName)
    unit_locator = (By.XPATH,unit)
    title_locator = (By.XPATH,title)
    mobile_locator = (By.XPATH,mobile)
    addJudgeSave_locator = (By.XPATH,addJudgeSave)

    def addScore_click(self):#新增评分点按钮
        self.click(self.addScore_locator)


    def scoreInput_send_keys(self,num):#输入评分点
        self.send_keys(self.scoreInput_locator,"评分点"+str(num))

    def mustType_click(self,num):#选择是否必须
        if num == 1:
            self.click(self.noMust_locator)
        elif num == 2:
            self.click(self.yesMust_locator)
        else:
            print("mustType是否必须参数错误，只能输入1 or 2")

    def reviewStandard_send_keys(self,num):#输入评分标准
        if num == 1 :
            self.send_keys(self.reviewStandard_locator,"非必须")
        elif num == 2:
            self.send_keys(self.reviewStandard_locator,"必须")
        else:
            print("reviewStandard是否必须参数错误，只能输入1 or 2")

    def addScoreSave_click(self):#保存评分点
        self.click(self.addScoreSave_locator)

    def nowEvaluationBidWay_click(self):#点击当前评标类型
        self.click(self.nowEvaluationBidWay_locator)

    def choose_EvaluationBidWay(self,num):#选择评标类型
        evaluationBidWay0 = "//span[contains(text(),'综合评标法')]"
        evaluationBidWay1 = "//span[contains(text(),'均值评标法')]"
        evaluationBidWay2 = "//span[contains(text(),'最低价评标法')]"
        evaluationBidWay3 = "//span[contains(text(),'最高价评标法')]"
        evaluationBidWay4 = "//span[contains(text(),'竞争性磋商')]"
        evaluationBidWay5="//span[contains(text(),'最低价评标法(竞争性谈判)')]"
        evaluationBidWay6="//span[contains(text(),'综合评标法(单一来源采购)')]"
        if num == 0:
            evaluationBidWay_locator0 = (By.XPATH,evaluationBidWay0)
            self.click(evaluationBidWay_locator0)
        elif num == 1 :
            evaluationBidWay_locator1 = (By.XPATH,evaluationBidWay1)
            self.click(evaluationBidWay_locator1)
        elif num == 2:
            evaluationBidWay_locator2 = (By.XPATH,evaluationBidWay2)
            self.click(evaluationBidWay_locator2)
        elif num == 3 :
            evaluationBidWay_locator3 = (By.XPATH,evaluationBidWay3)
            self.click(evaluationBidWay_locator3)
        elif num == 4:
            evaluationBidWay_locator4 = (By.XPATH,evaluationBidWay4)
            self.click(evaluationBidWay_locator4)
        elif num == 5:
            evaluationBidWay_locator5 = (By.XPATH,evaluationBidWay5)
            self.click(evaluationBidWay_locator5)
        elif num == 6:
            evaluationBidWay_locator6 = (By.XPATH,evaluationBidWay6)
            self.click(evaluationBidWay_locator6)
        else:
            print("评标办法类型错误"+str(num)+"只能输入0到6的整数")

        try:
            self.evaluationBidWay_affirm_click()#选择评标办法点击确定
        except(Exception,BaseException):
            error = traceback.format_exc()
            print(error)
            print("当前是该评标办法无需切换")

    def evaluationBidWay_affirm_click(self):#选择评标办法点击确定
        self.click(self.evaluationBidWay_affirm_locator)

    def cutEvaluationBidWay_click(self):#切换评标办法
        self.click(self.cutEvaluationBidWay_locator)

    def clickEvaluationBidWay_click(self):#点击请选择
        self.click(self.clickEvaluationBidWay_locator)

    def selectEvaluationBidWay_click(self):#选择评标办法"皮卡丘"
        self.click(self.selectEvaluationBidWay_locator)

    def cutEvaluationBidWayAffirm_click(self):#点击确定
        self.click(self.cutEvaluationBidWayAffirm_locator)

    def saveEvaluationBidWay_click(self):#保存评标办法
        self.click(self.saveEvaluationBidWay_locator)

    def saveEvaluationBidWayAffirm_click(self):#保存评标办法点击确认
        self.click(self.saveEvaluationBidWayAffirm_locator)

    def close_click(self):#管理弹窗
        self.click(self.close_locator)

    def affirmJudge_click(self):#点击确认评委
        self.click(self.affirmJudge_locator)

    def addJudge_click(self):#添加评委
        self.click(self.addJudge_locator)

    def judgeNumber_click(self):#评委账号管理
        self.click(self.judgeNumber_locator)

    def create_judge(self,judgeNumber):#创建评委
        for i in range(judgeNumber):
            self.addJudge_click()#点击添加评委
            self.judgeName_send_keys("评委"+str(i+1))
            self.unit_send_keys()#输入所在单位
            self.title_send_keys()#输入职称
            self.mobile_send_keys()#输入手机号码
            self.addJudgeSave_click()#保存添加评委
            time.sleep(1)

    def save_judge_username_password(self,projectNumber,judgesCount):#保存评委账号和密码
        for i in range(judgesCount):
            judgeName = "//div[text()='"+str(i+1)+"']/ancestor::td/following-sibling::td[1]/div"#评委名称数量
            judgeUsername = "//div[text()='"+str(i+1)+"']/ancestor::td/following-sibling::td[2]/div"#账号
            judgePassword = "//div[text()='"+str(i+1)+"']/ancestor::td/following-sibling::td[3]/div"#密码
            judgeName_locator = (By.XPATH,judgeName)
            judgeUsername_locator = (By.XPATH,judgeUsername)
            judgePassword_locator = (By.XPATH,judgePassword)
            try:
                name = self.get_text(judgeName_locator)
                username = self.get_text(judgeUsername_locator)
                password = self.get_text(judgePassword_locator)
                self.insert_expertData(projectNumber=projectNumber,username=username,password=password,judgeName=name)
            except(Exception,BaseException):
                error = traceback.format_exc()
                print(error)
                print("------------评委个数为"+str(i+1)+"------------")


    def judgeName_send_keys(self,judgeName):#输入评委名字
        self.send_keys(self.judgeName_locator,judgeName)

    def unit_send_keys(self):#输入所在单位
        self.send_keys(self.unit_locator,"农大侠")

    def  title_send_keys(self):#输入职称
        self.send_keys(self.title_locator,"技术")

    def mobile_send_keys(self):#输入手机号码
        self.send_keys(self.mobile_locator,"15212345678")

    def addJudgeSave_click(self):#点击保存
        self.click(self.addJudgeSave_locator)
