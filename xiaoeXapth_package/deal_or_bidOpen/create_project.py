from selenium.webdriver.common.by import By
from xiaoeXapth_package.deal_or_bidOpen.home_page_or_workbench import Home_page_or_workbench
from xiaoeXapth_package.deal_or_bidOpen.login_registerORselect_role import LoginORrole
from base.base import Base
import traceback
import time


class CreateProjectMethod(Base):
    home_page_or_workbench = Home_page_or_workbench()
    loginORrole = LoginORrole()
    base = Base()
    addtime = 12
    addTenderProjectButton = "//div[contains(text(),'招标项目')]/following-sibling::button//span[contains(text(),'新增招标项目')]"  # 新增招标项目
    projectNumber = "//label[contains(text(),'招标项目编号:')]/following-sibling::div/div/input"  # 项目编号
    projectName = "//label[contains(text(),'招标项目名称:')]/following-sibling::div/div/input"  # 项目名称
    projectAuditNumber = "//label[contains(text(),'项目审批文号:')]/following-sibling::div/div/input"  # 项目审批文号
    InvestprojectUnicode = "//label[contains(text(),'投资项目统一代码:')]/following-sibling::div/div/input"  # 投资项目统一代码
    tenderType = "//label[contains(text(),'招标类型:')]/following-sibling::div/div/div/input"  # 招标类型
    build = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'施工')]"  # 招标类型（施工）
    projectType = "//label[contains(text(),'项目类型:')]/following-sibling::div/div/div/input"  # 项目类型
    houseBuild = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'房屋建筑')]"  # 项目类型（房屋建设）
    tenderWay = "//label[contains(text(),'招标方式:')]/following-sibling::div/div/div/div/input"  # 招标方式
    openTender = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'公开招标')]"  # 招标方式（公开招标）
    inviteTender = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'邀请招标')]"  # 招标方式（邀请招标）
    competitionConsult = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'竞争性磋商')]"  # 竞争性磋商谈判
    competition_negotiate = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'竞争性谈判')]"  # 点击竞争性谈判
    single_source_procurement = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'单一来源采购')]"  # 点击单一来源采购
    inviteBid = "//label[contains(text(),'方式:')]/following-sibling::div/div/div/following-sibling::button/span[contains(text(),'邀请投标人')]"  # 邀请投标人按钮
    consultApplyWay = "//label[contains(text(),'方式:')]/following-sibling::div/div/div/following-sibling::button[3]/span[contains(text(),'报名方式')]"  # 竞争性磋商报名方式
    talkApplyWay = "//label[contains(text(),'方式:')]/following-sibling::div/div/div/following-sibling::button[4]/span[contains(text(),'报名方式')]"  # 竞争性谈判报名方式
    public_registration = "//span[contains(text(),'选择方式：')]/following-sibling::div/label/span[2]/span[contains(text(),'公开报名')]"  # 公开报名
    invitation_unit = "//span[contains(text(),'选择方式：')]/following-sibling::div/label/span[2]/span[contains(text(),'邀请单位')]"  # 邀请单位
    choose_supplier = "//label[contains(text(),'方式:')]/following-sibling::div/div/div/following-sibling::button/span[contains(text(),'选择供应商')]"  # 点击选择供应商
    enterpriseInput = "//input[@placeholder = '请输入关键词']"  # 企业输入框
    find = "//button//span[contains(text(),'查找')]"  # 查找
    add = "//div//span[contains(text(),'添加')]"  # 添加企业
    isApplyFee = "//label[contains(text(),'是否收取报名费')]/following-sibling::div/div/label//span[text()='否']"
    close = "//div/preceding-sibling::div[text()='×']"  # 点击关闭
    tenderOrganizationType = "//label[contains(text(),'招标组织方式:')]/following-sibling::div/div/div/input"  # 招标组织方式
    oneselfTender = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'自主招标')]"  # 自主招标
    entrustTender = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'委托招标')]"  # 委托招标
    projectPlace = "//label[contains(text(),'项目地点')]/following-sibling::div/div/input"  # 项目地点
    projectPrice = "//label[contains(text(),'项目估算价')]/following-sibling::div/div/input"  # 项目估算价
    projectDate = "//label[contains(text(),'工期')]/following-sibling::div/div/input"  # 工期
    tenderLinkMan = "//label[contains(text(),'招标人联系人')]/following-sibling::div/div/input"  # 招标联系人
    tenderMan = "//label[text()='招标人:']/following-sibling::div/div/input"  # 输入招标人
    tenderManUnicode = "//label[text()='招标人统一信用代码:']/following-sibling::div/div/input"  # 招标人统一信用代码
    tenderManBank = "//label[text()='招标人银行开户行:']/following-sibling::div/div/input"  # 招标人银行开户行
    tenderManBankNumber = "//label[text()='招标人银行开户账号:']/following-sibling::div/div/input"  # 招标人银行开户账号
    agentLinkMan = "//label[text()='代理联系人:']/following-sibling::div/div/input"  # 代理联系人
    agentLinkManPhone = "//div[contains(text(),'招标代理信息')]/../following-sibling::div/div/div[4]/div/div/div/input"  # 代理联系人手机号
    agentLinkPlace = "//div[contains(text(),'招标代理信息')]/../following-sibling::div/div/div[5]/div/div/div/input"  # 招标代理角色联系地址
    tenderLinkManNumber = "//label[contains(text(),'招标人联系号码:')]/following-sibling::div/div/input"  # 招标联系人手机号
    linkPlace = "//label[contains(text(),'联系地址:')]/following-sibling::div/div/input"  # 联系地址
    tenderGency = "//label[contains(text(),'招标代理:')]/following-sibling::div/div"  # 招标代理
    input_enterprise = "//span[contains(text(),'搜索')]/../preceding-sibling::div/input[@placeholder='请输入企业名称']"  # 输入招标代理企业名称
    search = "//span[contains(text(),'搜索')]"  # 点击搜索
    selectTenderGency = "//span[contains(text(),'1')]/ancestor::td/following-sibling::td//span[contains(text(),'选择')]"  # 选择招标代理
    gencyLinkPlace = "//label[contains(text(),'代理联系人')]//ancestor::div[2]//following-sibling::div[2]/div/div/div/input"  # 代理联系地址
    gencyLinkMan = "//label[text()='代理联系人:']/following-sibling::div/div[1]/input"  # 招标代理联系人
    gencyLinkManNumber = "//label[text()='代理联系人联系号码:']/following-sibling::div/div/input"  # 代理联系人手机号
    sectionNumber = "//label[contains(text(),'标段编号:')]/following-sibling::div/div/input"  # 标段编号
    sectionName = "//label[contains(text(),'标段名称:')]/following-sibling::div/div/input"  # 标段名称
    tenderFileBeginTime = "//label[contains(text(),'招标文件领取开始时间:')]/following-sibling::div/div/input"  # 招标文件领取开始时间
    tenderFileEndTime = "//label[contains(text(),'招标文件领取截止时间:')]/following-sibling::div/div/input"  # 招标文件领取截止时间
    applybeginTime = "//label[contains(text(),'报名开始时间:')]/following-sibling::div/div/input"  # 报名开始时间
    applyEndTime = "//label[contains(text(),'报名截止时间:')]/following-sibling::div/div/input"  # 报名截止时间
    quizEndTime = "//label[contains(text(),'提问截止时间:')]/following-sibling::div/div/input"  # 提问截止时间
    answerEndTime = "//label[contains(text(),'答疑截止时间:')]/following-sibling::div/div/input"  # 答疑截止时间
    bidFileEndTime = "//label[contains(text(),'投标文件递交截止时间:')]/following-sibling::div/div/input"  # 投标文件递交截止时间
    bidOpenTime = "//label[contains(text(),'开标时间:')]/following-sibling::div/div/input"  # 开标时间
    tenderFileCost = "//label[contains(text(),'招标文件费')]/following-sibling::div/div/input"  # 招标文件费用
    marginPaymentWay = "//label[contains(text(),'保证金缴纳方式:')]/following-sibling::div/div/div/input"  # 保证金缴纳方式
    EVE = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'电子保函')]"  # 保证金缴纳方式(电子保函)
    offlinePayment = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[text()='线下缴纳']"  # 保证金缴纳方式(线下缴纳)
    EVE_or_offlinePayment = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'电子保函或线下缴纳')]"  # 选择线上和线下
    more = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'...')]"
    marginSum = "//label[contains(text(),'保证金额')]/following-sibling::div/div/input"  # 保证金额
    marginEndTime = "//label[contains(text(),'保证金缴纳截止时间:')]/following-sibling::div/div/input"  # 保证金缴纳截止日期
    tenderNotice = "//label[contains(text(),'招标公告:')]/following-sibling::div/div/div/div/input"  # 上传招标公告
    tenderFile = "//label[contains(text(),'招标文件:')]/following-sibling::div/div/div/div/input"  # 上传招标文件
    saveButton = "//button[@class='el-button aui-margin-l-40 el-button--primary']//span[contains(text(),'保 存')]"  # 点击保存

    # 采购
    purchaseType = "//label[contains(text(),'采购类型:')]/following-sibling::div/div/div/input"  # 采购类型
    purchaseBuild = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li//span[contains(text(),'工程类')]"  # 采购类型(工程类)
    purchaseWay = "//label[contains(text(),'采购方式:')]/following-sibling::div/div/div/div/input"  # 采购方式
    purchasePrice = "//label[contains(text(),'采购预算')]/following-sibling::div/div/input"  # 采购预算

    purchaseType_locator = (By.XPATH, purchaseType)
    purchaseBuild_locator = (By.XPATH, purchaseBuild)
    purchaseWay_locator = (By.XPATH, purchaseWay)
    purchasePrice_locator = (By.XPATH, purchasePrice)

    addTenderProjectButton_locator = (By.XPATH, addTenderProjectButton)
    projectNumber_locator = (By.XPATH, projectNumber)
    projectName_locator = (By.XPATH, projectName)
    projectAuditNumber_locator = (By.XPATH, projectAuditNumber)
    InvestprojectUnicode_locator = (By.XPATH, InvestprojectUnicode)
    tenderType_locator = (By.XPATH, tenderType)
    build_locator = (By.XPATH, build)
    projectType_locator = (By.XPATH, projectType)
    houseBuild_locator = (By.XPATH, houseBuild)
    tenderWay_locator = (By.XPATH, tenderWay)
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
    tenderGency_locator = (By.XPATH, tenderGency)
    input_enterprise_locator = (By.XPATH, input_enterprise)
    search_locator = (By.XPATH, search)
    selectTenderGency_locator = (By.XPATH, selectTenderGency)
    gencyLinkPlace_loactor = (By.XPATH, gencyLinkPlace)
    gencyLinkMan_locator = (By.XPATH, gencyLinkMan)
    gencyLinkManNumber_locator = (By.XPATH, gencyLinkManNumber)

    sectionNumber_locator = (By.XPATH, sectionNumber)
    sectionName_locator = (By.XPATH, sectionName)
    tenderFileBeginTime_locator = (By.XPATH, tenderFileBeginTime)
    tenderFileEndTime_locator = (By.XPATH, tenderFileEndTime)
    applybeginTime_locator = (By.XPATH, applybeginTime)
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

    def addTenderProject_click(self):  # 点击新增招标项目
        self.click(self.addTenderProjectButton_locator)

    def projectNumber_send_keys(self):  # 输入项目编号
        projectNumber = self.get_nowTime_formatting()
        self.send_keys(self.projectNumber_locator, projectNumber)
        return projectNumber

    def projectName_send_keys(self, projectType, tenderOrganizationType, tenderWay):  # 输入项目名称
        if projectType == "engineering":
            if tenderOrganizationType == "0":
                if tenderWay == 0:
                    self.send_keys(self.projectName_locator, "工程自主公开招标项目" + self.get_nowTime_formatting())
                elif tenderWay == 1:
                    self.send_keys(self.projectName_locator, "工程自主邀请招标项目" + self.get_nowTime_formatting())
                else:
                    print("招标方式不正确：" + str(tenderWay))
            elif tenderOrganizationType == "1":
                if tenderWay == 0:
                    self.send_keys(self.projectName_locator, "工程委托公开招标项目" + self.get_nowTime_formatting())
                elif tenderWay == 1:
                    self.send_keys(self.projectName_locator, "工程委托邀请招标项目" + self.get_nowTime_formatting())
                else:
                    print("招标方式不正确：" + str(tenderWay))
            else:
                print("招标组织方式不正确：" + str(tenderOrganizationType))
        elif projectType == "purchase":
            if tenderOrganizationType == "0":
                if tenderWay == 0:
                    self.send_keys(self.projectName_locator, "政采自主公开招标项目" + self.get_nowTime_formatting())
                elif tenderWay == 1:
                    self.send_keys(self.projectName_locator, "政采自主邀请招标项目" + self.get_nowTime_formatting())
                elif tenderWay == 2:
                    self.send_keys(self.projectName_locator,
                                   "政采自主竞争性磋商招标项目" + self.get_nowTime_formatting())
                elif tenderWay == 3:
                    self.send_keys(self.projectName_locator,
                                   "政采自主竞争性谈判招标项目" + self.get_nowTime_formatting())
                elif tenderWay == 4:
                    self.send_keys(self.projectName_locator,
                                   "政采自主单一采购来源招标项目" + self.get_nowTime_formatting())
                else:
                    print("招标方式不正确：" + str(tenderWay))
            elif tenderOrganizationType == "1":
                if tenderWay == 0:
                    self.send_keys(self.projectName_locator, "政采委托公开招标项目" + self.get_nowTime_formatting())
                elif tenderWay == 1:
                    self.send_keys(self.projectName_locator, "政采委托邀请招标项目" + self.get_nowTime_formatting())
                elif tenderWay == 2:
                    self.send_keys(self.projectName_locator,
                                   "政采委托竞争性磋商招标项目" + self.get_nowTime_formatting())
                elif tenderWay == 3:
                    self.send_keys(self.projectName_locator,
                                   "政采委托竞争性谈判招标项目" + self.get_nowTime_formatting())
                elif tenderWay == 4:
                    self.send_keys(self.projectName_locator,
                                   "政采委托单一采购来源招标项目" + self.get_nowTime_formatting())
                else:
                    print("招标方式不正确：" + str(tenderWay))
            else:
                print("招标组织方式不正确：" + tenderOrganizationType)
        else:
            print("项目类型不正确！")

    def projectAuditNumber_send_keys(self):  # 输入项目审批文号
        self.send_keys(self.projectAuditNumber_locator, "项目审批文号342300")

    def InvestprojectUnicode_send_keys(self):  # 投资项目统一代码
        self.send_keys(self.InvestprojectUnicode_locator, "2983798236232")

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
        self.send_keys(self.projectPrice_locator, "15684000")

    def projectDate_send_keys(self):  # 输入工期
        self.send_keys(self.projectDate_locator, "120")

    def tenderLinkMan_send_keys(self):  # 输入招标联系人
        self.send_keys(self.tenderLinkMan_locator, "蟹老板")

    def tenderLinkManNumber_send_keys(self):  # 输入招标联系人号码
        self.send_keys(self.tenderLinkManNumber_locator, "15212345678")

    def linkPlace_send_keys(self):  # 输入联系地址
        self.send_keys(self.linkPlace_locator, "福建省漳州市")

    def gencyLinkPlace_send_keys(self):  # 输入代理联系地址
        self.send_keys(self.gencyLinkPlace_loactor, '厦门市湖里区鼎丰财富中心')

    def gencyLinkMan_send_keys(self):  # 输入代理联系人
        self.send_keys(self.gencyLinkMan_locator, "谢先生")

    def gencyLinkManNumber_send_keys(self):  # 输入代理联系人手机号
        self.send_keys(self.gencyLinkManNumber_locator, '15212121212')

    def tenderGency_click(self):  # 点击招标代理
        self.click(self.tenderGency_locator)

    def input_enterprise_send_keys(self):  # 输入招标代理企业信息
        if Base.environment == "正式":
            self.send_keys(self.input_enterprise_locator, '厦门城市开发建设有限公司')
        elif Base.environment == "测试":
            self.send_keys(self.input_enterprise_locator, '甘肃省胸补声蕊秘咨询股份有限公司')

    def search_click(self):  # 点击搜索
        self.click(self.search_locator)

    def selectTenderGency_click(self):  # 选择招标代理
        self.click(self.selectTenderGency_locator)

    def sectionNumber_send_keys(self):  # 输入标段编号
        self.send_keys(self.sectionNumber_locator, "20230224345642312")

    def sectionName_send_keys(self):  # 输入标段名称
        self.send_keys(self.sectionName_locator, "标段名称173634")

    def tenderFileBeginTime_send_keys(self):  # 点击招标文件领取开始时间
        self.send_keys(self.tenderFileBeginTime_locator, self.time1)

    def tenderFileEndTime_send_keys(self):  # 输入招标文件截止时间
        self.send_keys(self.tenderFileEndTime_locator, self.get_nowtime(self.addtime))

    def applyBeginTime_send_keys(self):  # 输入报名开始时间
        self.send_keys(self.applybeginTime_locator, self.time1)

    def applyEndTime_send_keys(self):  # 输入报名截止时间
        self.send_keys(self.applyEndTime_locator, self.get_nowtime(self.addtime))

    def quizEndTime_send_keys(self):  # 提问截止时间
        self.send_keys(self.quizEndTime_locator, self.get_nowtime(self.addtime))

    def answerEndTime_send_keys(self):  # 答疑截止时间
        self.send_keys(self.answerEndTime_locator, self.get_nowtime(self.addtime))

    def bidFileEndTime_send_keys(self):  # 投标文件递交截止时间
        self.send_keys(self.bidFileEndTime_locator, self.get_nowtime(self.addtime))

    def bidOpenTime_send_keys(self):  # 开标时间
        self.send_keys(self.bidOpenTime_locator, self.get_nowtime(self.addtime))

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
        self.send_keys(self.marginEndTime_locator, self.get_nowtime(self.addtime))

    def tenderNotice_send_keys(self):  # 点击招标公告
        self.js_xpath_modifyAttribute(self.tenderNotice_locator)  # 改变属性值
        self.send_keys(self.tenderNotice_locator, r'C:\Users\86176\Desktop\不同大小的文件和图片\招标文件.pdf')

    # def tenderNotice_send_keys(self):#上传招标公告
    #     self.send_keys(self.tenderNotice_locator,"D:\\1.png")

    def tenderFile_send_keys(self):  # 上传招标文件
        self.js_xpath_modifyAttribute(self.tenderFile_locator)  # 改变属性值
        self.send_keys(self.tenderFile_locator, r'C:\Users\86176\Desktop\不同大小的文件和图片\tender_file.xezf')

    def saveButton_click(self):  # 点击保存
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
        self.tenderFile_send_keys()  # 上传招标文件
        self.saveButton_click()  # 点击保存按钮
        time.sleep(1)
        errorText = self.get_text(self.alert_locator)
        self.logger.debugText(errorText=errorText)
        if (errorText is not None) and (errorText.find("成功") < 0):
            self.logger.debugText(errorText=errorText)
        else:
            if role == '1':
                self.insert_projectData(projectNumber=projectNumber, projectType=projectType,
                                        tenderOrganizationType='1', tenderWay=tenderWay)  # 数据库创建项目
                self.logger.debugText(projectNumber=projectNumber, errorText='项目添加完成！')
            elif role == '0':
                self.insert_projectData(projectNumber=projectNumber, projectType=projectType,
                                        tenderOrganizationType=tenderOrganizationType, tenderWay=tenderWay)  # 数据库创建项目
                self.logger.debugText(projectNumber, '项目添加完成！')

    def insert_projectData(self, projectNumber, projectType, tenderOrganizationType, tenderWay):  # 插入项目数据
        self.connect_mysql()
        sql = 'insert into project (projectNumber,projectType,tenderOrganizationType,tenderWay) values(%s,%s,%s,%s)'
        try:
            self.insert_and_update_sql(sql, projectNumber, projectType, tenderOrganizationType, tenderWay)
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber=projectNumber, errorText=error)

    def marginPayment(self, status):  # 保证金缴纳
        try:
            if status == 0:
                self.EVE_click()  # 点击保函申请
            elif status == 1:
                self.EVE_or_offlinePayment_click()  # 点击线上和线下
            elif status == 2:
                self.offlinePayment_click()  # 点击线下缴纳
            else:
                print('保证金缴纳状态错误，0保函申请，1线上和线下，2线下')
        except:
            if status == 0:
                self.more_click()  # 点击更多
                self.EVE_click()  # 点击保函申请
            elif status == 1:
                self.more_click()  # 点击更多
                self.EVE_or_offlinePayment_click()  # 点击线上和线下
            elif status == 2:
                self.more_click()  # 点击更多
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
        self.send_keys(self.purchasePrice_locator, "120.12")

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

    def tender_or_purchase_way(self, tenderWay, applyWay, enterpriseNumber=3):  # 选择招标方式或者采购方式
        if tenderWay == 0:
            self.openTender_click()  # 点击公开招标
        elif tenderWay == 1:
            self.inviteTender_click()  # 点击邀请招标
            self.inviteBid_click()  # 点击邀请投标人
            self.addEnterprise(enterpriseNumber, enterpriseName=self.enterpriseName)
            self.close_click()  # 点击关闭
        elif tenderWay == 2:  # 竞争性磋商
            if applyWay == 0:
                self.competitionConsult_click()  # 点击竞争性磋商
                self.consultApplyWay_click()  # 点击招标方式
                self.public_registration_click()  # 点击公开报名
                self.close_click()  # 点击关闭
            elif applyWay == 1:
                self.competitionConsult_click()  # 点击竞争性磋商
                self.consultApplyWay_click()  # 点击招标方式
                self.invitation_unit_click()  # 点击邀请报名
                self.addEnterprise(enterpriseNumber, enterpriseName=self.enterpriseName)
                self.close_click()  # 点击关闭
            else:
                print("报名方式错误！！")
        elif tenderWay == 3:  # 点击竞争性谈判
            if applyWay == 0:
                self.competition_negotiate_click()  # 点击竞争性谈判
                time.sleep(1)
                self.talkApplyWay_click()  # 点击招标方式
                self.public_registration_click()  # 点击公开报名
                self.close_click()  # 点击关闭
            elif applyWay == 1:
                self.competition_negotiate_click()  # 点击竞争性谈判
                self.talkApplyWay_click()  # 点击招标方式
                self.invitation_unit_click()  # 点击邀请报名
                self.addEnterprise(enterpriseNumber, enterpriseName=self.enterpriseName)
                self.close_click()  # 点击关闭
        elif tenderWay == 4:  # 点击单一采购来源
            self.single_source_procurement_click()
            self.choose_supplier_click()  # 点击选择供应商
            self.addEnterprise(1, enterpriseName=self.enterpriseName)
            self.close_click()  # 点击关闭
        else:
            print("招标方式不正确：" + str(tenderWay))

    def tender_or_tenderAgent(self, role, projectNumber, projectType, tenderOrganizationType,
                              tenderWay):  # 根据角色创建不同的项目 0 招标人 1招标代理
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
                self.tenderGency_click()  # 点击招标代理
                time.sleep(0.3)
                self.input_enterprise_send_keys()  # 输入招标代理名称
                self.search_click()  # 点击搜索企业
                self.selectTenderGency_click()  # 选择招标代理
                time.sleep(0.5)
                self.saveButton_click()  # 点击保存
                time.sleep(0.5)
                self.open_deal_url()
                self.loginORrole.login(self.username1[2], self.password[1])  # 登入交易平台
                self.loginORrole.tenderAgency_click()  # 点击招标人
                self.handle_skip(-1)  # 跳转句柄
                if projectType == 'engineering':
                    self.home_page_or_workbench.engineerBusiness_click()  # 点击工程业务
                    self.home_page_or_workbench.tenderProject_click()  # 点击招标项目
                elif projectType == 'purchase':
                    self.home_page_or_workbench.purchaseBusiness_click()  # 点击政采业务
                    self.home_page_or_workbench.purchaseTenderProject_click()  # 点击政采招标项目
                self.home_page_or_workbench.tender_edit_click(projectNumber=projectNumber)  # 招标代理点击编辑
                self.gencyLinkMan_send_keys()  # 输入代理联系人
                self.gencyLinkManNumber_send_keys()  # 输入代理联系人手机号
                time.sleep(0.5)
                self.gencyLinkPlace_send_keys()  # 输入代理联系地址
                self.perfectProjectMessage(role, projectNumber, projectType, tenderOrganizationType,
                                           tenderWay)  # 完善企业信息
            else:
                print("招标类型不符")
        elif role == '1':
            self.tenderMan_send_keys('江西转移有限公司')  # 输入招标人'江西转移有限公司'
            self.tenderManUnicode_send_keys('ceshi1293123')  # 招标人统一信用代码'sdchu1293123'
            self.tenderManBank_send_keys()  # 招标人银行开户行
            self.tenderManBankNumber_send_keys()  # 招标人银行开户账号
            self.agentLinkMan_send_keys()  # 代理联系人
            self.agentLinkManPhone_send_keys()  # 代理联系人手机号
            self.agentLinkPlace_send_keys()  # 招标代理角色联系地址
            self.perfectProjectMessage(role, projectNumber, projectType, tenderOrganizationType, tenderWay)  # 完善项目信息
