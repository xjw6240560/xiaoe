from xiaoeXapth_package.deal_or_bidOpen.create_project import CreateProjectMethod
import time
import unittest
import traceback
from log.log import Logger
from xiaoeXapth_package.deal_or_bidOpen.home_page_or_workbench import Home_page_or_workbench
from xiaoeXapth_package.deal_or_bidOpen.bidOpen import BidOpen
from xiaoeXapth_package.deal_or_bidOpen.login_registerORselect_role import LoginORrole
from xiaoeXapth_package.deal_or_bidOpen.evaluationBid_entrance import EvaluationBid_entrance
from xiaoeXapth_package.deal_or_bidOpen.expert import Expert
from selenium.webdriver.support import expected_conditions as EC
from base.base import Base
class Deal_testcase(unittest.TestCase):
    logger = Logger()
    username = Base.username
    enterpriseName = Base.enterpriseName
    username1 = Base.username1
    password = Base.password
    projectNumber = "20230720150557"#项目编号
    tenderOrganizationType = "1"#自主招标0或者委托招标1
    tenderWay = 0#公开招标0、邀请招标1、竞争性磋商2、竞争性谈判3、单一采购来源4
    applyWay = 0#公开0、邀请1
    role = "0"#角色 0招标人、1招标代理
    def setUp(self):
        self.base = Base()
        self.createProjectMethod = CreateProjectMethod()
        self.loginORrole = LoginORrole()
        self.home_page_or_workbench = Home_page_or_workbench()
        self.bidOpen = BidOpen()
        self.evaluationBid_entrance = EvaluationBid_entrance()
        self.expert = Expert()
        self.createProjectMethod.open_deal_url()
        #查询项目信息
        try:
            self.result1 = self.base.query_projectData(self.projectNumber)
            self.projectType_sql = self.result1[0]
            self.tenderOrganizationType_sql = self.result1[1]
            self.evaluationBidWay = self.result1[2]
            self.judgesCount =self.result1[3]
            self.tenderWay_sql = self.result1[4]
            self.applyNumber = self.result1[5]
            self.enterpriseCount = self.result1[6]
            self.ratingPointCount = self.result1[7]
        except (Exception,BaseException):
            error = traceback.format_exc()
            self.logger.debugText(self.projectNumber,error)

        #查询专家账号和密码
        try:
            self.result2 = self.base.select_expert(self.projectNumber)
            self.expert_username = self.result2[0]
            self.expert_password = self.result2[1]
            self.expert_name = self.result2[2]
        except(Exception,BaseException):
            error = traceback.format_exc()
            self.logger.debugText(self.projectNumber,error)
    """
    创建项目（工程项目）
    """
    def test_01_engineering(self):#工程项目
        self.loginORrole.jiaoyi_login(role=self.role)#登入交易平台
        self.createProjectMethod.handle_skip(-1)#跳转句柄
        self.home_page_or_workbench.engineerBusiness_click()#点击工程业务
        self.home_page_or_workbench.tenderProject_click()#点击招标项目
        self.createProjectMethod.addTenderProject_click()#点击新增招标项目
        projectNumber = self.createProjectMethod.projectNumber_send_keys()#输入项目编号
        self.createProjectMethod.projectName_send_keys(projectType="engineering",tenderOrganizationType=self.tenderOrganizationType,tenderWay=self.tenderWay)#输入项目名称
        self.createProjectMethod.projectAuditNumber_send_keys()#输入项目审批文号
        self.createProjectMethod.InvestprojectUnicode_send_keys()#投资项目统一代码
        self.createProjectMethod.tenderType_click()#点击招标类型
        self.createProjectMethod.build_click()#点击施工
        # time.sleep(1000)
        self.createProjectMethod.projectType_click()#点击项目类型
        self.createProjectMethod.houseBuild_click()#点击房屋建设
        self.createProjectMethod.tenderWay_click()#点击招标方式
        self.createProjectMethod.tender_or_purchase_way(tenderWay=self.tenderWay,applyWay=self.applyWay)#选择招标方式
        self.createProjectMethod.projectPlace_send_keys()#输入项目地址
        self.createProjectMethod.projectPrice_send_keys()#输入项目估算价
        self.createProjectMethod.projectDate_send_keys()#输入工期
        self.createProjectMethod.tenderLinkMan_send_keys()#输入联系人
        self.createProjectMethod.tenderLinkManNumber_send_keys()#输入联系人手机号
        self.createProjectMethod.linkPlace_send_keys()#输入联系地址
        self.createProjectMethod.tender_or_tenderAgent(role=self.role,projectNumber=projectNumber,projectType = 'engineering',tenderOrganizationType=self.tenderOrganizationType,tenderWay=self.tenderWay)
    """
    创建项目（政采项目）
    """
    def test_03_purchase(self):#采购项目
        self.loginORrole.jiaoyi_login(role=self.role)#登入交易平台
        self.createProjectMethod.handle_skip(-1)#跳转句柄
        self.home_page_or_workbench.purchaseBusiness_click()#点击采购业务
        self.home_page_or_workbench.purchaseTenderProject_click()#点击招标项目
        self.createProjectMethod.addTenderProject_click()#点击新增项目
        projectNumber = self.createProjectMethod.projectNumber_send_keys()#输入招标项目编号
        self.createProjectMethod.projectName_send_keys(projectType="purchase",tenderOrganizationType=self.tenderOrganizationType,tenderWay=self.tenderWay)#输入项目名称
        self.createProjectMethod.projectAuditNumber_send_keys()#输入项目审批文号
        self.createProjectMethod.InvestprojectUnicode_send_keys()#投资项目统一代码
        self.createProjectMethod.purchaseType_click()#采购类型
        self.createProjectMethod.purchaseBuild_click()#建筑材料
        self.createProjectMethod.purchaseWay_click()#采购方式
        self.createProjectMethod.tender_or_purchase_way(tenderWay=self.tenderWay,applyWay=self.applyWay)#选择采购方式
        self.createProjectMethod.purchasePrice_send_keys()#采购预算
        self.createProjectMethod.projectPlace_send_keys()#输入项目地址
        self.createProjectMethod.tenderLinkMan_send_keys()#输入联系人
        self.createProjectMethod.tenderLinkManNumber_send_keys()#输入联系人手机号
        self.createProjectMethod.linkPlace_send_keys()#输入联系地址
        self.createProjectMethod.tender_or_tenderAgent(role=self.role,projectNumber=projectNumber,projectType = 'purchase',tenderOrganizationType=self.tenderOrganizationType,tenderWay=self.tenderWay)
    """
    线下报名
    """
    def test_05_apply_offline(self):#报名(线下)状态
        for i in range(len(self.username)):
            if i == 6 :
                break
            self.base.update_applyNumber(i+1,projectNumber=self.projectNumber)
            self.loginORrole.login(username=self.username[i],password=self.password[0])
            self.loginORrole.bidder_click()#点击投标人
            try:
                self.home_page_or_workbench.select_apply(projectNumber= self.projectNumber,projectType=self.projectType_sql,tenderWay=self.tenderWay,applyWay=self.applyWay)#点击工作台
            except(Exception,BaseException):
                error = traceback.format_exc()
                self.logger.debugText(self.projectNumber,error)
                self.createProjectMethod.open_deal_url()
                continue
            time.sleep(0.2)
            self.home_page_or_workbench.linkMan_send_keys()#输入联系人
            self.home_page_or_workbench.linkManNumber_send_keys()#输入联系手机号
            self.home_page_or_workbench.affirmApply_click()#点击确认报名
            # time.sleep(1000)
            self.home_page_or_workbench.bid_workbench_click(self.projectNumber)#点击工作台
            self.home_page_or_workbench.marginPay_click()#点击保证金缴纳
            self.home_page_or_workbench.offlinePay_click()#点击线下缴纳
            try:
                self.home_page_or_workbench.receiptImg_click()#点击上传回单图片
            except:
                self.home_page_or_workbench.recallReceipt_click()
                self.home_page_or_workbench.recallAffirm_click()
                self.home_page_or_workbench.receiptImg_click()#点击上传回单图片
            self.home_page_or_workbench.upload_file("img")#选择回单
            time.sleep(0.5)
            self.home_page_or_workbench.saveReceipt_click()#点击保存回单
            message = self.home_page_or_workbench.errorMessage_text()#获取提示信息
            self.logger.debugText(self.projectNumber,message,self.username[i])
            self.home_page_or_workbench.returnButton_click()#点击返回
            self.home_page_or_workbench.margin_back_click()#保证金返回
            self.home_page_or_workbench.uploadBidFile_click()#点击上传投标文件
            self.home_page_or_workbench.bid_price_send_keys()#输入投标价
            self.home_page_or_workbench.duration_send_keys()#输入工期
            self.home_page_or_workbench.quality_send_keys()#输入质量标准
            try:
                self.home_page_or_workbench.bid_file_click()#点击招标公告
            except:
                self.home_page_or_workbench.recallTenderFile_click()#撤回标书
                self.home_page_or_workbench.tenderFileAffirm_click()#确认撤回
                self.home_page_or_workbench.bid_price_send_keys()#输入投标价
                self.home_page_or_workbench.duration_send_keys()#输入工期
                self.home_page_or_workbench.quality_send_keys()#输入质量标准
                self.home_page_or_workbench.bid_file_click()#点击招标公告
            self.home_page_or_workbench.upload_file("xetf")#选择投标文件图片
            time.sleep(0.3)
            self.home_page_or_workbench.saveBidFile_click()#点击保存
            message = self.home_page_or_workbench.errorMessage_text()#获取提示信息
            self.logger.debugText(self.projectNumber,message,self.username[i],'报名成功')
            time.sleep(0.5)
            self.createProjectMethod.open_deal_url()#进入登录页面
    """
    上传电子回单
    """
    def test_05_01_apply_offline(self):#上传电子回单
        for i in range(len(self.username)):
            self.loginORrole.login(username=self.username[i],password=self.password[0])
            self.loginORrole.bidder_click()#点击投标人
            try:
                self.home_page_or_workbench.select_bid_workbench(self.projectNumber,self.projectType_sql)
            except(Exception,BaseException):
                error = traceback.format_exc()
                self.logger.debugText(self.projectNumber,error)
                self.createProjectMethod.open_deal_url()
                continue
            self.home_page_or_workbench.marginPay_click()#点击保证金缴纳
            self.home_page_or_workbench.offlinePay_click()#点击线下缴纳
            try:
                self.home_page_or_workbench.receiptImg_click()#点击上传回单图片
            except:
                self.home_page_or_workbench.recallReceipt_click()
                self.home_page_or_workbench.recallAffirm_click()
                self.home_page_or_workbench.receiptImg_click()#点击上传回单图片
            self.home_page_or_workbench.upload_file("img")#选择回单
            time.sleep(0.5)
            self.home_page_or_workbench.saveReceipt_click()#点击保存回单
            self.home_page_or_workbench.returnButton_click()#点击返回
            self.home_page_or_workbench.margin_back_click()
            self.home_page_or_workbench.uploadBidFile_click()#点击上传投标文件
            self.home_page_or_workbench.bid_price_send_keys()#输入投标价
            self.home_page_or_workbench.duration_send_keys()#输入工期
            self.home_page_or_workbench.quality_send_keys()#输入质量标准
            try:
                self.home_page_or_workbench.bid_file_click()#点击投标文件
            except:
                self.home_page_or_workbench.recallTenderFile_click()#撤回标书
                self.home_page_or_workbench.tenderFileAffirm_click()#确认撤回
                self.home_page_or_workbench.bid_price_send_keys()#输入投标价
                self.home_page_or_workbench.duration_send_keys()#输入工期
                self.home_page_or_workbench.quality_send_keys()#输入质量标准
                self.home_page_or_workbench.bid_file_click()#点击投标文件
            self.home_page_or_workbench.upload_file("xetf")#选择投标文件图片
            time.sleep(0.3)
            self.home_page_or_workbench.saveBidFile_click()#点击保存
            time.sleep(0.5)
            self.createProjectMethod.open_deal_url()#进入登录页面
    """
    签到
    """
    def test_06_signIn_online(self):#签到
        for i in range(self.applyNumber):
            self.loginORrole.login(username=self.username[i],password=self.password[0])
            self.loginORrole.bidder_click()#点击投标人
            try:
                self.home_page_or_workbench.select_bid_workbench(self.projectNumber,self.projectType_sql)
            except(Exception,BaseException):
                error = traceback.format_exc()
                self.logger.debugText(self.projectNumber,error)
                self.createProjectMethod.open_deal_url()
                continue
            self.home_page_or_workbench.openBidEntrance_click()#点击开标入口
            self.createProjectMethod.handle_skip(-1)
            if self.base.is_url(self.base.workbeach_url) :
                message = self.home_page_or_workbench.errorMessage_text()#获取提示信息
                self.logger.debugText(self.projectNumber,message,self.username[i])
                self.createProjectMethod.open_deal_url()
                continue
            else:
                try:
                    self.bidOpen.clickSignIn_click()#点击签到
                except:
                    self.logger.debugText(projectNumber=self.projectNumber,errorText= '未找到签到按钮！',bidder=self.username[i])
                    self.createProjectMethod.open_deal_url()
                    continue
                self.bidOpen.bidRepresentative_send_keys()#输入投标代表
                self.bidOpen.linkNumber_send_keys()#输入联系人电话
                # time.sleep(1)
                self.bidOpen.affirm_click()#签到点击确认
                time.sleep(0.2)
                self.createProjectMethod.open_deal_url()#跳转登录页面
    """
    解密投标文件
    """
    def test_07_apply_online(self):#解密投标文件
        for i in range(self.applyNumber):
            self.loginORrole.login(username=self.username[i],password=self.password[0])
            self.loginORrole.bidder_click()#点击投标人
            try:
                self.home_page_or_workbench.select_bid_workbench(self.projectNumber,self.projectType_sql)#选择工作台
            except(Exception,BaseException):
                error = traceback.format_exc()
                self.logger.debugText(self.projectNumber,error,self.username[i])
                self.createProjectMethod.open_deal_url()
                continue
            self.home_page_or_workbench.openBidEntrance_click()#点击开标入口
            self.createProjectMethod.handle_skip(-1)
            if self.base.is_url(self.base.workbeach_url) :
                message = self.home_page_or_workbench.errorMessage_text()#获取提示信息
                self.logger.debugText(self.projectNumber,message,self.username[i])
                self.createProjectMethod.open_deal_url()
                continue
            else:
                try:
                    time.sleep(0.5)
                    self.bidOpen.decodeBidFile_click()#点击解密
                except (Exception,BaseException):
                    self.logger.debugText(projectNumber=self.projectNumber,errorText="未找到解密按钮！",bidder=self.username[i])
                    self.createProjectMethod.open_deal_url()
                    continue
                self.bidOpen.affirmDecode_click()#确认解密
                time.sleep(0.2)
                self.createProjectMethod.open_deal_url()
    """
    提出异议和确认唱标结果
    """
    def test_08_objection_or_affirmBidResult(self):#提出异议和确认唱标结果
        for i in range(self.applyNumber):
            self.loginORrole.login(username=self.username[i],password=self.password[0])
            self.loginORrole.bidder_click()#点击投标人
            try:
                self.home_page_or_workbench.select_bid_workbench(self.projectNumber,self.projectType_sql)
            except(Exception,BaseException):
                error = traceback.format_exc()
                self.logger.debugText(self.projectNumber,error,self.username[i])
                self.createProjectMethod.open_deal_url()
                continue
            self.home_page_or_workbench.openBidEntrance_click()#点击开标入口
            time.sleep(0.5)
            self.createProjectMethod.handle_skip(-1)
            if self.base.is_url(self.base.workbeach_url) :
                message = self.home_page_or_workbench.errorMessage_text()#获取提示信息
                self.logger.debugText(self.projectNumber,message,self.username[i])
                self.createProjectMethod.open_deal_url()
                continue
            else:
                try:
                    self.bidOpen.raiseObjection_click()#点击提出异议
                except:
                    self.logger.debugText(projectNumber=self.projectNumber,errorText="未找到提出异议按钮！",bidder=self.username[i])
                    self.createProjectMethod.open_deal_url()
                    continue
                self.bidOpen.inputContent_send_keys()#输入异议
                self.bidOpen.raiseObjectionAffirm_click()#确认提出异议
                self.bidOpen.affirmBidResult_click()#确认投标结果
                time.sleep(0.2)
                self.bidOpen.resultAffirm_click()#点击投标结果弹窗确认
                time.sleep(0.3)
                self.createProjectMethod.open_deal_url()
    """
    添加评标办法
    需要注意参数，评标类型
    """
    def test_add_evaluationBidWay(self):
        evaluationBidWay = 0 #0表示综合,1表示均值,2表示最低,3表示最高
        judgeNumber = 3#评委数量
        self.loginORrole.jiaoyi_login(self.role)#选择招标人或者招标代理
        self.home_page_or_workbench.select_tender_workbench(self.projectNumber,self.projectType_sql)#工程或者采购工作台选择
        try:
            self.home_page_or_workbench.evaluationBidEntrance_click()#点击评标入口
            self.evaluationBid_entrance.nowEvaluationBidWay_click()#点击当前评标办法
            self.evaluationBid_entrance.choose_EvaluationBidWay(evaluationBidWay)#选择评标办法----0表示综合,1表示均值,2表示最低,3表示最高
            for i in range(1,3):
                self.evaluationBid_entrance.addScore_click()#点击添加评分点
                self.evaluationBid_entrance.scoreInput_send_keys(i)#输入评分点
                self.evaluationBid_entrance.mustType_click(i)#是否必须1表示非必须，2表示必须
                self.evaluationBid_entrance.reviewStandard_send_keys(i)#输入评分标准
                self.evaluationBid_entrance.addScoreSave_click()#点击评分点保存
            self.evaluationBid_entrance.saveEvaluationBidWay_click()#点击保存评标办法
            self.evaluationBid_entrance.saveEvaluationBidWayAffirm_click()#点击保存评标办法确定
        except(Exception,BaseException):
            error = traceback.format_exc()
            self.logger.debugText(self.projectNumber,error)
            self.evaluationBid_entrance.close_click()
        self.base.update_evaluationBidWay(evaluationBidWay=evaluationBidWay,judgeNumber= judgeNumber,projectNumber=self.projectNumber)#更新评标办法
    """
    切换模板和添加评委
    需要注意参数，评标类型
    """
    def test_09_add_evaluationBid_and_judge(self):#添加评标办法和添加评委(自主招标)
        evaluationBidWay = 6#0表示综合,1表示均值,2表示最低,3表示最高,4代表竞争性磋商,5代表竞争性谈判，6代表单一采购来源
        judgeNumber = 5 #评委数量
        if self.tenderOrganizationType_sql == '0':
            self.loginORrole.login(username=self.username1[0],password=self.password[0])
            self.loginORrole.tenderee_click()#点击招标人
        elif self.tenderOrganizationType_sql == '1':
            self.loginORrole.login(username=self.username1[2],password=self.password[1])
            self.loginORrole.tenderAgency_click()#点击招标代理
        self.home_page_or_workbench.select_tender_workbench(self.projectNumber,self.projectType_sql)#工程或者采购工作台选择
        try:
            self.home_page_or_workbench.evaluationBidEntrance_click()#点击评标入口
            self.evaluationBid_entrance.nowEvaluationBidWay_click()#点击当前评标办法
            self.evaluationBid_entrance.choose_EvaluationBidWay(evaluationBidWay)#选择评标办法----0表示综合,1表示均值,2表示最低,3表示最高
            self.evaluationBid_entrance.cutEvaluationBidWay_click()#点击切换评标办法
            self.evaluationBid_entrance.clickEvaluationBidWay_click()#点击评标办法
            self.evaluationBid_entrance.selectEvaluationBidWay_click()#选择评标办法
            self.evaluationBid_entrance.cutEvaluationBidWayAffirm_click()#确认切换评标办法
            self.evaluationBid_entrance.saveEvaluationBidWay_click()#点击保存评标办法
            self.evaluationBid_entrance.saveEvaluationBidWayAffirm_click()#点击确认保存评标办法
        except(Exception,BaseException):
            error = traceback.format_exc()
            self.logger.debugText(self.projectNumber,error)
            self.evaluationBid_entrance.close_click()
        self.base.update_evaluationBidWay(evaluationBidWay=evaluationBidWay,judgeNumber=judgeNumber,projectNumber=self.projectNumber)
    """
    推选组长
    """
    def test_elect_group(self):#推荐组长
        username = self.expert_username
        password = self.expert_password
        self.expert.select_group(username=username,password=password,projectNumber=self.projectNumber,name=self.expert_name)
        while True:
            try:
                result = self.expert.get_group()#输出组长是那个评委
                if result is None:
                    self.logger.debugText(projectNumber=self.projectNumber,errorText='没有推选出评委!!!')
                    raise Exception("没有推选出评委!!!")
                else:
                    expert_username = self.base.select_expert_username(projectNumber=self.projectNumber,judgeName=result)
                    self.logger.debugText(projectNumber=self.projectNumber,errorText='组长为:'+result+"  身份证号为："+str(expert_username[0]))
                break
            except (Exception, BaseException):
                exstr = traceback.format_exc()
                self.logger.debugText(projectNumber=self.projectNumber,errorText=exstr)
                self.expert.select_group(username=username,password=password,projectNumber=self.projectNumber,name=self.expert_name)
    """
    开始评标，注意需要输入评标类型是哪个
    """
    def test_judge_score(self):#评分
        buttonCount = 1#用来判断是哪个评标类型
        expert_username = self.expert_username#获取账号
        expert_password = self.expert_password#获取密码
        expert_name = self.expert_name#获取评委名称
        self.base.update_ratingPoint_count(ratingPointCount='0',ratingType= '0',projectNumber= self.projectNumber)
        for i in range(len(expert_username)):
            self.result1 = self.base.query_projectData(self.projectNumber)#查询项目数据
            enterpriseCount = self.result1[6]
            self.expert.login(username=expert_username[i],password=expert_password[i],projectNumber = self.projectNumber)
            print("----------------------------------"+str(expert_name[i])+"----------------------------------")
            self.expert.review_click(buttonCount)#专家选择评标类型
            if enterpriseCount == '0':
                self.expert.enterprise_review(projectNumber=self.projectNumber)#企业评审
            else:
                self.expert.enterprise_review(projectNumber=self.projectNumber,enterprise_count=str(enterpriseCount))#企业评审
            time.sleep(0.2)
            try:
                self.expert.submit_result_click()#点击提交审核结果
                self.expert.submitResult_affirm_click()#点击确认
                time.sleep(0.5)
                errortext = self.home_page_or_workbench.errorMessage_text()
                self.logger.debugText(projectNumber=self.projectNumber,errorText=errortext,bidder=self.expert_username[i])
            except (Exception,BaseException):
                error = traceback.format_exc()
                self.logger.debugText(self.projectNumber,error)
                continue
    """
    二次报价
    """
    def test_secondary_quotation(self):#二次报价
        for i in range(self.applyNumber):
            self.loginORrole.login(username=self.username[i],password=self.password[0])
            self.loginORrole.bidder_click()#点击投标人
            try:
                self.home_page_or_workbench.select_bid_workbench(self.projectNumber,self.projectType_sql)#选择工作台
            except(Exception,BaseException):
                error = traceback.format_exc()
                self.logger.debugText(self.projectNumber,error)
                self.createProjectMethod.open_deal_url()
                continue
            self.home_page_or_workbench.secondaryQuotation_click()#点击二次报价按钮
            try:
                self.home_page_or_workbench.secondaryQuotationInput_send_keys()#输入二次报价
            except(Exception,BaseException):
                error = traceback.format_exc()
                self.logger.debugText(self.projectNumber,error)
                self.createProjectMethod.open_deal_url()
                continue
            self.home_page_or_workbench.secondaryQuotationFile_input_click()#点击上传响应性文件
            self.base.upload_file('pdf')
            self.home_page_or_workbench.submitButton_locator_click()#点击提交二次报价按钮
            self.createProjectMethod.open_deal_url()
    """
    确认评标报告
    """
    def test_judgeAffirm(self):
        expert_username = self.expert_username#获取账号
        expert_password = self.expert_password#获取密码
        evaluationReportNumber = 0#评标报告数量
        for i in range(len(expert_username)):
            self.expert.login(username=expert_username[i],password=expert_password[i],projectNumber = self.projectNumber)
            self.expert.judgeSignature_click()#点击评委签章
            if evaluationReportNumber == 0:
                evaluationReportNumber = self.expert.signature_examine()#点击确认
                print(evaluationReportNumber)
            else:
                self.expert.signature_examine(evaluationReportNumber)
            self.logger.debugText(projectNumber=self.projectNumber,errorText='确认评标结果完成！！！',bidder= expert_username[i])

    def tearDown(self):
        self.base.close()


if __name__ == '__main__':
    unittest.main()
