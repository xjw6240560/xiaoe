# -*- coding: utf-8 -*-
# @Time : 2023-09-18 15:28
# @Author : 皮卡丘
import time
import unittest
from xiaoeXapth_package.back.expert_store import Expert_store
from base.base import Base


class Back_createExpert(unittest.TestCase):
    base = Base()
    expert_store = Expert_store()

    def setUp(self):
        self.list1 = []
        self.base.open_back_url()  # 打开总后台
        with open(r'E:\PycharmProjects\xiaoe\xiaoe_test_method\idCard.txt', 'r') as f:
            for i in range(49):
                idcard = f.readline()
                self.list1.append(idcard)

    def test_create_expert(self):  # 添加专家
        # time.sleep(1000)
        self.expert_store.login_back()  # 登录总后台
        self.base.handle_skip(-1)  # 跳转句柄
        self.expert_store.expert_manage_click()  # 点击专家库管理
        self.expert_store.store_expert_click()  # 点击在库专家
        for i in self.list1:
            mobile = self.base.get_mobile_time()
            errortext = self.expert_store.create_expert(expertName='测试专家' + str(i), expertMobile='152' + str(mobile),
                                            expertIdCard=i)
            if errortext is not None:
                continue

    def tearDown(self):
        self.base.close()


if __name__ == '__main__':
    unittest.main()
