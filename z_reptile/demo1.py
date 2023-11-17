# 创建时间  2023-07-13 11:59
# 作者  小酒窝
# _*_ coding:utf-8 _*_
import requests
from fake_useragent import UserAgent
import time
from selenium import webdriver
import re
from lxml import html


class Demo1():
    def get_data(self):
        etree = html.etree
        url = 'https://www.mca.gov.cn/mzsj/xzqh/2022/202201xzqh.html'
        headers = {"User-Agent": UserAgent().random}
        req = requests.get(url=url, headers=headers)
        xml = req.content.decode('utf-8')
        data = etree.HTML(xml)  # 将str类型转化成xml类型
        code = data.xpath("//tr[@style='mso-height-source:userset;height:14.25pt']//td[2]/text()")
        name = data.xpath("//tr[@style='mso-height-source:userset;height:14.25pt']//td[3]/text()")
        # dictionaray = dict(zip(name,code))
        # for i,j in dictionaray.items():
        #     with open(r'D:\123.txt','wb') as f:
        #         f.write((j+'\r\n').encode('utf-8'))
        #     print(i,j)


if __name__ == '__main__':
    demo1 = Demo1()
    demo1.get_data()
