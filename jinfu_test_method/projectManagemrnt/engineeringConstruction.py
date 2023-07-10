import time
from base.base import Base
from selenium.webdriver.common.by import By
from background import engineeringConstruction
class EngineeringConstruction(Base):
    projectManagement_locator = (By.XPATH,engineeringConstruction.projectManagement)
    engineeringConstruction_locator = (By.XPATH,engineeringConstruction.engineeringConstruction)
    append_locator = (By.XPATH,engineeringConstruction.append)
    projectName_locator = (By.XPATH,engineeringConstruction.projectName)
    projectNumber_locator = (By.XPATH,engineeringConstruction.projectNumber)
    tenderee_locator = (By.XPATH,engineeringConstruction.tenderee)
    creditCode_locator = (By.XPATH,engineeringConstruction.creditCode)
    linkmanName_locator = (By.XPATH,engineeringConstruction.linkmanName)
    tendereeMobile_locator = (By.XPATH,engineeringConstruction.tendereeMobile)
    province_locator = (By.XPATH,engineeringConstruction.province)
    provinceSelect_locator = (By.XPATH,engineeringConstruction.provinceSelect)
    city_locator = (By.XPATH,engineeringConstruction.city)
    citySelect_locator = (By.XPATH,engineeringConstruction.citySelect)
    place_locator = (By.XPATH,engineeringConstruction.place)
    center_locator = (By.XPATH,engineeringConstruction.center)
    centerName_locator = (By.XPATH,engineeringConstruction.centerName)
    projectType_locator = (By.XPATH,engineeringConstruction.projectType)
    projectTypeName_locator = (By.XPATH,engineeringConstruction.projectTypeName)
    tenderType_locator = (By.XPATH,engineeringConstruction.tenderType)
    tenderTypeName_locator = (By.XPATH,engineeringConstruction.tenderTypeName)
    marginDeadline_locator = (By.XPATH,engineeringConstruction.marginDeadline)
    marginDeadlineSelect_locator = (By.XPATH,engineeringConstruction.marginDeadlineSelect)
    releaseTime_locator = (By.XPATH,engineeringConstruction.releaseTime)
    releaseTimeSelect_locator = (By.XPATH,engineeringConstruction.releaseTimeSelect)
    marginAmount_locator = (By.XPATH,engineeringConstruction.marginAmount)
    planTime_locator = (By.XPATH,engineeringConstruction.planTime)
    contractReckonPrice_locator = (By.XPATH,engineeringConstruction.contractReckonPrice)
    bidValidity_locator = (By.XPATH,engineeringConstruction.bidValidity)
    affirm_locator = (By.XPATH,engineeringConstruction.affirm)

    def projectManagement_click(self):#点击项目管理
        self.click(self.projectManagement_locator)
        
        time.sleep(1)

    def engineeringConstruction_click(self):#点击工程建设
        self.click(self.engineeringConstruction_locator)
        
        time.sleep(1)

    def append_click(self):#点击添加
        self.click(self.append_locator)
        
        time.sleep(1)

    def projectName_send_keys(self):#输入项目名称
        self.send_keys(self.projectName_locator,"1220测试项目")
        
        time.sleep(1)

    def projectNumber_send_keys(self):#输入项目编号
        self.send_keys(self.projectNumber_locator,"202212201522")
        
        time.sleep(1)

    def tenderee_send_keys(self):#输入招标人姓名
        self.send_keys(self.tenderee_locator,"皮卡丘")
        
        time.sleep(1)

    def creditCode_send_keys(self):#社会统一信用代码
        self.send_keys(self.creditCode_locator,"PKQ342300")
        
        time.sleep(1)

    def linkmanName_send_kets(self):#联系人姓名
        self.send_keys(self.linkmanName_locator,"皮卡丘")
        
        time.sleep(1)

    def tendereeMobile_send_keys(self):#招标人手机号
        self.send_keys(self.tendereeMobile_locator,"15212345678")
        
        time.sleep(1)

    def province_click(self):#省份
        self.click(self.engineeringConstruction_locator)
        
        time.sleep(1)

    def provinceSelect_click(self):#省份名称
        self.click(self.provinceSelect_locator)
        
        time.sleep(1)

    def city_click(self):#城市
        self.click(self.city_locator)
        
        time.sleep(1)

    def citySelect_click(self):#城市名称
        self.click(self.citySelect_locator)
        
        time.sleep(1)

    def place_send_keys(self):#地点
        self.send_keys(self.place_locator)
        
        time.sleep(1)

    def center_click(self):#中心
        self.click(self.center_locator)
        
        time.sleep(1)

    def centerName_click(self):#中心名称
        self.click(self.centerName_locator)
        
        time.sleep(1)

    def projectType_ckick(self):#项目类型
        self.click(self.projectType_locator)
        
        time.sleep(1)

    def projectTypeName_click(self):#项目类型选择
        self.click(self.projectTypeName_locator)
        
        time.sleep(1)

    def tenderType_click(self):#投标类型
        self.click(self.tenderType_locator)
        
        time.sleep(1)

    def tenderTypeName_click(self):#招标类型名称
        self.click(self.tenderTypeName_locator)
        
        time.sleep(1)

    def marginDeadline_click(self):#保证金截止时间
        self.click(self.marginDeadline_locator)
        
        time.sleep(1)

    def marginDeadlineSelect_click(self):#保证金截止时间选择
        self.click(self.marginDeadlineSelect_locator)
        
        time.sleep(1)

    def releaseTime_click(self):#开标时间
        self.click(self.releaseTime_locator)
        
        time.sleep(1)

    def releaseTimeSelect_click(self):#开标时间选择
        self.click(self.releaseTimeSelect_locator)
        
        time.sleep(1)

    def marginAmount_send_keys(self):#输入保证金
        self.send_keys(self.marginAmount_locator,"120")
        
        time.sleep(1)

if __name__ == '__main__':
     base = Base()










