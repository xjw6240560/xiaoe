from selenium.webdriver.common.by import By
from xiaoeXapth_package.deal_or_bidOpen.home_page_or_workbench import Home_page_or_workbench
from xiaoeXapth_package.deal_or_bidOpen.login_registerORselect_role import LoginOrRole
from base.base import Base
from base.mysql import Mysql
import traceback
import time
import random


class CreateProjectMethod(Base):
    home_page_or_workbench = Home_page_or_workbench()
    loginOrRole = LoginOrRole()
    base = Base()
    mysql = Mysql()
    addTime = 20
    addTenderProjectButton = "//div[contains(text(),'招标项目')]/../following-sibling::div/div/div/div/div/button//span[contains(text(),'新增项目')]"  # 新增招标项目
    projectNumber = "//div[contains(text(),'招标项目编号')]/following-sibling::div/div/div/div/input"  # 项目编号
    projectName = "//div[contains(text(),'招标项目名称')]/following-sibling::div/div/div/div/input"  # 项目名称
    projectAuditNumber = "//div[contains(text(),'项目审批文号')]/following-sibling::div/div/div/div/input"  # 项目审批文号
    InvestProjectUnicode = "//div[contains(text(),'投资项目统一代码')]/following-sibling::div/div/div/div/input"  # 投资项目统一代码
    tenderType = "//div[contains(text(),'招标类型')]/following-sibling::div/div/div/div/div/input"  # 招标类型
    build = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'施工')]"  # 招标类型（施工）
    projectType = "//div[contains(text(),'项目类型')]/following-sibling::div/div/div/div/div/input"  # 项目类型
    houseBuild = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'房屋建筑')]"  # 项目类型（房屋建设）
    tenderWay = "//div[contains(text(),'招标方式')]/following-sibling::div/div/div/div/div/div/input"  # 招标方式
    openTender = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'公开招标')]"  # 招标方式（公开招标）
    inviteTender = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'邀请招标')]"  # 招标方式（邀请招标）
    competitionConsult = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'竞争性磋商')]"  # 竞争性磋商谈判
    competition_negotiate = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'竞争性谈判')]"  # 点击竞争性谈判
    single_source_procurement = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'单一来源采购')]"  # 点击单一来源采购
    inviteBid = "//div[contains(text(),'方式')]/following-sibling::div/div/div/div/button/span[contains(text(),'邀请投标人')]"  # 邀请投标人按钮
    consultApplyWay = "//div[contains(text(),'采购方式')]/./following-sibling::div/div/div/div/button[3]/span[contains(text(),'报名方式')]"  # 竞争性磋商报名方式
    talkApplyWay = "//div[contains(text(),'采购方式')]/./following-sibling::div/div/div/div/button[4]/span[contains(text(),'报名方式')]"  # 竞争性谈判报名方式
    public_registration = "//span[contains(text(),'选择方式：')]/following-sibling::div/label/span[2]/span[contains(text(),'公开报名')]"  # 公开报名
    invitation_unit = "//span[contains(text(),'选择方式：')]/following-sibling::div/label/span[2]/span[contains(text(),'邀请单位')]"  # 邀请单位
    choose_supplier = "//div[contains(text(),'采购方式')]/./following-sibling::div/div/div/div/button[2]/span[contains(text(),'选择供应商')]"  # 点击选择供应商
    enterpriseInput = "//input[@placeholder = '请输入关键词']"  # 企业输入框
    find = "//button//span[contains(text(),'查找')]"  # 查找
    add = "//div//span[contains(text(),'添加')]"  # 添加企业
    isApplyFee = "//div[contains(text(),'是否收取报名费')]/following-sibling::div/div/label//span[text()='否']"
    close = "//div/preceding-sibling::div[text()='×']"  # 点击关闭
    tenderOrganizationType = "//div[contains(text(),'招标组织方式')]/following-sibling::div/div/div/div/div/input"  # 招标组织方式
    oneselfTender = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'自主招标')]"  # 自主招标
    entrustTender = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'委托招标')]"  # 委托招标
    industryType = "//div[contains(text(),'项目行业分类')]/following-sibling::div/div/div/div/div/input"  # 项目行业分类
    industryType1 = "//div/div/div/ul/li/span[contains(text(),'农、林、牧、渔业')]"
    industryType2 = "//div/div/div/ul/li/span[contains(text(),'农业')]"
    province = "//div[contains(text(),'项目所在地区')]/following-sibling::div/div/div/div/div"  # 项目所在省地区
    provinceName = "//div/div/div/ul/li/span[contains(text(),'北京市')]/.."
    city = "//div[contains(text(),'项目所在地区')]/following-sibling::div//input[@placeholder='市']"  # 项目所在市地区
    cityName = "//div/div/div/ul/li/span[contains(text(),'东城区')]"
    noticeType = "//div[contains(text(),'公告类型')]/following-sibling::div/div/div/div/div/input"  # 公告类型
    noticeTypeName = "//div/div/div/ul/li/span[contains(text(),'招标公告')]"
    projectPush = "//div[contains(text(),'项目推送')]/following-sibling::div/div/div/div/label[2]"  # 项目推送
    isElectronic = '//div[contains(text(),"是否电子标")]/following-sibling::div/div/div/div/div/input'  # 是否是电子标
    platformElectronic = "//div/div/ul/li/span[contains(text(),'平台电子标')]"  # 平台电子标
    offlinePaper = "//div/div/ul/li/span[contains(text(),'线下纸质标')]"  # 线下纸质标
    quotationMethod = '//div[contains(text(),"报价方式")]/following-sibling::div/div/div/div/div/input'  # 报价方式
    amountQuotation = "//div/div/ul/li/span[contains(text(),'金额报价(元)')]"  # 金额报价(元)
    rateQuotation = "//div/div/ul/li/span[contains(text(),'费率报价(%)')]"  # 费率报价(%)
    projectPlace = "//div[contains(text(),'项目地点')]/following-sibling::div/div/div/div/input"  # 项目地点
    projectPrice = "//div[contains(text(),'项目估算价')]/following-sibling::div/div/div/div/input"  # 项目估算价
    projectDate = "//div[contains(text(),'工期')]/following-sibling::div/div/div/div/input"  # 工期
    tenderLinkMan = "//div[contains(text(),'招标人联系人')]/following-sibling::div/div/div/div/input"  # 招标联系人
    tenderMan = "//div[contains(text(),'招标人：')]/following-sibling::div/div/div/div/input"  # 输入招标人
    tenderManUnicode = "//div[contains(text(),'招标人统一信用代码')]/following-sibling::div/div/div/div/input"  # 招标人统一信用代码
    tenderManBank = "//div[contains(text(),'招标人银行开户行')]/following-sibling::div/div/div/div/input"  # 招标人银行开户行
    tenderManBankNumber = "//div[contains(text(),'招标人银行开户账号')]/following-sibling::div/div/div/div/input"  # 招标人银行开户账号
    agentLinkMan = "//div[contains(text(),'代理联系人：')]/following-sibling::div/div/div/div/input"  # 代理联系人
    agentLinkManPhone = "//div[contains(text(),'代理联系人联系号码')]/following-sibling::div/div/div/div/input"  # 代理联系人手机号
    agentLinkPlace = "//*[@id='main']/div/form/div[4]/div/div[2]/div/div[5]/div/div[2]/div/div/div[1]/input"  # 招标代理角色联系地址
    tenderLinkManNumber = "//div[contains(text(),'招标人联系号码')]/following-sibling::div/div/div/div/input"  # 招标联系人手机号
    linkPlace = "//*[@id='main']/div/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/div/input"  # 联系地址
    tenderAgency = "//div[contains(text(),'招标代理')]/following-sibling::div/div"  # 招标代理
    input_enterprise = "//span[contains(text(),'搜索')]/../preceding-sibling::div/input[@placeholder='请输入企业名称']"  # 输入招标代理企业名称
    search = "//span[contains(text(),'搜索')]"  # 点击搜索
    selectTenderAgency = "//span[contains(text(),'1')]/ancestor::td/following-sibling::td//span[contains(text(),'选择')]"  # 选择招标代理
    agencyLinkPlace = "//*[@id='main']/div/form/div[4]/div/div[2]/div/div[5]/div/div[2]/div/div/div/input"  # 代理联系地址
    agencyLinkMan = "//div[contains(text(),'代理联系人：')]/./following-sibling::div/div/div//input"  # 招标代理联系人
    agencyLinkManNumber = "//div[contains(text(),'代理联系人联系号码')]/./following-sibling::div/div/div//input"  # 代理联系人手机号
    sectionNumber = "//div[contains(text(),'标段编号')]/following-sibling::div/div/div/div/input"  # 标段编号
    sectionName = "//div[contains(text(),'标段名称')]/following-sibling::div/div/div/div/input"  # 标段名称
    tenderFileBeginTime = "//div[contains(text(),'招标文件领取开始时间')]/following-sibling::div/div/div/div/input"  # 招标文件领取开始时间
    tenderFileEndTime = "//div[contains(text(),'招标文件领取截止时间')]/following-sibling::div/div/div/div/input"  # 招标文件领取截止时间
    applyBeginTime = "//div[contains(text(),'报名开始时间')]/following-sibling::div/div/div/div/input"  # 报名开始时间
    applyEndTime = "//div[contains(text(),'报名截止时间')]/following-sibling::div/div/div/div/input"  # 报名截止时间
    quizEndTime = "//div[contains(text(),'质疑截止时间')]/following-sibling::div/div/div/div/input"  # 提问截止时间
    answerEndTime = "//div[contains(text(),'答疑截止时间')]/following-sibling::div/div/div/div/input"  # 答疑截止时间
    bidFileEndTime = "//div[contains(text(),'投标文件递交截止时间')]/following-sibling::div/div/div/div/input"  # 投标文件递交截止时间
    bidOpenTime = "//div[contains(text(),'开标时间')]/following-sibling::div/div/div/div/input"  # 开标时间
    tenderFileCost = "//div[contains(text(),'招标文件费')]/following-sibling::div/div/div/div/input"  # 招标文件费用
    marginPaymentWay = "//div[contains(text(),'保证金缴纳方式')]/following-sibling::div/div/div/div/div/input"  # 保证金缴纳方式
    EVE = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'电子保函')]"  # 保证金缴纳方式(电子保函)
    offlinePayment = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[text()='线下缴纳']"  # 保证金缴纳方式(线下缴纳)
    EVE_or_offlinePayment = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'电子保函或线下缴纳')]"  # 选择线上和线下
    more = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'...')]"
    marginSum = "//div[contains(text(),'保证金额')]/following-sibling::div/div/div/div/input"  # 保证金额
    marginEndTime = "//div[contains(text(),'保证金缴纳截止时间')]/following-sibling::div/div/div/div/input"  # 保证金缴纳截止日期
    tenderNotice = "//div[contains(text(),'招标公告')]/following-sibling::div/div/div/div/div/div/input"  # 上传招标公告
    tenderFile = "//div[contains(text(),'招标文件')]/following-sibling::div/div/div/div/div/div/input"  # 上传招标文件
    saveButton = "//button[@class='el-button aui-margin-l-40 el-button--primary']//span[contains(text(),'保 存')]"  # 点击保存

    # 采购
    purchaseType = "//div[contains(text(),'采购类型')]/following-sibling::div/div/div/div/div/input"  # 采购类型
    purchaseBuild = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'工程类')]"  # 采购类型(工程类)
    purchaseWay = "//div[contains(text(),'采购方式')]/following-sibling::div/div/div/div/div/div/input"  # 采购方式
    purchasePrice = "//div[contains(text(),'采购预算')]/following-sibling::div/div/div/div/input"  # 采购预算

    purchaseType_locator = (By.XPATH, purchaseType)
    purchaseBuild_locator = (By.XPATH, purchaseBuild)
    purchaseWay_locator = (By.XPATH, purchaseWay)
    purchasePrice_locator = (By.XPATH, purchasePrice)

    addTenderProjectButton_locator = (By.XPATH, addTenderProjectButton)
    projectNumber_locator = (By.XPATH, projectNumber)
    projectName_locator = (By.XPATH, projectName)
    projectAuditNumber_locator = (By.XPATH, projectAuditNumber)
    InvestProjectUnicode_locator = (By.XPATH, InvestProjectUnicode)
    tenderType_locator = (By.XPATH, tenderType)
    build_locator = (By.XPATH, build)
    projectType_locator = (By.XPATH, projectType)
    houseBuild_locator = (By.XPATH, houseBuild)
    tenderWay_locator = (By.XPATH, tenderWay)

    isElectronic_locator = (By.XPATH, isElectronic)
    platformElectronic_locator = (By.XPATH, platformElectronic)
    offlinePaper_locator = (By.XPATH, offlinePaper)
    quotationMethod_locator = (By.XPATH, quotationMethod)
    amountQuotation_locator = (By.XPATH, amountQuotation)
    rateQuotation_locator = (By.XPATH, rateQuotation)
    consultApplyWay_locator = (By.XPATH, consultApplyWay)
    talkApplyWay_locator = (By.XPATH, talkApplyWay)
    public_registration_locator = (By.XPATH, public_registration)
    invitation_unit_locator = (By.XPATH, invitation_unit)
    choose_supplier_locator = (By.XPATH, choose_supplier)
    competition_negotiate_locator = (By.XPATH, competition_negotiate)
    single_source_procurement_locator = (By.XPATH, single_source_procurement)
    openTender_locator = (By.XPATH, openTender)
    inviteTender_locator = (By.XPATH, inviteTender)
    inviteBid_locator = (By.XPATH, inviteBid)
    enterpriseInput_locator = (By.XPATH, enterpriseInput)
    find_locator = (By.XPATH, find)
    add_locator = (By.XPATH, add)
    more_locator = (By.XPATH, more)
    close_locator = (By.XPATH, close)
    isApplyFee_locator = (By.XPATH, isApplyFee)
    tenderMan_locator = (By.XPATH, tenderMan)
    tenderManUnicode_locator = (By.XPATH, tenderManUnicode)
    tenderManBank_locator = (By.XPATH, tenderManBank)
    tenderManBankNumber_locator = (By.XPATH, tenderManBankNumber)
    agentLinkMan_locator = (By.XPATH, agentLinkMan)
    agentLinkManPhone_locator = (By.XPATH, agentLinkManPhone)
    agentLinkPlace_locator = (By.XPATH, agentLinkPlace)
    competitionConsult_locator = (By.XPATH, competitionConsult)
    tenderOrganizationType_locator = (By.XPATH, tenderOrganizationType)
    oneselfTender_locator = (By.XPATH, oneselfTender)
    entrustTender_locator = (By.XPATH, entrustTender)
    projectPlace_locator = (By.XPATH, projectPlace)
    projectPrice_locator = (By.XPATH, projectPrice)
    projectDate_locator = (By.XPATH, projectDate)
    tenderLinkMan_locator = (By.XPATH, tenderLinkMan)
    tenderLinkManNumber_locator = (By.XPATH, tenderLinkManNumber)
    linkPlace_locator = (By.XPATH, linkPlace)
    tenderAgency_locator = (By.XPATH, tenderAgency)
    input_enterprise_locator = (By.XPATH, input_enterprise)
    search_locator = (By.XPATH, search)
    selectTenderAgency_locator = (By.XPATH, selectTenderAgency)
    agencyLinkPlace_locator = (By.XPATH, agencyLinkPlace)
    agencyLinkMan_locator = (By.XPATH, agencyLinkMan)
    agencyLinkManNumber_locator = (By.XPATH, agencyLinkManNumber)

    sectionNumber_locator = (By.XPATH, sectionNumber)
    sectionName_locator = (By.XPATH, sectionName)
    tenderFileBeginTime_locator = (By.XPATH, tenderFileBeginTime)
    tenderFileEndTime_locator = (By.XPATH, tenderFileEndTime)
    applyBeginTime_locator = (By.XPATH, applyBeginTime)
    applyEndTime_locator = (By.XPATH, applyEndTime)
    quizEndTime_locator = (By.XPATH, quizEndTime)
    answerEndTime_locator = (By.XPATH, answerEndTime)
    bidFileEndTime_locator = (By.XPATH, bidFileEndTime)
    bidOpenTime_locator = (By.XPATH, bidOpenTime)
    tenderFileCost_locator = (By.XPATH, tenderFileCost)
    marginPaymentMethod_locator = (By.XPATH, marginPaymentWay)
    EVE_locator = (By.XPATH, EVE)
    offlinePayment_locator = (By.XPATH, offlinePayment)
    EVE_or_offlinePayment_locator = (By.XPATH, EVE_or_offlinePayment)
    marginSum_locator = (By.XPATH, marginSum)
    marginEndTime_locator = (By.XPATH, marginEndTime)
    tenderNotice_locator = (By.XPATH, tenderNotice)
    tenderFile_locator = (By.XPATH, tenderFile)
    saveButton_locator = (By.XPATH, saveButton)
    industryType_locator = (By.XPATH, industryType)
    industryType1_locator = (By.XPATH, industryType1)
    industryType2_locator = (By.XPATH, industryType2)
    province_locator = (By.XPATH, province)
    provinceName_locator = (By.XPATH, provinceName)
    city_locator = (By.XPATH, city)
    cityName_locator = (By.XPATH, cityName)
    noticeType_locator = (By.XPATH, noticeType)
    noticeTypeName_locator = (By.XPATH, noticeTypeName)
    projectPush_locator = (By.XPATH, projectPush)

    def addTenderProject_click(self):  # 点击新增招标项目
        self.click(self.addTenderProjectButton_locator)

    def projectNumber_send_keys(self):  # 输入项目编号
        projectNumber = self.get_nowTime_formatting()
        self.send_keys(self.projectNumber_locator, projectNumber)
        return projectNumber

    def industryType_click(self):
        self.click(self.industryType_locator)

    def industryType1_click(self):
        self.click(self.industryType1_locator)

    def industryType2_click(self):
        self.click(self.industryType2_locator)

    def province_click(self):
        self.click(self.province_locator)

    def provinceName_click(self):
        self.click(self.provinceName_locator)

    def city_click(self):
        self.click(self.city_locator)

    def cityName_click(self):
        self.click(self.cityName_locator)

    def noticeType_click(self):
        self.click(self.noticeType_locator)

    def noticeTypeName_click(self):
        self.click(self.noticeTypeName_locator)

    def projectPush_click(self):
        self.click(self.projectPush_locator)

    def getProjectType(self, projectType):  # 项目类型
        match projectType:
            case "engineering":
                return '工程'
            case "purchase":
                return '政采'
            case _:
                self.logger.debugText(errorText=f'项目类型错误：{projectType}')

    def getTenderOrganizationType(self, tenderOrganizationType):  # 招标组织方式
        match tenderOrganizationType:
            case "0":
                return '自主'
            case "1":
                return '委托'
            case _:
                self.logger.debugText(errorText=f'招标组织方式：{tenderOrganizationType}')

    def getTenderWay(self, tenderWay):  # 招标方式
        match tenderWay:
            case 0:
                return '公开'
            case 1:
                return '邀请'
            case 2:
                return '竞争性磋商'
            case 3:
                return '竞争性谈判'
            case 4:
                return '单一采购来源'
            case _:
                self.logger.debugText(errorText=f'招标方式：{str(tenderWay)}')

    def projectName_send_keys(self, projectType, tenderOrganizationType, tenderWay):  # 输入项目名称
        projectTypeResult = self.getProjectType(projectType)
        tenderOrganizationTypeResult = self.getTenderOrganizationType(tenderOrganizationType)
        tenderWayResult = self.getTenderWay(tenderWay)
        projectName = projectTypeResult + tenderOrganizationTypeResult + tenderWayResult + '招标项目'
        if projectType == 'engineering' and tenderWay > 1:
            errorText = f'工程项目没有-{tenderWayResult}-招标方式'
            raise Exception(errorText)
        else:
            self.send_keys(self.projectName_locator, projectName + self.get_nowTime_formatting())

    def projectAuditNumber_send_keys(self):  # 输入项目审批文号
        self.send_keys(self.projectAuditNumber_locator, "项目审批文号342300")

    def InvestProjectUnicode_send_keys(self):  # 投资项目统一代码
        self.send_keys(self.InvestProjectUnicode_locator, "2983798236232")

    def isElectronic_click(self):  # 是否是电子标
        self.click(self.isElectronic_locator)

    def platformElectronic_click(self):  # 平台电子标
        self.click(self.platformElectronic_locator)

    def offlinePaper_click(self):  # 线下纸质标
        self.click(self.offlinePaper_locator)

    def quotationMethod_click(self):  # 报价方式
        self.click(self.quotationMethod_locator)

    def amountQuotation_click(self):  # 金额报价
        self.click(self.amountQuotation_locator)

    def rateQuotation_click(self):  # 费率报价
        self.click(self.rateQuotation_locator)

    def tenderType_click(self):  # 点击招标类型
        self.click(self.tenderType_locator)

    def build_click(self):  # 点击施工
        self.click(self.build_locator)

    def isApplyFee_click(self):  # 报名费
        self.click(self.isApplyFee_locator)

    def projectType_click(self):  # 点击项目类型
        self.click(self.projectType_locator)

    def houseBuild_click(self):  # 点击房屋建设
        self.click(self.houseBuild_locator)

    def tenderWay_click(self):  # 点击招标方式
        self.click(self.tenderWay_locator)

    def openTender_click(self):  # 点击公开招标
        self.click(self.openTender_locator)

    def inviteTender_click(self):  # 点击邀请招标
        self.click(self.inviteTender_locator)

    def competitionConsult_click(self):  # 竞争性磋商
        self.click(self.competitionConsult_locator)

    def consultApplyWay_click(self):  # 竞争性磋商报名方式
        self.click(self.consultApplyWay_locator)

    def competition_negotiate_click(self):  # 点击竞争性谈判
        self.click(self.competition_negotiate_locator)

    def talkApplyWay_click(self):  # 竞争性谈判报名方式
        self.click(self.talkApplyWay_locator)

    def single_source_procurement_click(self):  # 点击单一来源采购
        self.click(self.single_source_procurement_locator)

    def inviteBid_click(self):  # 点击邀请投标人按钮
        self.click(self.inviteBid_locator)

    def public_registration_click(self):  # 点击公开报名
        self.click(self.public_registration_locator)

    def invitation_unit_click(self):  # 点击邀请报名
        self.click(self.invitation_unit_locator)

    def enterpriseInput_send_keys(self, enterpriseName):  # 输入企业名称
        self.send_keys(self.enterpriseInput_locator, enterpriseName)

    def find_click(self):  # 点击查找企业按钮
        self.click(self.find_locator)

    def add_click(self):  # 点击添加企业
        self.click(self.add_locator)

    def close_click(self):  # 点击关闭
        self.click(self.close_locator)

    def choose_supplier_click(self):  # 点击选择供应商
        self.click(self.choose_supplier_locator)

    def addEnterprise(self, number, enterpriseName):  # 添加投标人企业
        for i in range(number):
            self.js_xpath_removeAttribute(self.enterpriseInput_locator)
            time.sleep(0.2)
            self.enterpriseInput_send_keys(enterpriseName=enterpriseName[i])  # 输入企业名称
            time.sleep(0.2)
            self.find_click()  # 点击查找
            self.add_click()  # 点击添加企业

    def tenderOrganizationType_click(self):  # 点击招标组织方式
        self.click(self.tenderOrganizationType_locator)

    def oneselfTender_click(self):  # 点击自主招标
        self.click(self.oneselfTender_locator)

    def entrustTender_click(self):  # 委托招标
        self.click(self.entrustTender_locator)

    def projectPlace_send_keys(self):  # 输入项目地址
        self.send_keys(self.projectPlace_locator, "福建省漳州市")

    def projectPlace_click(self):  # 点击项目地址
        self.click(self.projectPlace_locator)

    def projectPrice_send_keys(self):  # 输入项目估算价
        projectPrice = round(random.uniform(10000, 4000000), 2)
        self.send_keys(self.projectPrice_locator, projectPrice)

    def projectDate_send_keys(self):  # 输入工期
        self.send_keys(self.projectDate_locator, "120")

    def tenderLinkMan_send_keys(self):  # 输入招标联系人
        self.send_keys(self.tenderLinkMan_locator, "蟹老板")

    def tenderLinkManNumber_send_keys(self):  # 输入招标联系人号码
        self.send_keys(self.tenderLinkManNumber_locator, "15212345678")

    def linkPlace_send_keys(self):  # 输入联系地址
        self.send_keys(self.linkPlace_locator, "福建省漳州市")

    def agencyLinkPlace_send_keys(self):  # 输入代理联系地址
        self.send_keys(self.agencyLinkPlace_locator, '厦门市湖里区鼎丰财富中心')

    def agencyLinkMan_send_keys(self):  # 输入代理联系人
        self.send_keys(self.agencyLinkMan_locator, "谢先生")

    def agencyLinkManNumber_send_keys(self):  # 输入代理联系人手机号
        self.send_keys(self.agencyLinkManNumber_locator, '15212121212')

    def tenderAgency_click(self):  # 点击招标代理
        self.click(self.tenderAgency_locator)

    def input_enterprise_send_keys(self):  # 输入招标代理企业信息
        self.send_keys(self.input_enterprise_locator, Base.tenderAgentName)

    def search_click(self):  # 点击搜索
        self.click(self.search_locator)

    def selectTenderAgency_click(self):  # 选择招标代理
        self.click(self.selectTenderAgency_locator)

    def sectionNumber_send_keys(self):  # 输入标段编号
        self.send_keys(self.sectionNumber_locator, "20230224345642312")

    def sectionName_send_keys(self):  # 输入标段名称
        self.send_keys(self.sectionName_locator, "标段名称173634")

    def tenderFileBeginTime_send_keys(self):  # 点击招标文件领取开始时间
        self.send_keys(self.tenderFileBeginTime_locator, self.time1)

    def tenderFileEndTime_send_keys(self):  # 输入招标文件截止时间
        self.send_keys(self.tenderFileEndTime_locator, self.get_nowTime(self.addTime))

    def applyBeginTime_send_keys(self):  # 输入报名开始时间
        self.send_keys(self.applyBeginTime_locator, self.time1)

    def applyEndTime_send_keys(self):  # 输入报名截止时间
        self.send_keys(self.applyEndTime_locator, self.get_nowTime(self.addTime))

    def quizEndTime_send_keys(self):  # 提问截止时间
        self.send_keys(self.quizEndTime_locator, self.get_nowTime(self.addTime))

    def answerEndTime_send_keys(self):  # 答疑截止时间
        self.send_keys(self.answerEndTime_locator, self.get_nowTime(self.addTime))

    def bidFileEndTime_send_keys(self):  # 投标文件递交截止时间
        self.send_keys(self.bidFileEndTime_locator, self.get_nowTime(self.addTime))

    def bidOpenTime_send_keys(self):  # 开标时间
        self.send_keys(self.bidOpenTime_locator, self.get_nowTime(self.addTime))

    def tenderFileCost_send_keys(self):  # 招标文件费
        self.send_keys(self.tenderFileCost_locator, "0.01")

    def marginPaymentWay_click(self):  # 点击保证金缴纳方式
        self.click(self.marginPaymentMethod_locator)

    def offlinePayment_click(self):  # 点击线下缴纳
        self.click(self.offlinePayment_locator)

    def EVE_click(self):  # 点击保函申请
        self.click(self.EVE_locator)

    def EVE_or_offlinePayment_click(self):  # 选择线上或者线下
        self.click(self.EVE_or_offlinePayment_locator)

    def more_click(self):  # 点击更多
        self.click(self.more_locator)

    def marginSum_send_keys(self):  # 保证金金额
        self.send_keys(self.marginSum_locator, "10000")

    def marginEndTime_send_keys(self):  # 保证金缴纳截止时间
        self.send_keys(self.marginEndTime_locator, self.get_nowTime(self.addTime))

    def tenderNotice_send_keys(self):  # 点击招标公告
        self.js_xpath_modifyAttribute(self.tenderNotice_locator)  # 改变属性值
        self.send_keys(self.tenderNotice_locator, r'C:\Users\86176\Desktop\不同大小的文件和图片\招标文件.pdf')

    # def tenderNotice_send_keys(self):#上传招标公告
    #     self.send_keys(self.tenderNotice_locator,"D:\\1.png")

    def tenderFile_send_keys(self):  # 上传招标文件
        self.js_xpath_modifyAttribute(self.tenderFile_locator)  # 改变属性值
        time.sleep(0.5)
        self.send_keys(self.tenderFile_locator, r'C:\Users\86176\Desktop\不同大小的文件和图片\tender_file.xezf')

    def saveButton_click(self):  # 点击保存
        self.roll_bottom()  # 滑动到底部
        time.sleep(0.5)
        self.click(self.saveButton_locator)

    def perfectProjectMessage(self, role, projectNumber, projectType, tenderOrganizationType, tenderWay):  # 完善项目信息
        self.sectionNumber_send_keys()  # 输入标段编号
        self.sectionName_send_keys()  # 输入标段名称
        self.tenderFileBeginTime_send_keys()  # 输入招标文件领取开始时间
        self.projectPlace_click()  # 点击项目地址
        self.tenderFileEndTime_send_keys()  # 输入招标文件领取截止时间
        self.projectPlace_click()  # 点击项目地址
        self.applyBeginTime_send_keys()  # 输入报名开始时间
        self.projectPlace_click()  # 点击项目地址
        self.applyEndTime_send_keys()  # 输入报名截止时间
        self.projectPlace_click()  # 点击项目地址
        self.quizEndTime_send_keys()  # 输入提问截止时间
        self.projectPlace_click()  # 点击项目地址
        self.answerEndTime_send_keys()  # 输入答疑截止时间
        self.projectPlace_click()  # 点击项目地址
        self.bidFileEndTime_send_keys()  # 输入投标文件递交截止时间
        self.projectPlace_click()  # 点击项目地址
        self.bidOpenTime_send_keys()  # 输入开标时间
        self.projectPlace_click()  # 点击项目地址
        self.tenderFileCost_send_keys()  # 输入招标文件费用
        self.marginPaymentWay_click()  # 点击保证金缴纳方式
        self.marginPayment(self.marginApplyWay)  # （0 保函申请， 1 线上和线下， 2 线下）
        self.marginSum_send_keys()  # 输入保证金金额
        # self.isApplyFee_click()#点击是否缴纳报名费
        self.marginEndTime_send_keys()  # 输入保证金戒指递交时间
        self.tenderNotice_send_keys()  # 上传招标公告
        time.sleep(0.5)
        self.tenderFile_send_keys()  # 上传招标文件
        self.saveButton_click()  # 点击保存按钮
        time.sleep(1)
        errorText = self.get_text(self.alert_locator)
        commitAudit_result = self.find_element(self.home_page_or_workbench.commitAudit_locator, 3)  # 提交审核按钮，判断项目是否创建成功
        if commitAudit_result is not False:
            if role == '1':
                self.mysql.insert_projectData(projectNumber=projectNumber, projectType=projectType,
                                              tenderOrganizationType='1', tenderWay=tenderWay)  # 数据库创建项目
            elif role == '0':
                self.mysql.insert_projectData(projectNumber=projectNumber, projectType=projectType,
                                              tenderOrganizationType=tenderOrganizationType,
                                              tenderWay=tenderWay)  # 数据库创建项目
            self.logger.debugText(projectNumber, '项目添加完成！')
        else:
            self.logger.debugText(errorText=errorText)

    def addProjectMsg(self, isElectronic, quotationMethod):
        """招标人角色创建项目是需要维护的字段"""
        self.projectPlace_send_keys()  # 输入项目地址
        self.tenderLinkMan_send_keys()  # 输入联系人
        self.tenderLinkManNumber_send_keys()  # 输入联系人手机号
        self.linkPlace_send_keys()  # 输入联系地址
        self.projectAuditNumber_send_keys()  # 输入项目审批文号
        self.InvestProjectUnicode_send_keys()  # 投资项目统一代码
        self.industryType_click()  # 点击行业分类
        self.industryType1_click()  # 点击行业分类一级选项
        self.industryType2_click()  # 点击行业分类二级选项
        self.province_click()  # 点击省份下拉框
        self.provinceName_click()  # 选择省份名字
        self.city_click()  # 点击城市下拉框
        self.cityName_click()  # 选择城市
        self.noticeType_click()  # 点击公告类型下拉框
        self.noticeTypeName_click()  # 选择公告类型名字
        self.projectPush_click()  # 点击不推送项目
        self.isElectronic_click()  # 点击是否电子标
        self.select_isElectronic(isElectronic=isElectronic)  # 选择是否平台电子标和报价方式
        self.quotationMethod_click()  # 点击报价方式
        self.select_quotationMethod(quotationMethod=quotationMethod)  # 选择报价方式

    def select_isElectronic(self, isElectronic):  # 选择是否平台电子标和报价方式
        match isElectronic:
            case 0:
                self.platformElectronic_click()  # 点击平台电子标
            case 1:
                self.offlinePaper_click()  # 点击线下纸质标

    def select_quotationMethod(self, quotationMethod):  # 选择报价方式
        match quotationMethod:
            case 0:
                self.amountQuotation_click()  # 金额报价方式
            case 1:
                self.rateQuotation_click()  # 费率报价方式

    def marginPayment(self, status):  # 保证金缴纳
        self.more_click()  # 点击更多
        if status == 0:
            self.EVE_click()  # 点击保函申请
        elif status == 1:
            self.EVE_or_offlinePayment_click()  # 点击线上和线下
        elif status == 2:
            self.offlinePayment_click()  # 点击线下缴纳
        else:
            print('保证金缴纳状态错误，0保函申请，1线上和线下，2线下')

    # 政采项目

    def purchaseType_click(self):  # 采购类型
        self.click(self.purchaseType_locator)

    def purchaseBuild_click(self):  # 建筑材料
        self.click(self.purchaseBuild_locator)

    def purchaseWay_click(self):  # 采购方式
        self.click(self.purchaseWay_locator)

    def purchasePrice_send_keys(self):  # 采购预算
        projectPrice = round(random.uniform(10000, 4000000), 2)
        self.send_keys(self.purchasePrice_locator, projectPrice)

    def tenderMan_send_keys(self, tenderMan=base.tenderMan):  # 输入招标人
        self.send_keys(self.tenderMan_locator, tenderMan)

    def tenderManUnicode_send_keys(self, tenderManUnicode=base.tenderManUnicode):  # 招标人统一信用代码
        self.send_keys(self.tenderManUnicode_locator, tenderManUnicode)

    def tenderManBank_send_keys(self):  # 招标人银行开户行
        self.send_keys(self.tenderManBank_locator, '厦门建设银行湖里')

    def tenderManBankNumber_send_keys(self):  # 招标人银行开户账号
        self.send_keys(self.tenderManBankNumber_locator, '235346452123124')

    def agentLinkMan_send_keys(self):  # 代理联系人
        self.send_keys(self.agentLinkMan_locator, '罗女士')

    def agentLinkManPhone_send_keys(self):  # 代理联系人手机号
        self.send_keys(self.agentLinkManPhone_locator, '15222222222')

    def agentLinkPlace_send_keys(self):  # 招标代理角色联系地址
        self.send_keys(self.agentLinkPlace_locator, '江西省濂溪县桥头村')

    def selectApplyWay(self, applyWay):  # 竞争性磋商和竞争性谈判招标方式选择：0：公开，1：邀请
        match applyWay:
            case 0:
                self.consultApplyWay_click()  # 点击招标方式
                self.public_registration_click()  # 点击公开报名
                self.close_click()  # 点击关闭
            case 1:
                self.talkApplyWay_click()  # 点击招标方式
                self.invitation_unit_click()  # 点击邀请报名
                self.addEnterprise(number=4, enterpriseName=self.enterpriseName)
                self.close_click()  # 点击关闭
            case _:
                raise Exception(f'竞争性磋商和竞争性谈判招标方式选择：0：公开，1：邀请:-{applyWay}-')

    def tender_or_purchase_way(self, tenderWay, applyWay):  # 选择招标方式或者采购方式
        match tenderWay:
            case 0:  # 公开招标
                self.openTender_click()  # 点击公开招标
            case 1:  # 邀请招标
                self.inviteTender_click()  # 点击邀请招标
                self.inviteBid_click()  # 点击邀请投标人
                self.addEnterprise(number=4, enterpriseName=self.enterpriseName)
                self.close_click()  # 点击关闭
            case 2:  # 竞争性磋商
                self.competitionConsult_click()  # 点击竞争性磋商
                self.selectApplyWay(applyWay=applyWay)
            case 3:  # 竞争性谈判
                self.competition_negotiate_click()  # 点击竞争性谈判
                self.selectApplyWay(applyWay=applyWay)
            case 4:  # 单一采购来源
                self.single_source_procurement_click()
                self.choose_supplier_click()  # 点击选择供应商
                self.addEnterprise(number=1, enterpriseName=self.enterpriseName)
                self.close_click()  # 点击关闭
            case _:
                raise Exception(f'招标方式错误：-{str(tenderWay)}-')

    def tender_or_tenderAgent(self, role, projectNumber, projectType, tenderOrganizationType,
                              tenderWay, areaNo):  # 根据角色创建不同的项目 0 招标人 1招标代理
        if role == '0':
            self.tenderOrganizationType_click()  # 点击招标组织方式
            # 自主招标
            if tenderOrganizationType == "0":
                self.oneselfTender_click()  # 选择自主招标
                self.perfectProjectMessage(role, projectNumber, projectType, tenderOrganizationType,
                                           tenderWay)  # 完善项目信息
            # 委托招标
            elif tenderOrganizationType == "1":
                self.entrustTender_click()  # 委托招标
                self.tenderAgency_click()  # 点击招标代理
                time.sleep(0.3)
                self.input_enterprise_send_keys()  # 输入招标代理名称
                self.search_click()  # 点击搜索企业
                self.selectTenderAgency_click()  # 选择招标代理
                time.sleep(0.3)
                self.saveButton_click()  # 点击保存
                time.sleep(0.5)
                self.open_deal_url()
                self.loginOrRole.login(self.username1[2], self.password[1], areaNo=areaNo)  # 登入交易平台
                self.loginOrRole.tenderAgency_click()  # 点击招标人
                self.handle_skip(-1)  # 跳转句柄
                if projectType == 'engineering':
                    self.home_page_or_workbench.engineerBusiness_click()  # 点击工程业务
                    self.home_page_or_workbench.tenderProject_click()  # 点击招标项目
                elif projectType == 'purchase':
                    self.home_page_or_workbench.purchaseBusiness_click()  # 点击政采业务
                    self.home_page_or_workbench.purchaseTenderProject_click()  # 点击政采招标项目
                self.home_page_or_workbench.tender_edit_click(projectNumber=projectNumber)  # 招标代理点击编辑
                self.agencyLinkMan_send_keys()  # 输入代理联系人
                self.agencyLinkManNumber_send_keys()  # 输入代理联系人手机号
                time.sleep(0.5)
                self.agencyLinkPlace_send_keys()  # 输入代理联系地址
                self.perfectProjectMessage(role, projectNumber, projectType, tenderOrganizationType,
                                           tenderWay)  # 完善企业信息
            else:
                print("招标类型不符")
        elif role == '1':
            self.tenderMan_send_keys('建设集团有限公司')  # 输入招标人Base.tenderMan,'建设集团有限公司'
            self.tenderManUnicode_send_keys('sdfmsd3454654645')  # 招标人统一信用代码Base.tenderManUnicode,'sdfmsd3454654645
            self.tenderManBank_send_keys()  # 招标人银行开户行
            self.tenderManBankNumber_send_keys()  # 招标人银行开户账号
            self.agentLinkMan_send_keys()  # 代理联系人
            self.agentLinkManPhone_send_keys()  # 代理联系人手机号
            self.agentLinkPlace_send_keys()  # 招标代理角色联系地址
            self.perfectProjectMessage(role, projectNumber, projectType, tenderOrganizationType, tenderWay)  # 完善项目信息
