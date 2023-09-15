import random
import time
from base.base import Base
from xiaoeXapth_package.deal_or_bidOpen.home_page_or_workbench import Home_page_or_workbench
from xiaoeXapth_package.deal_or_bidOpen.bidOpen import BidOpen
from xiaoeXapth_package.deal_or_bidOpen.create_project import CreateProjectMethod
from xiaoeXapth_package.deal_or_bidOpen.login_registerORselect_role import LoginORrole
from xiaoeXapth_package.deal_or_bidOpen.evaluationBid_entrance import EvaluationBid_entrance
from xiaoeXapth_package.deal_or_bidOpen.expert import Expert
from base.base import Base
class Test(Base):
    projectNumber = "20230421105413"#项目编号
    tenderType = "0"#自主招标0或者委托招标1
    def  createProject(self):
        self.createProjectMethod = CreateProjectMethod()
        self.loginORrole = LoginORrole()
        self.home_page_or_workbench = Home_page_or_workbench()
        self.bidOpen = BidOpen()
        self.evaluationBid_entrance = EvaluationBid_entrance()
        self.expert = Expert()

        self.createProjectMethod.open_deal_url()#打开交易平台
        self.loginORrole.code_login_click()#点击验证码登录
        time.sleep(0.5)
        self.loginORrole.send_number_input()#输入账号
        self.loginORrole.send_password()#输入图片验证码
        noteCode = self.get_noteCode_time()
        self.loginORrole.register_noteCode_send_keys(noteCode)
        self.loginORrole.login_button_click()#点击登录

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
        self.createProjectMethod.openTender_click()#点击公开招标
        self.createProjectMethod.tenderOrganizationWay_click()#点击招标组织方式
        #自主招标
        if self.tenderType =="0":
            self.createProjectMethod.oneselfTender_click()#选择自主招标
            self.createProjectMethod.projectPlace_send_keys()#输入项目地址
            self.createProjectMethod.projectPrice_send_keys()#输入项目估算价
            self.createProjectMethod.projectDate_send_keys()#输入工期
            self.createProjectMethod.tenderLinkMan_send_keys()#输入联系人
            self.createProjectMethod.tenderLinkManNumber_send_keys()#输入联系人手机号
            self.createProjectMethod.linkPlace_send_keys()#输入联系地址
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
            self.createProjectMethod.tenderNotice_send_keys()  # 上传招标公告
            time.sleep(0.5)
            self.createProjectMethod.tenderFile_send_keys()  # 上传招标文件
            time.sleep(1)
            self.createProjectMethod.saveButton_click()#点击保存按钮
            time.sleep(0.5)
            self.home_page_or_workbench.commitAudit_click()#点击提交审核
            time.sleep(1000)
            self.home_page_or_workbench.commitAudit_affirm_click()#点击提交审核确定
        #委托招标
        elif self.tenderType == "1":
            self.createProjectMethod.entrustTender_click()#委托招标
            self.createProjectMethod.projectPlace_send_keys()#输入项目地址
            self.createProjectMethod.projectPrice_send_keys()#输入项目估算价
            self.createProjectMethod.projectDate_send_keys()#输入工期
            self.createProjectMethod.tenderLinkMan_send_keys()#输入联系人
            self.createProjectMethod.tenderLinkManNumber_send_keys()#输入联系人手机号
            self.createProjectMethod.linkPlace_send_keys()#输入联系地址
            self.createProjectMethod.tenderGency_click()#点击招标代理
            self.createProjectMethod.selectTenderGency_click()#选择招标代理
            time.sleep(1)
            self.createProjectMethod.saveButton_click()#点击保存

        else:
            print("招标类型不符")
        self.insert_projectData(projectNumber=projectNumber,projectType="engineer",tenderType=self.tenderType)#数据库创建项目
        self.drive.close()
        # self.open_manage_url()



if __name__ == '__main__':
   test = Test()
   test.createProject()
