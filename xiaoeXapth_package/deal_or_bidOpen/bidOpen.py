from base.base import Base
import time
from selenium.webdriver.common.by import By
import random


class BidOpen(Base):
    clickSignIn = "//div/span[contains(text(),'点击签到')]"  # 点击签到
    message_input = "//button[contains(text(),'发送')]/../preceding-sibling::input"  # 消息输入框
    send_button = "//button[contains(text(),'发送')]"
    bidRepresentative = "//label[contains(text(),'投标代表')]/following-sibling::div/div/input"  # 投标代表
    linkNumber = "//label[contains(text(),'联系电话')]/following-sibling::div/div/input"  # 联系电话
    affirm = "//span[contains(text(),'取消')]/../following-sibling::button/span[contains(text(),'确定')]"  # 确定
    decodeBidFile = "//span[contains(text(),'解密投标文件')]"  # 解密投标文件
    affirmDecode = "//span[contains(text(),'取消')]/../following-sibling::button//span[contains(text(),'确认解密')]"  # 确认解密
    input_bidMessage_button = "//div//span[contains(text(),'延长解密时间')]/../following-sibling::div//span[contains(text(" \
                              "),'录入唱标信息')]"  # 录入唱标信息
    #     input_bidMessage_button ="//*[@id='wrap']/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/span"
    bidMessage_saveButton = "//span[contains(text(),'保存')]"  # 点击保存唱标信息
    raiseObjection = "//span[contains(text(),'查看异议')]/../following-sibling::div/div//span[contains(text(),'提出异议')]"  # 提出异议
    inputContent = "//textarea[@placeholder='请输入内容，不少于5个字']"  # 输入提议内容
    raiseObjectionAffirm = "//span[contains(text(),'/200')]/ancestor::div/following-sibling::div/button/span[" \
                           "contains(text(),'提出异议')]"  # 弹窗提出异议
    affirmBidResult = "//span[contains(text(),'提出异议')]/../following-sibling::div//span[contains(text(),'确认唱标结果')]"
    resultAffirm = "//p[contains(text(),'确认唱标结果')]/../div/button[2]/span[contains(text(),'确认')]"
    refresh = "//p[contains(text(),'刷新')]"

    clickSignIn_locator = (By.XPATH, clickSignIn)
    message_input_locator = (By.XPATH, message_input)
    send_button_locator = (By.XPATH, send_button)
    bidRepresentative_locator = (By.XPATH, bidRepresentative)
    affirm_locator = (By.XPATH, affirm)
    linkNumber_locator = (By.XPATH, linkNumber)
    decodeBidFile_locator = (By.XPATH, decodeBidFile)
    affirmDecode_locator = (By.XPATH, affirmDecode)
    input_bidMessage_button_locator = (By.XPATH, input_bidMessage_button)
    bidMessage_saveButton_locator = (By.XPATH, bidMessage_saveButton)
    raiseObjection_locator = (By.XPATH, raiseObjection)
    inputContent_locator = (By.XPATH, inputContent)
    raiseObjectionAffirm_locator = (By.XPATH, raiseObjectionAffirm)
    affirmBidResult_locator = (By.XPATH, affirmBidResult)
    resultAffirm_locator = (By.XPATH, resultAffirm)
    refresh_locator = (By.XPATH, refresh)

    def clickSignIn_click(self):  # 点击签到
        return self.click(self.clickSignIn_locator)

    def message_input_send_keys(self):  # 发送消息
        for i in range(20):
            self.send_keys(self.message_input_locator, i)
            self.click(self.send_button_locator)

    def sum_message(self):  # 计算消息总数i
        count = 0
        for i in range(1, 1000):
            time.sleep(0.3)
            message = "//div[@class='message aui-padded-b-20']/div[" + str(208 - i) + "]"
            message_locator = (By.XPATH, message)
            try:
                self.click(message_locator)
                self.roll_className("message aui-padded-b-20", 60)
            except:
                print("第" + str(i) + "条信息找不到")
                break
            count = count + 1
        print(count)

    def bidRepresentative_send_keys(self):  # 输入投标代表
        self.send_keys(self.bidRepresentative_locator, "写代表")

    def linkNumber_send_keys(self):  # 输入联系电话
        self.send_keys(self.linkNumber_locator, "15212345678")

    def affirm_click(self):  # 点击确认
        self.click(self.affirm_locator)

    def decodeBidFile_click(self):  # 点击解密
        time.sleep(0.5)
        return self.click(self.decodeBidFile_locator)

    def affirmDecode_click(self):  # 点击确认解密
        self.click(self.affirmDecode_locator)

    def input_bidMessage_button_click(self):  # 点击录入唱标信息按钮
        self.click(self.input_bidMessage_button_locator)

    def input_bidMessage_send_keys(self, num):  # 录入唱标信息
        flag = 0
        for j in range(2, num):
            pageJumps = "//span[contains(text(),'录入唱标信息')]/../following-sibling::div//div[3]//ul//li[text()='" + str(
                j) + "']"  # 页面跳转
            pageJumps_locator = (By.XPATH, pageJumps)
            for i in range(1, 6):
                price = random.randint(10000, 1000000)
                input_bidMessage = "//tr[" + str(i) + "]//td[4]/div/div/input[@placeholder='请输入']"
                input_bidMessage_locator = (By.XPATH, input_bidMessage)
                try:
                    self.send_keys(input_bidMessage_locator, price)
                except:
                    flag = 1
                    print("页面只有" + str(i - 1) + "数据")
                    break
            if flag == 0:
                try:
                    self.click(pageJumps_locator)
                    time.sleep(0.2)
                except:
                    print("分页不足：" + str(j) + "页")
                    break
            elif flag == 1:
                break
            else:
                print("错误状态" + str(flag))

    def bidMessage_saveButton_click(self):  # 点击保存唱标信息
        self.click(self.bidMessage_saveButton_locator)

    def raiseObjection_click(self):  # 点击提出异议
        self.click(self.raiseObjection_locator)

    def inputContent_send_keys(self):  # 输入异议内容
        self.send_keys(self.inputContent_locator, "评标结果需要多长时间出来")

    def raiseObjectionAffirm_click(self):  # 点击确认提出异议
        self.click(self.raiseObjectionAffirm_locator)

    def affirmBidResult_click(self):  # 点击确认唱标结果
        time.sleep(0.3)
        self.click(self.affirmBidResult_locator)

    def resultAffirm_click(self):  # 点击唱标结果弹窗确认
        self.click(self.resultAffirm_locator)

    def refresh(self):  # 查看是否有刷新按钮
        return self.find_element(self.refresh_locator, 0.5)
