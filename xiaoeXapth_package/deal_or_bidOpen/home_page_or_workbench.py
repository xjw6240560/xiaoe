from base.base import Base
import random
import time
from selenium.webdriver.common.by import By


class Home_page_or_workbench(Base):
    # 公用
    linkMan = "//label[contains(text(),'联系人')]/following-sibling::div/div/input"  # 输入联系人
    linkManNumber = "//label[contains(text(),'联系手机号')]/following-sibling::div/div/input"  # 输入联系手机号
    affirmApply = "//span[contains(text(),'确认报名')]"  # 点击确认报名
    auditAffirm = "//button//span[text()='取 消']/../following-sibling::button//span[contains(text(),'确 定')]"  # 审核确定
    marginPay = "//span[contains(text(),'投标阶段')]/../following-sibling::div[contains(text(),'保证金缴纳')]"  # 点击保证金缴纳
    offlinePay = "//div//span[contains(text(),'电子保函')]/../following-sibling::div//span[contains(text(),'线下缴纳')]"  # 点击线下缴纳
    applyEVE = "//div[contains(text(),'电子保函')]"  # 申请电子保函按钮
    back_margin = "//button//span[contains(text(),'返回')]"  # 点击返回
    agreement = "//span[contains(text(),'我已阅读并同意')]/preceding-sibling::label/span/span"  # 同意协议
    applyEVE_div = "//div[contains(text(),'您将通过')]/../preceding-sibling::div/div//span[text()='申请保函 ']"  # 点击申请保函
    receiptImg = "//div[contains(text(),'上传图片')]/./following-sibling::div/div/div/div/input"  # 点击图片上传回单
    saveReceipt = "//span[contains(text(),'上传保证金回单')]"  # 保存回单
    recallReceipt = "//span[contains(text(),'撤回保证金回单')]"  # 撤回回单
    recallAffirm = "//span[contains(text(),'确 定')]"
    returnButton = "//span[contains(text(),'返回')]"  # 点击返回
    error_p = "//div[@class='el-message el-message--error']/p"  # 获取错误p的地址
    warn_p = "//div[@class='el-message el-message--warn']/p"  # 获取警告p的地址
    warning_p = "//div[@class='el-message el-message--warning']/p"  # 获取警告p的地址
    uploadBidFile = "//span[contains(text(),'投标阶段')]/../following-sibling::div[contains(text(),'上传投标文件')]"  # 上传投标文件
    recallTenderFile = "//button/following-sibling::button/span[contains(text(),'撤回标书')]"
    tenderFileAffirm = "//button//span[contains(text(),'确 定')]"
    bidFileImg = "//span[contains(text(),'上传标书')]/./following-sibling::div/div/div/img"  # 点击图片上传投标文件
    bid_price = "//label[contains(text(),'投标价')]/./following-sibling::div/div/input"  # 输入投标价
    duration = "//label[contains(text(),'工期')]/./following-sibling::div/div/input"  # 输入工期
    quality = "//label[contains(text(),'质量标准')]/./following-sibling::div/div/input"  # 输入质量标准
    bid_file = "//label[contains(text(),'投标文件')]/./following-sibling::div/div/div/div/input"  # 投标文件
    saveBidFile = "//span[contains(text(),'提交投标文件')]"  # 保存投标文件
    commitAudit = "//span[contains(text(),'1')]/ancestor::td/following-sibling::td[5]/div/span[text()='提交审核']"  # 点击提交审核
    commitAudit_affirm = "//button//span[contains(text(),'确 定')]"  # 提交审核确定
    search_input = "//input[@placeholder='请输入项目编号/项目名称']"  # 搜索
    search_button = "//button/span[contains(text(),'搜索')]"
    openBidEntrance = "//span[contains(text(),'开标阶段')]/../following-sibling::div[contains(text(),'开标入口')]"  # 点击开标入口
    secondaryQuotation = "//span[contains(text(),'开标阶段')]/../following-sibling::div[contains(text(),'二次报价')]"  # 工作台点击二次报价
    secondaryQuotationInput = "//label[contains(text(),'二次报价')]/./following-sibling::div/div/div/input"  # 输入二次报价
    secondaryQuotationFile = "//label[contains(text(),'上传二次报价文件')]/./following-sibling::div/div/div/div/div/input"  # 上传响应性文件
    submitButton = "//button//span[contains(text(),'提交二次报价')]"  # 提交二次报价按钮
    recall_file = "//button//span[contains(text(),'撤回文件')]"  # 点击撤回文件按钮
    recall_affirm = "//button//span[contains(text(),'确 定')]"  # 撤回文件确定
    confirm_upload = "//span[contains(text(),'确认上传')]"
    evaluationBidEntrance = "//span[contains(text(),'开标阶段')]/../following-sibling::div[contains(text(),'评标入口')]"  # 点击评标入口
    enterpriseName = "//*[@id='header']/div[2]/div[3]/span"  # 企业名称
    quitLogin = "//li[contains(text(),'修改密码')]/./following-sibling::li[contains(text(),'退出登录')]"  # 退出登录

    linkMan_locator = (By.XPATH, linkMan)
    submitButton_locator = (By.XPATH, submitButton)
    recall_file_locator = (By.XPATH, recall_file)
    recall_affirm_locator = (By.XPATH, recall_affirm)
    linkManNumber_locator = (By.XPATH, linkManNumber)
    affirmApply_locator = (By.XPATH, affirmApply)
    auditAffirm_locator = (By.XPATH, auditAffirm)
    marginPay_locator = (By.XPATH, marginPay)
    offlinePay_locator = (By.XPATH, offlinePay)
    back_margin_locator = (By.XPATH, back_margin)
    receiptImg_locator = (By.XPATH, receiptImg)
    saveReceipt_locator = (By.XPATH, saveReceipt)
    recallReceipt_locator = (By.XPATH, recallReceipt)
    recallAffirm_locator = (By.XPATH, recallAffirm)
    returnButton_locator = (By.XPATH, returnButton)
    error_p_locator = (By.XPATH, error_p)
    warn_p_locator = (By.XPATH, warn_p)
    warning_p_locator = (By.XPATH, warning_p)
    recallTenderFile_locator = (By.XPATH, recallTenderFile)
    tenderFileAffirm_locator = (By.XPATH, tenderFileAffirm)
    uploadBidFile_locator = (By.XPATH, uploadBidFile)
    secondaryQuotationInput_locator = (By.XPATH, secondaryQuotationInput)
    bidFileImg_locator = (By.XPATH, bidFileImg)
    saveBidFile_locator = (By.XPATH, saveBidFile)
    commitAudit_locator = (By.XPATH, commitAudit)
    secondaryQuotation_locator = (By.XPATH, secondaryQuotation)
    secondaryQuotationFile_locator = (By.XPATH, secondaryQuotationFile)
    bid_price_locator = (By.XPATH, bid_price)
    duration_locator = (By.XPATH, duration)
    quality_locator = (By.XPATH, quality)
    confirm_upload_locator = (By.XPATH, confirm_upload)
    search_input_locator = (By.XPATH, search_input)
    search_button_locator = (By.XPATH, search_button)
    bid_file_locator = (By.XPATH, bid_file)
    commitAudit_affirm_locator = (By.XPATH, commitAudit_affirm)
    openBidEntrance_locator = (By.XPATH, openBidEntrance)
    evaluationBidEntrance_locator = (By.XPATH, evaluationBidEntrance)
    enterpriseName_locator = (By.XPATH, enterpriseName)
    quitLogin_locator = (By.XPATH, quitLogin)

    def commitAudit_click(self):  # 点击提交审核
        self.click(self.commitAudit_locator)

    def commitAudit_affirm_click(self):  # 点击提交审核确定
        self.click(self.commitAudit_affirm_locator)

    def linkMan_send_keys(self):  # 输入联系人
        self.send_keys(self.linkMan_locator, "谢先生")

    def linkManNumber_send_keys(self):  # 输入联系手机号
        self.send_keys(self.linkManNumber_locator, '15212345678')

    def affirmApply_click(self):  # 点击确认报名
        self.click(self.affirmApply_locator)

    def secondaryQuotationInput_send_keys(self):  # 输入投标价
        bidPrice = round(random.uniform(1000000, 4000000), 2)  # 产生一个两位小数的随机数
        self.send_keys(self.secondaryQuotationInput_locator, bidPrice)

    def tender_workbench_click(self, projectNumber):  # 招标人点击工作台
        workbenchButton = "//div[contains(text(),'" + str(
            projectNumber) + "')]/../following-sibling::td[6]/div/span[text()='工作台']"  # 点击工作台
        workbench_locator = (By.XPATH, workbenchButton)
        self.click(workbench_locator)

    def search_input_send_keys(self, projectNumber):  # 项目编号和项目名称输入框
        self.send_keys(self.search_input_locator, projectNumber)

    def search_button_click(self):  # 点击搜索按钮
        self.click(self.search_button_locator)

    def tender_edit_click(self, projectNumber):  # 招标人编辑
        edit = "//div[contains(text(),'" + str(
            projectNumber) + "')]/../following-sibling::td[4]/div/span[text()='编辑']"  # 点击编辑
        edit_locator = (By.XPATH, edit)
        self.click(edit_locator)

    def bid_workbench_click(self, projectNumber):  # 投标人点击工作台
        workbenchButton = "//div[contains(text(),'" + str(
            projectNumber) + "')]/../following-sibling::td[3]/div/span[text()='工作台']"  # 点击工作台
        workbench_locator = (By.XPATH, workbenchButton)
        return self.short_click(workbench_locator)

    def audit_click(self):  # 点击审核
        result = self.audit_choose(5)
        if result is False:
            self.audit_choose(6)

    def audit_choose(self, x):
        auditButton = "//div[contains(text(),'" + str(
            self.get_nowTime_formatting()) + "')]/../following-sibling::td[" + x + "]/div/span[text()='提交审核']"  # 点击提交审核
        audit_locator = (By.XPATH, auditButton)
        result = self.click(audit_locator)
        return result

    def auditAffirm_click(self):  # 点击审核确认
        self.click(self.auditAffirm_locator)

    def marginPay_click(self):  # 点击保证金缴纳
        self.click(self.marginPay_locator)

    def offlinePay_click(self):  # 点击线下缴纳
        self.click(self.offlinePay_locator)

    def margin_back_click(self):  # 线上和线下选择时的返回
        self.click(self.back_margin_locator)

    def receiptImg_send_keys(self):  # 点击上传回单图片
        self.js_xpath_modifyAttribute(self.receiptImg_locator)  # 改变class属性
        return self.short_send_keys(self.receiptImg_locator, r"C:\Users\86176\Desktop\不同大小的文件和图片\保证金.jpg")

    def saveReceipt_click(self):  # 点击保存回单
        self.click(self.saveReceipt_locator)

    def recallReceipt_click(self):  # 撤回回单
        self.click(self.recallReceipt_locator)

    def recallAffirm_click(self):  # 撤回确认
        self.click(self.recallAffirm_locator)

    def errorMessage_text(self, type='warn'):  # 获取错误提示错误类型
        global message
        if type == 'warn':
            message = self.get_text(self.warn_p_locator)
        elif type == 'error':
            message = self.get_text(self.error_p_locator)
        elif type == 'warning':
            message = self.get_text(self.warning_p_locator)
        else:
            print("错误类型不正确：" + type)
        return message

    def returnButton_click(self):  # 点击返回
        self.click(self.returnButton_locator)

    def uploadBidFile_click(self):  # 点击上传投标文件
        self.click(self.uploadBidFile_locator)

    def confirm_upload_click(self):  # 确认上传
        return self.click(self.confirm_upload_locator)

    def recallTenderFile_click(self):  # 点击撤回标书
        self.click(self.recallTenderFile_locator)

    def tenderFileAffirm_click(self):  # 撤回标书确定
        self.click(self.tenderFileAffirm_locator)

    def bidFileImg_click(self):  # 点击上传投标文件图片
        self.click(self.bidFileImg_locator)

    def bid_price_send_keys(self):  # 输入投标价
        price = round(random.uniform(1000000, 4000000),2)
        # price = 0
        time.sleep(0.3)
        self.send_keys(self.bid_price_locator, price)

    def duration_send_keys(self):  # 输入工期
        self.send_keys(self.duration_locator, 120)

    def quality_send_keys(self):  # 输入质量标准
        self.send_keys(self.quality_locator,
                       "温馨提示：填写的投标信息请确认与所上传的投标文件一致，投标文件递交时间截至之后无法进行撤回和修改")

    def bid_file_send_keys(self):  # 点击投标文件
        self.js_xpath_modifyAttribute(self.bid_file_locator)
        time.sleep(0.5)
        return self.send_keys(self.bid_file_locator, r"C:\Users\86176\Desktop\不同大小的文件和图片\深圳CA.xetf")

    def saveBidFile_click(self):  # 保存投标文件
        self.click(self.saveBidFile_locator)

    def openBidEntrance_click(self):  # 点击开标入口
        self.click(self.openBidEntrance_locator)
        time.sleep(0.1)

    def evaluationBidEntrance_click(self):  # 点击评标入口
        self.click(self.evaluationBidEntrance_locator)

    def secondaryQuotation_click(self):  # 点击二次报价按钮
        self.click(self.secondaryQuotation_locator)

    def secondaryQuotationFile_input_send_keys(self):  # 点击上传响应性文件
        self.js_xpath_modifyAttribute(self.secondaryQuotationFile_locator)
        self.send_keys(self.secondaryQuotationFile_locator, r"C:\Users\86176\Desktop\不同大小的文件和图片\招标文件.pdf")

    def engpriseName_move(self):  # 悬浮在企业名称位置
        self.move_mouse(self.enterpriseName_locator)

    def quitLogin_click(self):  # 点击退出登录
        self.click(self.quitLogin_locator)

    # 工程
    # engineerBusiness = "//*[@id='aside']/div[2]/ul/li[9]/div/span"  # 工程业务
    # tenderProject = "//*[@id='aside']/div[2]/ul/li[9]/ul/div/li/div"  # 招标项目(工程)
    # engineerTenderNotice = "//*[@id='aside']/div[2]/ul/li[9]/ul/div[1]/li/div"  # 招标公告（工程）
    # engineerTenderInvite = "//*[@id='aside']/div[2]/ul/li[9]/ul/div[2]/li/div"  # 投标邀请
    # engineerApplyProject = "//*[@id='aside']/div[2]/ul/li[9]/ul/div[3]/li/div"  # 报名项目
    engineerBusiness = "//div[@class='el-submenu__title']//span[text()='工程业务']"  # 工程业务
    tenderProject = "//span[contains(text(),'工程业务')]/../following-sibling::ul/descendant::div[contains(text(),'招标项目')]"  # 招标项目(工程)
    engineerTenderNotice = "//span[contains(text(),'工程业务')]/../following-sibling::ul/descendant::div[contains(text(),'招标公告')]"  # 招标公告（工程）
    engineerTenderInvite = "//span[contains(text(),'工程业务')]/../following-sibling::ul/descendant::div[contains(text(),'投标邀请')]"  # 投标邀请
    engineerApplyProject = "//span[contains(text(),'工程业务')]/../following-sibling::ul/descendant::div[contains(text(),'报名项目')]"  # 报名项目

    engineerTenderNotice_locator = (By.XPATH, engineerTenderNotice)
    engineerBusiness_locator = (By.XPATH, engineerBusiness)
    tenderProject_locator = (By.XPATH, tenderProject)
    engineerTenderInvite_locator = (By.XPATH, engineerTenderInvite)
    engineerApplyProject_locator = (By.XPATH, engineerApplyProject)

    def engineerBusiness_click(self):  # 点击工程业务
        self.click(self.engineerBusiness_locator)

    def engineerApplyProject_click(self):  # 点击报名项目
        self.click(self.engineerApplyProject_locator)

    def engineerTenderNotice_click(self):  # 点击招标公告(工程)
        self.click(self.engineerTenderNotice_locator)

    def engineerTenderInvite_click(self):  # 点击工程招标邀请
        self.click(self.engineerTenderInvite_locator)

    def tenderProject_click(self):  # 点击招标项目
        self.click(self.tenderProject_locator)

    # 采购
    # purchaseBusiness = "//*[@id='aside']/div[2]/ul/li[14]/div/span"  # 政采业务
    # purchaseTenderproject = "//*[@id='aside']/div[2]/ul/li[14]/ul/div/li/div"  # 招标项目(政采)
    # purchaseTenderNotice = "//*[@id='aside']/div[2]/ul/li[14]/ul/div[1]/li/div"  # 招标公告
    # purchaseTenderInvite = "//*[@id='aside']/div[2]/ul/li[14]/ul/div[2]/li/div"  # 投标邀请
    # purchaseApplyProject = "//*[@id='aside']/div[2]/ul/li[14]/ul/div[3]/li/div"
    purchaseBusiness = "//div[@class='el-submenu__title']//span[contains(text(),'政采业务')]"  # 政采业务
    purchaseTenderproject = "//span[contains(text(),'政采业务')]/../following-sibling::ul/descendant::div[contains(text(),'招标项目')]"  # 招标项目(政采)
    purchaseTenderNotice = "//span[contains(text(),'政采业务')]/../following-sibling::ul/descendant::div[contains(text(),'招标公告')]"  # 招标公告
    purchaseTenderInvite = "//span[contains(text(),'政采业务')]/../following-sibling::ul/descendant::div[contains(text(),'投标邀请')]"  # 投标邀请
    purchaseApplyProject = "//span[contains(text(),'政采业务')]/../following-sibling::ul/descendant::div[contains(text(),'报名项目')]"  # 报名项目

    purchaseBusiness_locator = (By.XPATH, purchaseBusiness)
    purchaseTenderProject_locator = (By.XPATH, purchaseTenderproject)
    purchaseTenderNotice_locator = (By.XPATH, purchaseTenderNotice)
    purchaseTenderInvite_locator = (By.XPATH, purchaseTenderInvite)
    purchaseApplyProject_locator = (By.XPATH, purchaseApplyProject)

    def purchaseTenderNotice_click(self):  # 点击招标公告（政采）
        self.click(self.purchaseTenderNotice_locator)

    def purchaseApplyProject_click(self):  # 点击报名项目（政采）
        self.click(self.purchaseApplyProject_locator)

    def purchaseTenderInvite_click(self):  # 点击政采邀请招标
        self.click(self.purchaseTenderInvite_locator)

    def select_apply(self, projectNumber, projectType, tenderWay, applyWay):  # 点击报名
        if projectType == "engineering":  # 工程
            self.engineerBusiness_click()  # 点击工程项目
            if tenderWay == 0:
                self.engineerTenderNotice_click()  # 点击招标公告
                return self.notice_apply_click(projectNumber)  # 点击报名按钮
            elif tenderWay == 1:
                self.engineerTenderInvite_click()  # 点击投标邀请
                return self.bid_apply_click(projectNumber)  # 点击报名
            else:
                print("招标方式输入错入！工程项目没有：" + str(tenderWay))
        elif projectType == "purchase":  # 政采
            self.purchaseBusiness_click()  # 点击采购项目
            if tenderWay in (0, 2, 3):
                if applyWay == 0:
                    self.purchaseTenderNotice_click()  # 点击招标公告（政采）
                    return self.notice_apply_click(projectNumber)  # 点击报名按钮
                elif applyWay == 1:
                    self.purchaseTenderInvite_click()  # 点击政采招标邀请
                    return self.bid_apply_click(projectNumber)  # 点击报名
                else:
                    self.logger.debugText(projectNumber=projectNumber,
                                          errorText='招标方式:' + str(tenderWay) + '或者报名方式' + str(
                                              applyWay) + '不符:')
            elif tenderWay in (1, 4):
                self.purchaseTenderInvite_click()  # 点击政采招标邀请
                return self.bid_apply_click(projectNumber)  # 点击报名
            else:
                self.logger.debugText(projectNumber=projectNumber,
                                      errorText='招标方式输入错误：' + str(tenderWay) + '，0表示公开招标，1表示邀请招标')
        else:
            print("项目类型错误" + projectType)

    def purchaseBusiness_click(self):  # 点击采购业务
        time.sleep(0.5)
        self.click(self.purchaseBusiness_locator)

    def purchaseTenderProject_click(self):  # 点击招标项目
        self.click(self.purchaseTenderProject_locator)

    def notice_apply_click(self, projectNumber):  # 招标公告报名
        applyButton = "//div[contains(text(),'" + str(
            projectNumber) + "')]/../following-sibling::td[6]/div/span[text()='报名']"  # 点击报名
        apply_locator = (By.XPATH, applyButton)  # 选择报名项目编号
        return self.short_click(apply_locator)

    def bid_apply_click(self, projectNumber):  # 投标邀请报名
        applyButton = "//div[contains(text(),'" + str(
            projectNumber) + "')]/../following-sibling::td[4]/div/span[text()='报名']"  # 点击报名
        apply_locator = (By.XPATH, applyButton)  # 选择报名项目编号
        return self.short_click(apply_locator)

    def select_tender_workbench(self, projectNumber, projectType):  # 招标人选择工作台
        if projectType == "engineer":
            # 工程
            self.engineerBusiness_click()  # 点击工程业务
            self.tenderProject_click()  # 点击招标项目
            self.tender_workbench_click(projectNumber)  # 点击项目对应的工作台
        elif projectType == "purchase":
            # 采购
            self.purchaseBusiness_click()  # 点击采购业务
            self.purchaseTenderProject_click()  # 点击招标项目
            self.tender_workbench_click(projectNumber)  # 点击项目对应的工作台
        else:
            print("招标类型不符" + projectType)

    def select_tender_edit(self, projectNumber, projectType):  # 招标人和招标代理选择编辑
        if projectType == "engineer":
            # 工程
            self.engineerBusiness_click()  # 点击工程业务
            self.tenderProject_click()  # 点击招标项目
            self.tender_edit_click(projectNumber)  # 点击项目对应的编辑
        elif projectType == "purchase":
            # 采购
            self.purchaseBusiness_click()  # 点击采购业务
            self.purchaseTenderProject_click()  # 点击招标项目
            self.tender_edit_click(projectNumber)  # 点击项目对应的编辑
        else:
            print("招标类型不符" + projectType)

    def select_bid_workbench(self, projectNumber, projectType, status):  # 投标人选择工作台
        # status 用于区分报名和签到时候需不需要选择项目这一栏
        if projectType == "engineering":
            # 工程
            if status == 1:
                self.engineerBusiness_click()  # 点击工程项目
            self.engineerApplyProject_click()  # 点击工程报名项目
        elif projectType == "purchase":
            # 采购
            if status == 1:
                self.purchaseBusiness_click()  # 点击采购项目
            self.purchaseApplyProject_click()  # 点击政采报名项目
        else:
            print("招标类型不符" + projectType)

        workbenchResult = self.bid_workbench_click(projectNumber)  # 点击项目对应的工作台
        if workbenchResult is False:  # 项目不在第一页
            self.search_input_send_keys(projectNumber=projectNumber)  # 输入项目编号
            self.search_button_click()  # 点击搜索
            result = self.bid_workbench_click(projectNumber)  # 点击项目对应的工作台
            if result is False:
                self.logger.debugText(projectNumber=projectNumber, errorText='未找到项目！')
                return result

    def submitButton_locator_click(self):  # 点击提交二次报价按钮
        self.click(self.submitButton_locator)

    def recall_file_click(self):  # 点击撤回文件按钮
        self.click(self.recall_file_locator)

    def recall_affirm_click(self):  # 撤回文件确定
        self.click(self.recall_affirm_locator)

    def magin_and_tenderfile(self, projectNumber, bidder, applynumber):  # 缴纳保证金和上传投标文件
        self.marginPay_click()  # 点击保证金缴纳
        self.offlinePay_click()  # 点击线下缴纳
        receiptImg_result = self.receiptImg_send_keys()  # 点击上传回单图片
        if receiptImg_result is None:  # 回单上传成功！
            time.sleep(0.5)
            self.saveReceipt_click()  # 点击保存回单
            text01 = self.get_text(self.alert_locator)
            self.logger.debugText(bidder=bidder, projectNumber=projectNumber, errorText='保证金缴纳:' + str(text01))
        elif receiptImg_result is False:  # 未找到上传回单按钮
            if self.find_element(locator=self.recallTenderFile_locator, timeout=2) is not False:
                self.logger.debugText(errorText='保证金已缴纳！')
        self.returnButton_click()  # 点击返回
        self.margin_back_click()  # 再次点击返回
        self.uploadBidFile_click()  # 点击上传投标文件
        bidFile_result = self.bid_file_send_keys()  # 上传投标文件
        if bidFile_result is None:
            self.bid_price_send_keys()  # 输入投标价
            self.duration_send_keys()  # 输入工期
            self.quality_send_keys()  # 输入质量标准
            self.saveBidFile_click()  # 提交投标文件
            text02 = self.get_text(self.alert_locator)
            self.logger.debugText(projectNumber=projectNumber, bidder=bidder,
                                  errorText='提交投标文件：' + str(text02))  # 打印错误信息
            self.confirm_upload_click()  # 点击确认上传
            text03 = self.get_text(self.alert_locator)  # 获取确认上传错误信息
            recallTenderFile_result = self.find_element(self.recallTenderFile_locator, 2)  # 撤回投标文件按钮，用于判断是否上传成功投标文件
            if recallTenderFile_result is not False:  # 判断是否上传成功
                self.update_applyNumber(applynumber + 1, projectNumber=projectNumber)  # 更新报名人数
            else:
                self.logger.debugText(projectNumber=projectNumber, bidder=bidder,
                                      errorText='确认上传：' + str(text03))  # 打印错误信息
        elif bidFile_result is False:  # 未找到投标文件按钮
            recallTenderFile_result = self.find_element(self.recallTenderFile_locator, 2)  # 撤回投标文件按钮，用于判断是否上传成功投标文件
            self.error_detemine(result=recallTenderFile_result, isFalseText='该企业未报名！',
                                isNoneText='投标文件已上传！', projectNumber=projectNumber, bidder=bidder)
        else:
            self.logger.debugText(projectNumber=projectNumber, bidder=bidder, errorText=bidFile_result)
