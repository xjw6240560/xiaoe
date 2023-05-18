import time
import unittest
from xiaoeXapth_package.deal_or_bidOpen.home_page_or_workbench import Home_page_or_workbench
from xiaoeXapth_package.deal_or_bidOpen.bidOpen import BidOpen
from xiaoeXapth_package.deal_or_bidOpen.create_project import CreateProjectMethod
from xiaoeXapth_package.deal_or_bidOpen.login_registerORselect_role import LoginORrole
from xiaoeXapth_package.deal_or_bidOpen.evaluationBid_entrance import EvaluationBid_entrance
from xiaoeXapth_package.deal_or_bidOpen.expert import Expert
from base.base import Base
class CreateProject(unittest.TestCase):
    username = ["15222222222","15260621329","13954214241","15255555555","15244444444","15233333333","15287654321","15288888888","15277777777"]
    enterpriseName = ["福建尤建科技有限公司","福建省佳美集团公司厦门分公司","江西湘昌建设有限公司","天一科技有限公司","德安县2023年老旧小区改造工程（一期）项目EPC总承包","厦门城市开发建设有限公司","江西九润建设工程有限公司","江西省本善建筑有限公司","建银工程咨询有限责任公司"]
    username1 = ["15212345678","15287654321","13412841346"]
    password = ["ndx111","111111"]
    projectNumber = "20230518170029"#项目编号
    tenderOrganizationType = "0"#自主招标0或者委托招标1
    tenderWay = 1#公开招标0、邀请招标1
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
            self.result1 = self.base.select_project(self.projectNumber)
            self.projectType_sql = self.result1[0]
            self.tenderOrganizationType_sql = self.result1[1]
            self.evaluationBidWay = self.result1[2]
            self.judgesCount =self.result1[3]
            self.tenderWay_sql = self.result1[4]
        except:
            print("项目信息查询失败")

        #查询专家账号和密码
        try:
            self.result2 = self.base.select_expert(self.projectNumber)
            self.expert_username = self.result2[0]
            self.expert_password = self.result2[1]
            self.expert_name = self.result2[2]
        except:
            print("专家账号查询失败——2")
    """
    创建项目（工程项目）
    """
    def test_01_engineering(self):#工程项目
        self.loginORrole.login(self.username1[0],self.password[0])#登入交易平台
        self.loginORrole.tenderee_click()#点击招标人
        self.createProjectMethod.handle_skip(-1)#跳转句柄
        self.home_page_or_workbench.engineerBusiness_click()#点击工程业务
        self.home_page_or_workbench.tenderProject_click()#点击招标项目
        self.createProjectMethod.addTenderProject_click()#点击新增招标项目
        projectNumber = self.createProjectMethod.projectNumber_send_keys()#输入项目编号
        self.createProjectMethod.projectName_send_keys()#输入项目名称
        self.createProjectMethod.projectAuditNumber_send_keys()#输入项目审批文号
        self.createProjectMethod.InvestprojectUnicode_send_keys()#投资项目统一代码
        self.createProjectMethod.tenderType_click()#点击招标类型
        self.createProjectMethod.build_click()#点击施工
        # time.sleep(1000)
        self.createProjectMethod.projectType_click()#点击项目类型
        self.createProjectMethod.houseBuild_click()#点击房屋建设
        self.createProjectMethod.tenderWay_click()#点击招标方式
        if self.tenderWay == 0:
            self.createProjectMethod.openTender_click()#点击公开招标
        elif self.tenderWay == 1:
            self.createProjectMethod.inviteTender_click()#点击邀请招标
            self.createProjectMethod.inviteBid_click()#点击邀请投标人
            self.createProjectMethod.addEnterprise(len(self.enterpriseName),enterpriseName=self.enterpriseName)
            self.createProjectMethod.close_click()#点击关闭
        self.createProjectMethod.projectPlace_send_keys()#输入项目地址
        self.createProjectMethod.projectPrice_send_keys()#输入项目估算价
        self.createProjectMethod.projectDate_send_keys()#输入工期
        self.createProjectMethod.tenderLinkMan_send_keys()#输入联系人
        self.createProjectMethod.tenderLinkManNumber_send_keys()#输入联系人手机号
        self.createProjectMethod.linkPlace_send_keys()#输入联系地址
        self.createProjectMethod.tenderOrganizationType_click()#点击招标组织方式
        #自主招标
        if self.tenderOrganizationType =="0":
            self.createProjectMethod.oneselfTender_click()#选择自主招标
            self.createProjectMethod.sectionNumber_send_keys()#输入标段编号
            self.createProjectMethod.sectionName_send_keys()#输入标段名称
            self.createProjectMethod.tenderFileBeginTime_send_keys()#输入招标文件领取开始时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.tenderFileEndTime_send_keys()#输入招标文件领取截止时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.applyBeginTime_send_keys()#输入报名开始时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.applyEndTime_send_keys()#输入报名截止时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.quizEndTime_send_keys()#输入提问截止时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.answerEndTime_send_keys()#输入答疑截止时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.bidFileEndTime_send_keys()#输入投标文件递交截止时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.bidOpenTime_send_keys()#输入开标时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.tenderFileCost_send_keys()#输入招标文件费用
            self.createProjectMethod.marginPaymentWay_click()#点击保证金缴纳方式
            # self.createProjectMethod.offlinePayment_click()#点击线下缴纳
            # self.createProjectMethod.EVE_click()#点击保函申请
            self.createProjectMethod.EVE_or_offlinePayment_click()#点击线上和线下
            self.createProjectMethod.marginSum_send_keys()#输入保证金金额
            self.createProjectMethod.marginEndTime_send_keys()#输入保证金戒指递交时间
            self.createProjectMethod.tenderNotice_click()#点击招标公告按钮
            self.createProjectMethod.upload_file("pdf")#上传招标公告
            self.createProjectMethod.tenderFile_click()#点击招标文件按钮
            self.createProjectMethod.upload_file("pdf")#上传招标文件
            time.sleep(0.3)
            self.createProjectMethod.saveButton_click()#点击保存按钮
            time.sleep(0.5)
        #委托招标
        elif self.tenderOrganizationType == "1":
            self.createProjectMethod.entrustTender_click()#委托招标
            self.createProjectMethod.tenderGency_click()#点击招标代理
            self.createProjectMethod.input_enterprise_send_keys()#输入招标代理名称
            self.createProjectMethod.search_click()#点击搜索企业
            self.createProjectMethod.selectTenderGency_click()#选择招标代理
            time.sleep(0.5)
            self.createProjectMethod.saveButton_click()#点击保存
            time.sleep(0.5)
        else:
            print("招标类型不符")
        self.base.insert_projectData(projectNumber=projectNumber,projectType="engineer",tenderOrganizationType=self.tenderOrganizationType,tenderWay=self.tenderWay)#数据库创建项目
    """
    创建项目（政采项目）
    """
    def test_03_purchase(self):#采购项目
        self.loginORrole.login(self.username1[0],self.password[0])#登入交易平台
        self.loginORrole.tenderee_click()#点击招标人
        self.createProjectMethod.handle_skip(-1)#跳转句柄
        self.home_page_or_workbench.purchaseBusiness_click()#点击采购业务
        self.home_page_or_workbench.purchaseTenderProject_click()#点击招标项目
        self.createProjectMethod.addTenderProject_click()#点击新增项目
        projectNumber = self.createProjectMethod.projectNumber_send_keys()#输入招标项目编号
        self.createProjectMethod.projectName_send_keys()#输入项目名称
        self.createProjectMethod.projectAuditNumber_send_keys()#输入项目审批文号
        self.createProjectMethod.InvestprojectUnicode_send_keys()#投资项目统一代码
        self.createProjectMethod.purchaseType_click()#采购类型
        self.createProjectMethod.purchaseBuild_click()#建筑材料
        self.createProjectMethod.purchaseWay_click()#采购方式
        if self.tenderWay == 0:
            self.createProjectMethod.openTender_click()#点击公开招标
        elif self.tenderWay == 1:
            self.createProjectMethod.inviteTender_click()#点击邀请招标
            self.createProjectMethod.inviteBid_click()#点击邀请投标人
            self.createProjectMethod.addEnterprise(len(self.enterpriseName),enterpriseName=self.enterpriseName)
            self.createProjectMethod.close_click()#点击关闭
        self.createProjectMethod.purchasePrice_send_keys()#采购预算
        self.createProjectMethod.projectPlace_send_keys()#输入项目地址
        self.createProjectMethod.tenderLinkMan_send_keys()#输入联系人
        self.createProjectMethod.tenderLinkManNumber_send_keys()#输入联系人手机号
        self.createProjectMethod.linkPlace_send_keys()#输入联系地址
        self.createProjectMethod.tenderOrganizationType_click()#点击招标组织方式
        if self.tenderOrganizationType == "0":
            self.createProjectMethod.oneselfTender_click()#自主招标
            self.createProjectMethod.sectionNumber_send_keys()#输入标段编号
            self.createProjectMethod.sectionName_send_keys()#输入标段名称
            self.createProjectMethod.tenderFileBeginTime_send_keys()#输入招标文件领取开始时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.tenderFileEndTime_send_keys()#输入招标文件领取截止时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.applyBeginTime_send_keys()#输入报名开始时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.applyEndTime_send_keys()#输入报名截止时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.quizEndTime_send_keys()#输入提问截止时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.answerEndTime_send_keys()#输入答疑截止时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.bidFileEndTime_send_keys()#输入投标文件递交截止时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.bidOpenTime_send_keys()#输入开标时间
            self.createProjectMethod.projectPlace_click()#点击项目地址
            self.createProjectMethod.tenderFileCost_send_keys()#输入招标文件费用
            self.createProjectMethod.marginPaymentWay_click()#点击保证金缴纳方式
            # self.createProjectMethod.offlinePayment_click()#点击线下缴纳
            # self.createProjectMethod.EVE_click()#点击保函申请
            self.createProjectMethod.EVE_or_offlinePayment_click()#线上和线下一起
            self.createProjectMethod.marginSum_send_keys()#输入保证金金额
            self.createProjectMethod.marginEndTime_send_keys()#输入保证金戒指递交时间
            self.createProjectMethod.tenderNotice_click()#点击招标公告按钮
            self.createProjectMethod.upload_file("pdf")#上传招标公告
            self.createProjectMethod.tenderFile_click()#点击招标文件按钮
            self.createProjectMethod.upload_file("pdf")#上传招标文件
            time.sleep(1)
            self.createProjectMethod.saveButton_click()#点击登录
        elif self.tenderOrganizationType == "1":
            self.createProjectMethod.entrustTender_click()#委托招标
            self.createProjectMethod.tenderGency_click()#点击招标代理
            self.createProjectMethod.input_enterprise_send_keys()#输入招标代理企业名称
            self.createProjectMethod.search_click()#点击搜索
            self.createProjectMethod.selectTenderGency_click()#选择招标代理
            time.sleep(1)
            self.createProjectMethod.saveButton_click()#点击保存
            time.sleep(2)
        else:
            print("项目类型不符")
        self.base.insert_projectData(projectNumber=projectNumber,projectType="purchase",tenderOrganizationType=self.tenderOrganizationType,tenderWay=self.tenderWay)
    """
    线下报名
    """
    def test_05_apply_offline(self):#报名(线下)状态
        count = 0
        for i in range(len(self.username)):
            # count = count +1
            # if count == 6 :
            #     break
            self.loginORrole.login(username=self.username[i],password=self.password[0])
            self.loginORrole.bidder_click()#点击投标人
            try:
                self.home_page_or_workbench.select_apply(projectNumber= self.projectNumber,projectType=self.projectType_sql,tenderWay=self.tenderWay)#点击工作台
            except:
                print("账号"+self.username[i]+"未找到"+self.projectNumber+"该项目")
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
            self.home_page_or_workbench.returnButton_click()#点击返回
            self.home_page_or_workbench.margin_back_click()#保证金返回
            self.home_page_or_workbench.uploadBidFile_click()#点击上传投标文件
            try:
                self.home_page_or_workbench.bidFileImg_click()#点击上传投标文件图片
            except:
                self.home_page_or_workbench.recallTenderFile_click()#撤回标书
                self.home_page_or_workbench.tenderFileAffirm_click()#确认撤回
                self.home_page_or_workbench.bidFileImg_click()#点击上传投标文件图片
            self.home_page_or_workbench.upload_file("pdf")#选择投标文件图片
            time.sleep(0.3)
            self.home_page_or_workbench.saveBidFile_click()#点击保存
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
            except:
                print("账号"+self.username[i]+"未找到"+self.projectNumber+"该项目")
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
            try:
                self.home_page_or_workbench.bidFileImg_click()#点击上传投标文件图片
            except:
                self.home_page_or_workbench.recallTenderFile_click()#撤回标书
                self.home_page_or_workbench.tenderFileAffirm_click()#确认撤回
                self.home_page_or_workbench.bidFileImg_click()#点击上传投标文件图片
            self.home_page_or_workbench.upload_file("pdf")#选择投标文件
            time.sleep(0.5)
            self.home_page_or_workbench.saveBidFile_click()#点击保存
            time.sleep(0.5)
            self.createProjectMethod.open_deal_url()
    """
    签到
    """
    def test_06_signIn_online(self):#签到
        for i in range(len(self.username)):
            self.loginORrole.login(username=self.username[i],password=self.password[0])
            self.loginORrole.bidder_click()#点击投标人
            try:
                self.home_page_or_workbench.select_bid_workbench(self.projectNumber,self.projectType_sql)
            except:
                print("账号"+self.username[i]+"未找到"+self.projectNumber+"该项目")
                self.createProjectMethod.open_deal_url()
                continue
            self.home_page_or_workbench.openBidEntrance_click()#点击开标入口
            time.sleep(0.5)
            self.createProjectMethod.handle_skip(-1)
            time.sleep(0.5)
            try:
                self.bidOpen.clickSignIn_click()#点击签到
            except:
                print("账号"+self.username[i]+"未找到签到按钮！")
                self.createProjectMethod.open_deal_url()
                continue
            self.bidOpen.bidRepresentative_send_keys()#输入投标代表
            self.bidOpen.linkNumber_send_keys()#输入联系人电话
            # time.sleep(1)
            self.bidOpen.affirm_click()#签到点击确认
            time.sleep(0.2)
            self.createProjectMethod.open_deal_url()
    """
    发送信息
    """
    def test_send_message(self):
        for i in range(len(self.username)):
            self.loginORrole.login(username=self.username[i],password=self.password[0])
            self.loginORrole.bidder_click()#点击投标人
            try:
                self.home_page_or_workbench.select_bid_workbench(self.projectNumber,self.projectType_sql)
            except:
                self.home_page_or_workbench.engpriseName_move()#悬浮在企业名称位置
                time.sleep(0.3)
                self.home_page_or_workbench.quitLogin_click()#点击推出登录
                continue
            self.home_page_or_workbench.openBidEntrance_click()#点击开标入口
            time.sleep(0.3)
            self.createProjectMethod.handle_skip(-1)
            self.bidOpen.message_input_send_keys()#发送信息
            self.createProjectMethod.handle_skip(0)
            self.home_page_or_workbench.engpriseName_move()#悬浮在企业名称位置
            time.sleep(0.5)
            self.home_page_or_workbench.quitLogin_click()#点击推出登录
    """
    解密投标文件
    """
    def test_07_apply_online(self):#解密投标文件
        for i in range(len(self.username)):
            self.loginORrole.login(username=self.username[i],password=self.password[0])
            self.loginORrole.bidder_click()#点击投标人
            try:
                self.home_page_or_workbench.select_bid_workbench(self.projectNumber,self.projectType_sql)#选择工作台
            except:
                print("账号"+self.username[i]+"未找到"+self.projectNumber+"该项目")
                self.createProjectMethod.open_deal_url()
                continue
            self.home_page_or_workbench.openBidEntrance_click()#点击开标入口
            time.sleep(0.2)
            self.createProjectMethod.handle_skip(-1)
            # time.sleep(1000)
            try:
                self.bidOpen.decodeBidFile_click()#点击解密
            except:
                print("账号"+self.username[i]+"未找到解密按钮！")
                self.createProjectMethod.open_deal_url()
                continue
            time.sleep(0.3)
            self.bidOpen.affirmDecode_click()#确认解密
            time.sleep(0.2)
            self.createProjectMethod.open_deal_url()
    """
    录入唱标信息
    """
    def test_input_bidMessage(self):#输入唱标信息
        self.loginORrole.jiaoyi_login(self.tenderOrganizationType_sql)
        self.home_page_or_workbench.select_tender_workbench(self.projectNumber,self.projectType_sql)
        self.home_page_or_workbench.openBidEntrance_click()#点击开标入口
        time.sleep(1)
        self.createProjectMethod.handle_skip(-1)
        self.bidOpen.input_bidMessage_button_click()#点击录入唱标信息按钮
        self.bidOpen.input_bidMessage_send_keys(2080)#录入唱标信息
        self.bidOpen.bidMessage_saveButton_click()#保存唱标信息
        time.sleep(1)
    """
    提出异议和确认唱标结果
    """
    def test_08_objection_or_affirmBidResult(self):#提出异议和确认唱标结果
        for i in range(len(self.username)):
            self.loginORrole.login(username=self.username[i],password=self.password[0])
            self.loginORrole.bidder_click()#点击投标人
            try:
                self.home_page_or_workbench.select_bid_workbench(self.projectNumber,self.projectType_sql)
            except:
                print("账号"+self.username[i]+"未找到"+self.projectNumber+"该项目")
                self.createProjectMethod.open_deal_url()
                continue
            self.home_page_or_workbench.openBidEntrance_click()#点击开标入口
            time.sleep(0.5)
            self.createProjectMethod.handle_skip(-1)
            try:
                self.bidOpen.raiseObjection_click()#点击提出异议
            except:
                print("账号"+self.username[i]+"未找到提出异议按钮")
                self.createProjectMethod.open_deal_url()
                continue
            self.bidOpen.inputContent_send_keys()#输入异议
            self.bidOpen.raiseObjectionAffirm_click()#确认提出异议
            self.bidOpen.affirmBidResult_click()#确认投标结果
            time.sleep(0.3)
            self.bidOpen.resultAffirm_click()#点击投标结果弹窗确认
            self.createProjectMethod.open_deal_url()
    """
    添加评标办法
    需要注意参数，评标类型
    """
    def test_add_evaluationBidWay(self):
        evaluationBidWay = 0 #0表示综合,1表示均值,2表示最低,3表示最高
        judgeNumber = 5#评委数量
        self.loginORrole.jiaoyi_login(self.tenderOrganizationType_sql)#选择招标人或者招标代理
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
        except:
            self.evaluationBid_entrance.close_click()
        self.base.update_evaluationBidWay(evaluationBidWay=evaluationBidWay,judgeNumber= judgeNumber,projectNumber=self.projectNumber)#更新评标办法
    """
    切换模板和添加评委
    需要注意参数，评标类型
    """
    def test_09_add_evaluationBid_and_judge(self):#添加评标办法和添加评委(自主招标)
        evaluationBidWay = 1 #0表示综合,1表示均值,2表示最低,3表示最高
        judgeNumber = 15 #评委数量
        self.loginORrole.jiaoyi_login(self.tenderOrganizationType_sql)#选择招标人或者招标代理
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
        except:
            self.evaluationBid_entrance.close_click()
        self.evaluationBid_entrance.affirmJudge_click()#点击确认评委
        self.evaluationBid_entrance.create_judge(judgeNumber)#添加评委
        self.base.update_evaluationBidWay(evaluationBidWay=evaluationBidWay,judgeNumber=judgeNumber,projectNumber=self.projectNumber)

    """
    保存评委名称、账号和密码
    """
    def test_save_username_password(self):#保存评委账号和密码
        self.loginORrole.jiaoyi_login(self.tenderOrganizationType_sql)
        self.home_page_or_workbench.select_tender_workbench(self.projectNumber,self.projectType_sql)
        self.home_page_or_workbench.evaluationBidEntrance_click()#点击评标入口
        self.evaluationBid_entrance.affirmJudge_click()#点击确认评委
        self.evaluationBid_entrance.judgeNumber_click()#评委账号管理
        self.evaluationBid_entrance.save_judge_username_password(self.projectNumber,self.judgesCount)
    """
    推选组长
    """
    def test_elect_group(self):#推荐组长
        username = self.expert_username
        password = self.expert_password
        # for i in range(len(username)):
        #     self.expert.login(username=username[i],password=password[i])
        #     self.expert.electGroup_click()#点击推选组长
        #     try:
        #         self.expert.elect_click(self.judgesCount)#点击推选
        #     except:
        #         print("已经推荐过了")
        #     time.sleep(0.5)
        self.expert.select_group(username=username,password=password,judgesCount=self.judgesCount)
        while True:
            try:
                self.expert.get_group()#输出组长是那个评委
                break
            except:
                self.expert.select_group(username=username,password=password,judgesCount=self.judgesCount)
                # print("票数相同,没有选出组长！！！")
    """
    评分,在运行报错时，需要输入评分点个数score_count = 个数 + 1,score_count初始值为0
    """
    def test_judge_score(self):#评分
        expert_username = self.expert_username#获取账号
        expert_password = self.expert_password#获取密码
        expert_name = self.expert_name#获取评委名称
        enterprise_count = 0#企业个数
        input_count = 0#评分点个数
        for i in range(len(expert_username)):
            self.expert.login(username=expert_username[i],password=expert_password[i])
            print("----------------------------------"+str(expert_name[i])+"----------------------------------")
            type = self.expert.review_click(self.evaluationBidWay)#专家选择评标类型,type用来判断是通过式，还是分值式
            # self.expert.click(self.expert.review1_locator)
            # type = 1
            if enterprise_count == 0 and input_count == 0:
                count = self.expert.enterprise_review(type= type)#企业评审
                enterprise_count = count[0]
                input_count = count[1]
            else:
                self.expert.enterprise_review(type= type,enterprise_count=enterprise_count,input_count=input_count)#企业评审
            time.sleep(0.2)
            try:
                self.expert.submit_result_click()#点击提交审核结果
                self.expert.submitResult_affirm_click()#点击确认
                time.sleep(0.5)
            except :
                continue
    """
    评委确认
    """
    def test_judgeAffirm(self):
        expert_username = self.expert_username#获取账号
        expert_password = self.expert_password#获取密码
        for i in range(len(expert_username)):
            self.expert.login(username=expert_username[i],password=expert_password[i])
            self.expert.judgeSignature_click()#点击评委签章
            self.expert.signature_examine(self.evaluationBidWay)#点击确认


    def tearDown(self):
        self.base.close()


if __name__ == '__main__':
    unittest.main()
