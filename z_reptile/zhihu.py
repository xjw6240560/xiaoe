# -*- coding: utf-8 -*-
# @Time : 2023-12-08 11:08
# @Author : 皮卡丘
import requests
from fake_useragent import UserAgent


class Zhihu:
    @staticmethod
    def talk():
        headers = {'UserAgent': UserAgent().random}
        url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend?action=down&ad_interval=1&after_id=5&desktop=true&page_number=5&session_token=f119c0bd70a0a9ea2f3e25e7d90589cb'
        result = requests.get(url=url, headers=headers)
        for i in result.json()['data']:
            print('标题：' + i['target']['question']['title'])
            print(i['target']['content'])


if __name__ == '__main__':
    zhihu = Zhihu()
    zhihu.talk()
