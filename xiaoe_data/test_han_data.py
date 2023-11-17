from xiaoe_data.test_xiaoe_data import Test_xiaoe_data


class Test_han_data:
    t = Test_xiaoe_data()
    username = ["15222222222", "15233333333", "15287654321", "15255555555", "15244444444", "15260621329", "13954214241",
                "15288888888", "15277777777"]
    enterpriseName = ["福建尤建科技有限公司", "福建省佳美集团公司厦门分公司", "江西湘昌建设有限公司",
                      "江西省本善建筑有限公司", "江西九润建设工程有限公司", "厦门城市开发建设有限公司",
                      "建银工程咨询有限责任公司", "德安县2023年老旧小区改造工程（一期）项目EPC总承包", "天一科技有限公司"]
    username1 = ["15212345678", "15287654321", "13412841346"]
    password = ["ndx111", "ndx111"]
    deal_login_url = t.deal_login_url.replace('jiaoyi', 'han')  # 交易平台地址
    expert_login_url = t.expert_login_url.replace('jiaoyi', 'han')  # 专家端登陆地址
    expert_projectList_url = t.expert_projectList_url.replace('jiaoyi', 'han')  # 专家端选择项目列表地址
    extract_login_url = t.extract_login_url.replace('jiaoyi', 'han')  # 抽取系统登录地址
    workbeach_url = t.workbeach_url.replace('jiaoyi', 'han')  # 工作台地址
    back_url = t.back_url.replace('jiaoyi', 'han')  # 总后台地址
    extract_username = "15212345678"
    extract_password = "ndx111"
    marginApplyWay = 2
    tenderMan = '江西鸿业生态环境建设集团有限公司'  # 招标代理创建项目时，填写的招标人
    tenderManUnicode = '91350200MA2YNRF9XT3'  # 招标代理创建项目时，填写的社会统一信用代码
    tenderGencyName = '甘肃省胸补声蕊秘咨询股份有限公司'
