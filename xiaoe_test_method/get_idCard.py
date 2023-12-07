# -*- coding: utf-8 -*-
# @Time : 2023-09-18 13:50
# @Author : 皮卡丘

import requests
from base.base import Base
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium import webdriver
import re


class Get_idCard(Base):
    url = 'https://www.lddgo.net/common/idgenerator'
    province = '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div/input'  # 选择省份
    fujian = '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/dl/dd[14]'
    text = '//*[@id="generateResult"]'
    btn = '//*[@id="startGenerate"]'
    number = '//*[@id="generatorCount"]'
    number_locator = (By.XPATH, number)
    btn_locator = (By.XPATH, btn)
    text_locator = (By.XPATH, text)
    province_locator = (By.XPATH, province)
    fujian_locator = (By.XPATH, fujian)
    drive = webdriver.Edge()
    drive.get(url=url)
    drive.maximize_window()

    def get_idCard(self):
        self.send_keys(self.number_locator, '100')
        self.click(self.province_locator)
        self.click(self.fujian_locator)
        self.click(self.btn_locator)
        result = self.get_text(self.text_locator)
        l = re.findall('身份证号码:(.*?),出生日期', result)
        with open('idCard.txt', 'w+') as f:  # 删除文件内容
            f.truncate(0)
        for i in l:
            with open('idCard.txt', 'a+') as f:
                f.write(i + '\n')


if __name__ == '__main__':
    get_idCard = Get_idCard()
    get_idCard.get_idCard()
