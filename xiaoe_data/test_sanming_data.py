# -*- coding: utf-8 -*-
# @Time : 2023-09-27 10:06
# @Author : 皮卡丘
from xiaoe_data.test_xiaoe_data import Test_xiaoe_data


class Test_sanming_data:
    t = Test_xiaoe_data()
    # username = ["15222222222", "15813174909", "15813174945", "15813175020", "15813175055"]
    # enterpriseName = ["福建尤建科技有限公司", "国函通科技有限公司",
    #                   "江西九润建设工程有限公司", "天一科技有限公司", "火炬招商服务中心有限公司",
    #                   ]
    username = ["15222222222", "15233333333", "15287654321", "15820093831", "15820093809", "15255555555", "15244444444",
                "15260621329", "13954214241", "15288888888", "15277777777"]
    enterpriseName = ["福建尤建科技有限公司", "福建省佳美集团公司厦门分公司", "江西湘昌建设有限公司",
                      "国函通科技有限公司", "农大侠（厦门）信息技术有限公司", "江西省本善建筑有限公司",
                      "德安县2023年老旧小区改造工程（一期）项目EPC总承包",
                      "厦门城市开发建设有限公司", "江西九润建设工程有限公司", "天一科技有限公司",
                      "建银工程咨询有限责任公司"]
    username1 = ["15212345678", "15287654321", "15813174909"]
    password = ["ndx111", "ndx111"]
    deal_login_url = t.deal_login_url.replace('jiaoyi', 'sanming')  # 交易平台地址
    expert_login_url = t.expert_login_url.replace('jiaoyi', 'sanming')  # 专家端登陆地址
    expert_projectList_url = t.expert_projectList_url.replace('jiaoyi', 'sanming')  # 专家端选择项目列表地址
    extract_login_url = t.extract_login_url.replace('jiaoyi', 'sanming')  # 抽取系统登录地址
    workbench_url = t.workbench_url.replace('jiaoyi', 'sanming')  # 工作台地址
    back_url = t.back_url.replace('jiaoyi', 'sanming')  # 总后台地址
    extract_username = ['15212345678', '15312345678', '15412345678', '15727114760']
    extract_password = "ndx111"
    marginApplyWay = 1
    tenderMan = '江西鸿业生态环境建设集团有限公司'  # 招标代理创建项目时，填写的招标人
    tenderManUnicode = '91350200MA2YNRF9XT3'  # 招标代理创建项目时，填写的社会统一信用代码
    tenderGencyName = '陕西省科馋徒教育股份有限公司'
