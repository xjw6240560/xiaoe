from selenium.webdriver.common.by import By
from base.base import Base
import time
class CreateProjectMethod(Base):
    addtime = 25
    addTenderProjectButton = "//div[contains(text(),'招标项目')]/following-sibling::button//span[contains(text(),'新增招标项目')]"#新增招标项目
    projectNumber = "//label[contains(text(),'招标项目编号:')]/following-sibling::div/div/input"#项目编号
    projectName = "//label[contains(text(),'招标项目名称:')]/following-sibling::div/div/input"#项目名称
    projectAuditNumber = "//label[contains(text(),'项目审批文号:')]/following-sibling::div/div/input"#项目审批文号
    InvestprojectUnicode = "//label[contains(text(),'投资项目统一代码:')]/following-sibling::div/div/input"#投资项目统一代码
    tenderType = "//label[contains(text(),'招标类型:')]/following-sibling::div/div/div/input"#招标类型
    build = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'施工')]"#招标类型（施工）
    projectType = "//label[contains(text(),'项目类型:')]/following-sibling::div/div/div/input"#项目类型
    houseBuild = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'房屋建筑')]"#项目类型（房屋建设）
    tenderWay = "//label[contains(text(),'招标方式:')]/following-sibling::div/div/div/div/input"#招标方式
    openTender = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'公开招标')]"#招标方式（公开招标）
    inviteTender = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'邀请招标')]"#招标方式（邀请招标）
    inviteBid = "//label[contains(text(),'方式:')]/following-sibling::div/div/div/following-sibling::button/span[contains(text(),'邀请投标人')]"#邀请投标人按钮
    enterpriseInput = "//div[contains(text(),'邀请投标单位')]/following-sibling::div[1]/div/div/input"#企业输入框
    find = "//button//span[contains(text(),'查找')]"#查找
    add = "//div//span[contains(text(),'添加')]"#添加企业
    close = "//div[contains(text(),'邀请投标单位')]/preceding-sibling::div[text()='×']"#点击关闭
    tenderOrganizationType = "//label[contains(text(),'招标组织方式:')]/following-sibling::div/div/div/input"#招标组织方式
    oneselfTender = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'自主招标')]"#自主招标
    entrustTender = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'委托招标')]"#委托招标
    projectPlace = "//label[contains(text(),'项目地点')]/following-sibling::div/div/input"#项目地点
    projectPrice = "//label[contains(text(),'项目估算价')]/following-sibling::div/div/input"#项目估算价
    projectDate =  "//label[contains(text(),'工期')]/following-sibling::div/div/input"#工期
    tenderLinkMan = "//label[contains(text(),'招标人联系人')]/following-sibling::div/div/input"#招标联系人
    tenderLinkManNumber = "//label[contains(text(),'招标人联系人手机号:')]/following-sibling::div/div/input"#招标联系人手机号
    linkPlace = "//label[contains(text(),'联系地址:')]/following-sibling::div/div/input"#联系地址
    tenderGency = "//label[contains(text(),'招标代理:')]/following-sibling::div/div"#招标代理
    input_enterprise = "//span[contains(text(),'搜索')]/../preceding-sibling::div/input[@placeholder='请输入企业名称']"#输入招标代理企业名称
    search = "//span[contains(text(),'搜索')]"#点击搜索
    selectTenderGency = "//span[contains(text(),'1')]/ancestor::td/following-sibling::td//span[contains(text(),'选择')]"#选择招标代理
    sectionNumber = "//label[contains(text(),'标段编号:')]/following-sibling::div/div/input"#标段编号
    sectionName = "//label[contains(text(),'标段名称:')]/following-sibling::div/div/input"#标段名称
    tenderFileBeginTime = "//label[contains(text(),'招标文件领取开始时间:')]/following-sibling::div/div/input"#招标文件领取开始时间
    tenderFileEndTime = "//label[contains(text(),'招标文件领取截止时间:')]/following-sibling::div/div/input"#招标文件领取截止时间
    applybeginTime = "//label[contains(text(),'报名开始时间:')]/following-sibling::div/div/input"#报名开始时间
    applyEndTime = "//label[contains(text(),'报名截止时间:')]/following-sibling::div/div/input"#报名截止时间
    quizEndTime = "//label[contains(text(),'提问截止时间:')]/following-sibling::div/div/input"#提问截止时间
    answerEndTime = "//label[contains(text(),'答疑截止时间:')]/following-sibling::div/div/input"#答疑截止时间
    bidFileEndTime = "//label[contains(text(),'投标文件递交截止时间:')]/following-sibling::div/div/input"#投标文件递交截止时间
    bidOpenTime = "//label[contains(text(),'开标时间:')]/following-sibling::div/div/input"#开标时间
    tenderFileCost = "//label[contains(text(),'招标文件费')]/following-sibling::div/div/input"#招标文件费用
    marginPaymentWay = "//label[contains(text(),'保证金缴纳方式:')]/following-sibling::div/div/div/input"#保证金缴纳方式
    EVE = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'电子保函')]"#保证金缴纳方式(电子保函)
    offlinePayment = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'线下缴纳')]"#保证金缴纳方式(线下缴纳)
    EVE_or_offlinePayment = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'电子保函或线上缴纳')]"#选择线上和线下
    marginSum = "//label[contains(text(),'保证金额')]/following-sibling::div/div/input"#保证金额
    marginEndTime = "//label[contains(text(),'保证金缴纳截止时间:')]/following-sibling::div/div/input"#保证金缴纳截止日期
    tenderNotice = "//label[contains(text(),'招标公告:')]/following-sibling::div/div/div/div/div//span"#上传招标公告
    tenderFile = "//label[contains(text(),'招标文件:')]/following-sibling::div/div/div/div/div//span"#上传招标文件
    saveButton = "//button[@class='el-button aui-margin-l-40 el-button--primary']//span[contains(text(),'保 存')]"#点击保存


    #采购
    purchaseType = "//label[contains(text(),'采购类型:')]/following-sibling::div/div/div/input"#采购类型
    purchaseBuild = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'工程类')]"#采购类型(工程类)
    purchaseWay = "//label[contains(text(),'采购方式:')]/following-sibling::div/div/div/div/input"#采购方式
    purchasePrice = "//label[contains(text(),'采购预算')]/following-sibling::div/div/input"#采购预算

    purchaseType_locator = (By.XPATH,purchaseType)
    purchaseBuild_locator = (By.XPATH,purchaseBuild)
    purchaseWay_locator = (By.XPATH,purchaseWay)
    purchasePrice_locator = (By.XPATH,purchasePrice)



    addTenderProjectButton_locator = (By.XPATH,addTenderProjectButton)
    projectNumber_locator = (By.XPATH,projectNumber)
    projectName_locator = (By.XPATH,projectName)
    projectAuditNumber_locator = (By.XPATH,projectAuditNumber)
    InvestprojectUnicode_locator = (By.XPATH,InvestprojectUnicode)
    tenderType_locator = (By.XPATH,tenderType)
    build_locator = (By.XPATH,build)
    projectType_locator = (By.XPATH,projectType)
    houseBuild_locator = (By.XPATH,houseBuild)
    tenderWay_locator = (By.XPATH,tenderWay)
    openTender_locator = (By.XPATH,openTender)
    inviteTender_locator = (By.XPATH,inviteTender)
    inviteBid_locator = (By.XPATH,inviteBid)
    enterpriseInput_locator = (By.XPATH,enterpriseInput)
    find_locator = (By.XPATH,find)
    add_locator = (By.XPATH,add)
    close_locator = (By.XPATH,close)
    tenderOrganizationType_locator = (By.XPATH,tenderOrganizationType)
    oneselfTender_locator = (By.XPATH,oneselfTender)
    entrustTender_locator = (By.XPATH,entrustTender)
    projectPlace_locator = (By.XPATH,projectPlace)
    projectPrice_locator = (By.XPATH,projectPrice)
    projectDate_locator = (By.XPATH,projectDate)
    tenderLinkMan_locator = (By.XPATH,tenderLinkMan)
    tenderLinkManNumber_locator = (By.XPATH,tenderLinkManNumber)
    linkPlace_locator = (By.XPATH,linkPlace)
    tenderGency_locator = (By.XPATH,tenderGency)
    input_enterprise_locator = (By.XPATH,input_enterprise)
    search_locator = (By.XPATH,search)
    selectTenderGency_locator = (By.XPATH,selectTenderGency)
    sectionNumber_locator = (By.XPATH,sectionNumber)
    sectionName_locator = (By.XPATH,sectionName)
    tenderFileBeginTime_locator = (By.XPATH,tenderFileBeginTime)
    tenderFileEndTime_locator = (By.XPATH,tenderFileEndTime)
    applybeginTime_locator = (By.XPATH,applybeginTime)
    applyEndTime_locator = (By.XPATH,applyEndTime)
    quizEndTime_locator = (By.XPATH,quizEndTime)
    answerEndTime_locator = (By.XPATH,answerEndTime)
    bidFileEndTime_locator = (By.XPATH,bidFileEndTime)
    bidOpenTime_locator = (By.XPATH,bidOpenTime)
    tenderFileCost_locator = (By.XPATH,tenderFileCost)
    marginPaymentMethod_locator = (By.XPATH,marginPaymentWay)
    EVE_locator = (By.XPATH,EVE)
    offlinePayment_locator = (By.XPATH,offlinePayment)
    EVE_or_offlinePayment_locator = (By.XPATH,EVE_or_offlinePayment)
    marginSum_locator = (By.XPATH,marginSum)
    marginEndTime_locator = (By.XPATH,marginEndTime)
    tenderNotice_locator = (By.XPATH,tenderNotice)
    tenderFile_locator = (By.XPATH,tenderFile)
    saveButton_locator = (By.XPATH,saveButton)



    def addTenderProject_click(self):#点击新增招标项目
        self.click(self.addTenderProjectButton_locator)

    def projectNumber_send_keys(self):#输入项目编号
        projectNumber = self.get_nowTime_formatting()
        self.send_keys(self.projectNumber_locator,projectNumber)
        return projectNumber
    def projectName_send_keys(self):#输入项目名称
        self.send_keys(self.projectName_locator,"测试项目"+self.get_nowTime_formatting())
        # self.send_keys(self.projectName_locator,"工程委托线下")

    def projectAuditNumber_send_keys(self):#输入项目审批文号
        self.send_keys(self.projectAuditNumber_locator,"项目审批文号342300")

    def InvestprojectUnicode_send_keys(self):#投资项目统一代码
        self.send_keys(self.InvestprojectUnicode_locator,"2983798236232")

    def tenderType_click(self):#点击招标类型
        self.click(self.tenderType_locator)

    def build_click(self):#点击施工
        self.click(self.build_locator)

    def projectType_click(self):#点击项目类型
        self.click(self.projectType_locator)

    def houseBuild_click(self):#点击房屋建设
        self.click(self.houseBuild_locator)

    def tenderWay_click(self):#点击招标方式
        self.click(self.tenderWay_locator)

    def openTender_click(self):#点击公开招标
        self.click(self.openTender_locator)

    def inviteTender_click(self):#点击邀请招标
        self.click(self.inviteTender_locator)

    def inviteBid_click(self):#点击邀请投标人按钮
        self.click(self.inviteBid_locator)

    def enterpriseInput_send_keys(self,enterpriseName):#输入企业名称
        self.send_keys(self.enterpriseInput_locator,enterpriseName)

    def find_click(self):#点击查找企业按钮
        self.click(self.find_locator)

    def add_click(self):#点击添加企业
        self.click(self.add_locator)

    def close_click(self):#点击关闭
        self.click(self.close_locator)

    def addEnterprise(self,number,enterpriseName):#添加投标人企业
        for i in range(number):
            self.js_xpath_removeAttribute(self.enterpriseInput_locator)
            time.sleep(0.2)
            self.enterpriseInput_send_keys(enterpriseName=enterpriseName[i])#输入企业名称
            time.sleep(0.1)
            self.find_click()#点击查找
            self.add_click()#点击添加企业

    def tenderOrganizationType_click(self):#点击招标组织方式
        self.click(self.tenderOrganizationType_locator)

    def oneselfTender_click(self):#点击自主招标
        self.click(self.oneselfTender_locator)

    def entrustTender_click(self):#委托招标
        self.click(self.entrustTender_locator)

    def projectPlace_send_keys(self):#输入项目地址
        self.send_keys(self.projectPlace_locator,"江西省九江市濂溪县")

    def projectPlace_click(self):#点击项目地址
        self.click(self.projectPlace_locator)

    def projectPrice_send_keys(self):#输入项目估算价
        self.send_keys(self.projectPrice_locator,"120.12")

    def projectDate_send_keys(self):#输入工期
        self.send_keys(self.projectDate_locator,"120")

    def tenderLinkMan_send_keys(self):#输入招标联系人
        self.send_keys(self.tenderLinkMan_locator,"蟹老板")

    def tenderLinkManNumber_send_keys(self):#输入招标联系人号码
        self.send_keys(self.tenderLinkManNumber_locator,"15212345678")

    def linkPlace_send_keys(self):#输入联系地址
        self.send_keys(self.linkPlace_locator,"江西省九江市濂溪县")

    def tenderGency_click(self):#点击招标代理
        self.click(self.tenderGency_locator)

    def input_enterprise_send_keys(self):#输入招标代理企业信息
        self.send_keys(self.input_enterprise_locator,'甘肃省胸补声蕊秘咨询股份有限公司')

    def search_click(self):#点击搜索
        self.click(self.search_locator)

    def selectTenderGency_click(self):#选择招标代理
        self.click(self.selectTenderGency_locator)

    def sectionNumber_send_keys(self):#输入标段编号
        self.send_keys(self.sectionNumber_locator,"20230224345642312")

    def sectionName_send_keys(self):#输入标段名称
        self.send_keys(self.sectionName_locator,"标段名称173634")

    def tenderFileBeginTime_send_keys(self):#点击招标文件领取开始时间
        self.send_keys(self.tenderFileBeginTime_locator,self.time1)

    def tenderFileEndTime_send_keys(self):#输入招标文件截止时间
        self.send_keys(self.tenderFileEndTime_locator,self.get_nowtime(self.addtime))

    def applyBeginTime_send_keys(self):#输入报名开始时间
        self.send_keys(self.applybeginTime_locator,self.time1)

    def applyEndTime_send_keys(self):#输入报名截止时间
        self.send_keys(self.applyEndTime_locator,self.get_nowtime(self.addtime))

    def quizEndTime_send_keys(self):#提问截止时间
        self.send_keys(self.quizEndTime_locator,self.get_nowtime(self.addtime))

    def answerEndTime_send_keys(self):#答疑截止时间
        self.send_keys(self.answerEndTime_locator,self.get_nowtime(self.addtime))

    def bidFileEndTime_send_keys(self):#投标文件递交截止时间
        self.send_keys(self.bidFileEndTime_locator,self.get_nowtime(self.addtime))

    def bidOpenTime_send_keys(self):#开标时间
        self.send_keys(self.bidOpenTime_locator,self.get_nowtime(self.addtime))

    def tenderFileCost_send_keys(self):#招标文件费
        self.send_keys(self.tenderFileCost_locator,"0")

    def marginPaymentWay_click(self):#点击保证金缴纳方式
        self.click(self.marginPaymentMethod_locator)

    def offlinePayment_click(self):#点击线下缴纳
        self.click(self.offlinePayment_locator)

    def EVE_click(self):#点击保函申请
        self.click(self.EVE_locator)

    def EVE_or_offlinePayment_click(self):#选择线上或者线下
        self.click(self.EVE_or_offlinePayment_locator)

    def marginSum_send_keys(self):#保证金金额
        self.send_keys(self.marginSum_locator,"120.12")

    def marginEndTime_send_keys(self):#保证金缴纳截止时间
        self.send_keys(self.marginEndTime_locator,self.get_nowtime(self.addtime))

    def tenderNotice_click(self):#点击招标公告
        self.click(self.tenderNotice_locator)

    # def tenderNotice_send_keys(self):#上传招标公告
    #     self.send_keys(self.tenderNotice_locator,"D:\\1.png")

    def tenderFile_click(self):#上传招标文件
        self.click(self.tenderFile_locator)


    def saveButton_click(self):#点击保存
        self.click(self.saveButton_locator)

#政采项目

    def purchaseType_click(self):#采购类型
        self.click(self.purchaseType_locator)

    def purchaseBuild_click(self):#建筑材料
        self.click(self.purchaseBuild_locator)

    def purchaseWay_click(self):#采购方式
        self.click(self.purchaseWay_locator)

    def purchasePrice_send_keys(self):#采购预算
        self.send_keys(self.purchasePrice_locator,"120.12")




