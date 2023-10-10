# -*- coding: utf-8 -*-
# @Time : 2023-09-27 18:47
# @Author : 皮卡丘
from xiaoe_data.test_xiaoe_data import Test_xiaoe_data


class Formal_sanming_data(Test_xiaoe_data):
    t = Test_xiaoe_data()
    username = ["17759210504", "13313707910", "15216189856"]
    enterpriseName = ["测试公司名称", "以招标公告为准", "农大侠（厦门）信息技术有限公司"]
    username1 = ["13026824439", "15287654321", "15260621329"]
    password = ["ndx111", "ndx111"]
    deal_login_url = t.deal_login_url.replace('jiaoyi', 'minhztb').replace('http', 'https')  # 交易正式登录地址
    expert_login_url = t.expert_login_url.replace('jiaoyi', 'minhztb').replace('http', 'https')  # 专家正式登陆地址
    expert_projectList_url = t.expert_projectList_url.replace('jiaoyi', 'minhztb').replace('http',
                                                                                           'https')  # 专家端选择项目列表地址
    extract_login_url = t.extract_login_url.replace('jiaoyi', 'minhztb').replace('http', 'https')  # 专家抽取系统登陆地址
    workbeach_url = t.workbeach_url.replace('jiaoyi', 'minhztb').replace('http', 'https')
    back_url = t.back_url.replace('jiaoyi', 'minhztb').replace('http', 'https')  # 总后台地址
    extract_username = "15212345678"
    extract_password = "ndx111"
    environment = "正式"
    marginApplyWay = 0
    tenderMan = '测试企业'  # 招标代理创建项目时，填写的招标人
    tenderManUnicode = '4585452SDFGVCD454'  # 招标代理创建项目时，填写的社会统一信用代码
