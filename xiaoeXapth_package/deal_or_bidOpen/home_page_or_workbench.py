from base.base import Base
import random
import time
from selenium.webdriver.common.by import By
def workbench(projectNumber):#点击工作台
    workbenchButton = "//div[contains(text(),'"+str(projectNumber)+"')]/../following-sibling::td[5]/div/span[text()='工作台']"#点击工作台
    workbench_locator = (By.XPATH,workbenchButton)
    return workbench_locator
class Home_page_or_workbench(Base):
    #公用
    linkMan = "//label[contains(text(),'联系人')]/following-sibling::div/div/input"#输入联系人
    linkManNumber = "//label[contains(text(),'联系手机号')]/following-sibling::div/div/input"#输入联系手机号
    affirmApply = "//span[contains(text(),'确认报名')]"#点击确认报名
    auditAffirm = "//button//span[text()='取 消']/../following-sibling::button//span[contains(text(),'确 定')]"#审核确定
    marginPay = "//span[contains(text(),'投标阶段')]/../following-sibling::div[contains(text(),'保证金缴纳')]"#点击保证金缴纳
    offlinePay = "//div//span[contains(text(),'电子保函')]/../following-sibling::div//span[contains(text(),'线下缴纳')]"#点击线下缴纳
    applyEVE = "//div[contains(text(),'电子保函')]"#申请电子保函按钮
    back_margin = "//button//span[contains(text(),'返回')]"#点击返回
    agreement = "//span[contains(text(),'我已阅读并同意')]/preceding-sibling::label/span/span"#同意协议
    applyEVE_div = "//div[contains(text(),'您将通过')]/../preceding-sibling::div/div//span[text()='申请保函 ']"#点击申请保函
    receiptImg = "//div[contains(text(),'上传图片')]/./following-sibling::div/div/div/div/div/img"#点击图片上传回单
    saveReceipt = "//span[contains(text(),'上传保证金回单')]"#保存回单
    recallReceipt = "//span[contains(text(),'撤回保证金回单')]"#撤回回单
    recallAffirm = "//span[contains(text(),'确 定')]"
    returnButton = "//span[contains(text(),'返回')]"#点击返回
    errorMessage = "//p[@class = 'el-message__content']"#报错信息
    uploadBidFile = "//span[contains(text(),'投标阶段')]/../following-sibling::div[contains(text(),'上传投标文件')]"#上传投标文件
    recallTenderFile = "//span[contains(text(),'撤回标书')]"
    tenderFileAffirm = "//button//span[contains(text(),'确 定')]"
    bidFileImg = "//span[contains(text(),'上传标书')]/./following-sibling::div/div/div/img"#点击图片上传投标文件
    bid_price = "//label[contains(text(),'投标价')]/./following-sibling::div/div/input"#输入投标价
    duration = "//label[contains(text(),'工期')]/./following-sibling::div/div/input"#输入工期
    quality = "//label[contains(text(),'质量标准')]/./following-sibling::div/div/input"#输入质量标准
    bid_file = "//label[contains(text(),'投标文件')]/./following-sibling::div/div/div/div/div"#招标公告
    saveBidFile = "//span[contains(text(),'提交投标文件')]"#保存投标文件
    commitAudit = "//span[contains(text(),'1')]/ancestor::td/following-sibling::td[7]/div/span[text()='提交审核']"#点击提交审核
    commitAudit_affirm = "//button//span[contains(text(),'确 定')]"#提交审核确定
    openBidEntrance = "//span[contains(text(),'开标阶段')]/../following-sibling::div[contains(text(),'开标入口')]"#点击开标入口
    secondaryQuotation = "//span[contains(text(),'开标阶段')]/../following-sibling::div[contains(text(),'二次报价')]"#工作台点击二次报价
    secondaryQuotationInput = "//label[contains(text(),'二次报价')]/./following-sibling::div/div/div/input"#输入二次报价
    secondaryQuotationFile = "//label[contains(text(),'上传响应性文件')]/./following-sibling::div/div/div/div/div"#上传响应性文件
    submitButton = "//button//span[contains(text(),'提交二次报价')]"#提交二次报价按钮
    recall_file = "//button//span[contains(text(),'撤回文件')]"#点击撤回文件按钮
    recall_affirm = "//button//span[contains(text(),'确 定')]"#撤回文件确定
    evaluationBidEntrance = "//span[contains(text(),'开标阶段')]/../following-sibling::div[contains(text(),'评标入口')]"#点击评标入口
    enterpriseName = "//*[@id='header']/div[2]/div[3]/span"#企业名称
    quitLogin = "//li[contains(text(),'修改密码')]/./following-sibling::li[contains(text(),'退出登录')]"#退出登录

    linkMan_locator = (By.XPATH,linkMan)
    submitButton_locator = (By.XPATH,submitButton)
    recall_file_locator = (By.XPATH,recall_file)
    recall_affirm_locator = (By.XPATH,recall_affirm)
    linkManNumber_locator = (By.XPATH,linkManNumber)
    affirmApply_locator = (By.XPATH,affirmApply)
    auditAffirm_locator = (By.XPATH,auditAffirm)
    marginPay_locator = (By.XPATH,marginPay)
    offlinePay_locator = (By.XPATH,offlinePay)
    back_margin_locator = (By.XPATH,back_margin)
    receiptImg_locator = (By.XPATH,receiptImg)
    saveReceipt_locator = (By.XPATH,saveReceipt)
    recallReceipt_locator = (By.XPATH,recallReceipt)
    recallAffirm_locator = (By.XPATH,recallAffirm)
    returnButton_locator = (By.XPATH,returnButton)
    errorMessage_locator = (By.XPATH,errorMessage)
    recallTenderFile_locator = (By.XPATH,recallTenderFile)
    tenderFileAffirm_locator = (By.XPATH,tenderFileAffirm)
    uploadBidFile_locator = (By.XPATH,uploadBidFile)
    secondaryQuotationInput_locator = (By.XPATH,secondaryQuotationInput)
    bidFileImg_locator = (By.XPATH,bidFileImg)
    saveBidFile_locator = (By.XPATH,saveBidFile)
    commitAudit_locator = (By.XPATH,commitAudit)
    secondaryQuotation_locator = (By.XPATH,secondaryQuotation)
    secondaryQuotationFile_locator = (By.XPATH,secondaryQuotationFile)
    bid_price_locator = (By.XPATH,bid_price)
    duration_locator = (By.XPATH,duration)
    quality_locator = (By.XPATH,quality)
    bid_file_locator = (By.XPATH,bid_file)
    commitAudit_affirm_locator = (By.XPATH,commitAudit_affirm)
    openBidEntrance_locator = (By.XPATH,openBidEntrance)
    evaluationBidEntrance_locator = (By.XPATH,evaluationBidEntrance)
    enterpriseName_locator = (By.XPATH,enterpriseName)
    quitLogin_locator = (By.XPATH,quitLogin)

    def commitAudit_click(self):#点击提交审核
        self.click(self.commitAudit_locator)

    def commitAudit_affirm_click(self):#点击提交审核确定
        self.click(self.commitAudit_affirm_locator)

    def linkMan_send_keys(self):#输入联系人
        self.send_keys(self.linkMan_locator,"谢先生")

    def linkManNumber_send_keys(self):#输入联系手机号
        self.send_keys(self.linkManNumber_locator,'15212345678')

    def affirmApply_click(self):#点击确认报名
        self.click(self.affirmApply_locator)

    def secondaryQuotationInput_send_keys(self):#输入投标价
        bidprice = random.randint(10000000,800000000)
        self.send_keys(self.secondaryQuotationInput_locator,bidprice)

    def tender_workbench_click(self,projectNumber):#招标人点击工作台
        workbenchButton = "//div[contains(text(),'"+str(projectNumber)+"')]/../following-sibling::td[6]/div/span[text()='工作台']"#点击工作台
        workbench_locator = (By.XPATH,workbenchButton)
        self.click(workbench_locator)

    def tender_edit_click(self,projectNumber):#招标人编辑
        edit = "//div[contains(text(),'"+str(projectNumber)+"')]/../following-sibling::td[6]/div/span[text()='编辑']"#点击编辑
        edit_locator = (By.XPATH,edit)
        self.click(edit_locator)

    def bid_workbench_click(self,projectNumber):#投标人点击工作台
        workbenchButton = "//div[contains(text(),'"+str(projectNumber)+"')]/../following-sibling::td[5]/div/span[text()='工作台']"#点击工作台
        workbench_locator = (By.XPATH,workbenchButton)
        self.click(workbench_locator)

    def audit_click(self):#点击审核
        try:
            auditButton = "//div[contains(text(),'"+str(self.get_nowTime_formatting())+"')]/../following-sibling::td[5]/div/span[text()='提交审核']"#点击提交审核
            audit_locator = (By.XPATH,auditButton)
            self.click(audit_locator)
        except:
            auditButton = "//div[contains(text(),'"+str(self.get_nowTime_formatting())+"')]/../following-sibling::td[6]/div/span[text()='提交审核']"#点击审核
            audit_locator = (By.XPATH,auditButton)
            self.click(audit_locator)

    def auditAffirm_click(self):#点击审核确认
        self.click(self.auditAffirm_locator)

    def marginPay_click(self):#点击保证金缴纳
        self.click(self.marginPay_locator)

    def offlinePay_click(self):#点击线下缴纳
        self.click(self.offlinePay_locator)

    def margin_back_click(self):#线上和线下选择时的返回
        self.click(self.back_margin_locator)

    def receiptImg_click(self):#点击上传回单图片
        self.click(self.receiptImg_locator)

    def saveReceipt_click(self):#点击保存回单
        self.click(self.saveReceipt_locator)

    def recallReceipt_click(self):#撤回回单
        self.click(self.recallReceipt_locator)

    def recallAffirm_click(self):#撤回确认
        self.click(self.recallAffirm_locator)

    def errorMessage_text(self):#获取错误提示
        message = self.get_text(self.errorMessage_locator)
        return message

    def returnButton_click(self):#点击返回
        self.click(self.returnButton_locator)

    def uploadBidFile_click(self):#点击上传投标文件
        self.click(self.uploadBidFile_locator)

    def recallTenderFile_click(self):#点击撤回标书
        self.click(self.recallTenderFile_locator)

    def tenderFileAffirm_click(self):#撤回标书确定
        self.click(self.tenderFileAffirm_locator)

    def bidFileImg_click(self):#点击上传投标文件图片
        self.click(self.bidFileImg_locator)

    def bid_price_send_keys(self):#输入投标价
        price = random.randint(100000,10000000)
        time.sleep(0.3)
        self.send_keys(self.bid_price_locator,price)

    def duration_send_keys(self):#输入工期
        self.send_keys(self.duration_locator,120)

    def quality_send_keys(self):#输入质量标准
        self.send_keys(self.quality_locator,"好")

    def bid_file_click(self):#招标公告
        self.click(self.bid_file_locator)

    def saveBidFile_click(self):#保存投标文件
        self.click(self.saveBidFile_locator)

    def openBidEntrance_click(self):#点击开标入口
        self.click(self.openBidEntrance_locator)

    def evaluationBidEntrance_click(self):#点击评标入口
        self.click(self.evaluationBidEntrance_locator)

    def secondaryQuotation_click(self):#点击二次报价按钮
        self.click(self.secondaryQuotation_locator)

    def secondaryQuotationFile_input_click(self):#点击上传响应性文件
        self.click(self.secondaryQuotationFile_locator)

    def engpriseName_move(self):#悬浮在企业名称位置
        self.move_mouse(self.enterpriseName_locator)

    def quitLogin_click(self):#点击退出登录
        self.click(self.quitLogin_locator)

    #工程
    engineerBusiness = "//div[@class='el-submenu__title']//span[text()='工程业务']"#工程业务
    tenderProject = "//span[contains(text(),'工程业务')]/../following-sibling::ul/descendant::div[contains(text(),'招标项目')]"#招标项目(工程)
    engineerTenderNotice = "//span[contains(text(),'工程业务')]/../following-sibling::ul/descendant::div[contains(text(),'招标公告')]"#招标公告（工程）
    engineerTenderInvite = "//span[contains(text(),'工程业务')]/../following-sibling::ul/descendant::div[contains(text(),'投标邀请')]"#投标邀请
    engineerApplyProject = "//span[contains(text(),'工程业务')]/../following-sibling::ul/descendant::div[contains(text(),'报名项目')]"#报名项目

    engineerTenderNotice_locator = (By.XPATH,engineerTenderNotice)
    engineerBusiness_locator = (By.XPATH,engineerBusiness)
    tenderProject_locator = (By.XPATH,tenderProject)
    engineerTenderInvite_locator = (By.XPATH,engineerTenderInvite)
    engineerApplyProject_locator = (By.XPATH,engineerApplyProject)

    def engineerBusiness_click(self):#点击工程业务
        self.click(self.engineerBusiness_locator)

    def engineerApplyProject_click(self):#点击报名项目
        self.click(self.engineerApplyProject_locator)

    def engineerTenderNotice_click(self):#点击招标公告(工程)
        self.click(self.engineerTenderNotice_locator)

    def engineerTenderInvite_click(self):#点击工程招标邀请
        self.click(self.engineerTenderInvite_locator)

    def tenderProject_click(self):#点击招标项目
        self.click(self.tenderProject_locator)



    #采购
    purchaseBusiness = "//div[@class='el-submenu__title']//span[contains(text(),'政采业务')]"#政采业务
    purchaseTenderproject = "//span[contains(text(),'政采业务')]/../following-sibling::ul/descendant::div[contains(text(),'招标项目')]"#招标项目(政采)
    purchaseTenderNotice = "//span[contains(text(),'政采业务')]/../following-sibling::ul/descendant::div[contains(text(),'招标公告')]"#招标公告
    purchaseTenderInvite = "//span[contains(text(),'政采业务')]/../following-sibling::ul/descendant::div[contains(text(),'投标邀请')]"#投标邀请
    purchaseApplyProject = "//span[contains(text(),'政采业务')]/../following-sibling::ul/descendant::div[contains(text(),'报名项目')]"


    purchaseBusiness_locator = (By.XPATH,purchaseBusiness)
    purchaseTenderProject_locator = (By.XPATH,purchaseTenderproject)
    purchaseTenderNotice_locator = (By.XPATH,purchaseTenderNotice)
    purchaseTenderInvite_locator = (By.XPATH,purchaseTenderInvite)
    purchaseApplyProject_locator = (By.XPATH,purchaseApplyProject)


    def purchaseTenderNotice_click(self):#点击招标公告（政采）
        self.click(self.purchaseTenderNotice_locator)

    def purchaseApplyProject_click(self):#点击报名项目（政采）
        self.click(self.purchaseApplyProject_locator)

    def purchaseTenderInvite_click(self):#点击政采邀请招标
        self.click(self.purchaseTenderInvite_locator)

    def select_apply(self,projectNumber,projectType,tenderWay):#点击报名
        if projectType == "engineering":#工程
            self.engineerBusiness_click()#点击工程项目
            if tenderWay ==0:
                self.engineerTenderNotice_click()#点击招标公告
            elif tenderWay == 1:
                self.engineerTenderInvite_click()#点击投标邀请
            else:
                print("招标方式输入错入！工程项目没有："+str(tenderWay))
            self.apply_click(projectNumber)
        elif projectType == "purchase" :#政采
            self.purchaseBusiness_click()#点击采购项目
            if tenderWay in  (0,2,3):
                self.purchaseTenderNotice_click()#点击招标公告（政采）
            elif tenderWay in (1,4):
                self.purchaseTenderInvite_click()#点击政采招标邀请
            else:
                print("招标方式输入错入！，0表示公开招标，1表示邀请招标")
            self.apply_click(projectNumber)
        else:
            print("项目类型错误"+projectType)

    def purchaseBusiness_click(self):#点击采购业务
        self.click(self.purchaseBusiness_locator)

    def purchaseTenderProject_click(self):#点击招标项目
        self.click(self.purchaseTenderProject_locator)

    def apply_click(self,projectNumber):
        applyButton = "//div[contains(text(),'"+str(projectNumber)+"')]/../following-sibling::td[6]/div/span[text()='报名']"#点击报名
        apply_locator = (By.XPATH,applyButton)#选择报名项目编号
        self.click(apply_locator)

    def select_tender_workbench(self,projectNumber,projectType):#招标人选择工作台
        if projectType == "engineer":
            #工程
            self.engineerBusiness_click()#点击工程业务
            self.tenderProject_click()#点击招标项目
            self.tender_workbench_click(projectNumber)#点击项目对应的工作台
        elif projectType == "purchase":
            #采购
            self.purchaseBusiness_click()#点击采购业务
            self.purchaseTenderProject_click()#点击招标项目
            self.tender_workbench_click(projectNumber)#点击项目对应的工作台
        else:
            print("招标类型不符"+projectType)

    def select_tender_edit(self,projectNumber,projectType):#招标人和招标代理选择编辑
        if projectType == "engineer":
            #工程
            self.engineerBusiness_click()#点击工程业务
            self.tenderProject_click()#点击招标项目
            self.tender_edit_click(projectNumber)#点击项目对应的编辑
        elif projectType == "purchase":
            #采购
            self.purchaseBusiness_click()#点击采购业务
            self.purchaseTenderProject_click()#点击招标项目
            self.tender_edit_click(projectNumber)#点击项目对应的编辑
        else:
            print("招标类型不符"+projectType)

    def select_bid_workbench(self,projectNumber,projectType):#投标人选择工作台
        if projectType == "engineering":
            #工程
            self.engineerBusiness_click()#点击工程业务
            self.engineerApplyProject_click()#点击工程报名项目
            self.bid_workbench_click(projectNumber)#点击项目对应的工作台
        elif projectType == "purchase":
            #采购
            self.purchaseBusiness_click()#点击采购业务
            self.purchaseApplyProject_click()#点击报名项目
            self.bid_workbench_click(projectNumber)#点击项目对应的工作台
        else:
            print("招标类型不符"+projectType)

    def submitButton_locator_click(self):#点击提交二次报价按钮
        self.click(self.submitButton_locator)

    def recall_file_click(self):#点击撤回文件按钮
        self.click(self.recall_file_locator)

    def recall_affirm_click(self):#撤回文件确定
        self.click(self.recall_affirm_locator)