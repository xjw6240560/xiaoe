from xiaoe_data.test_xiaoe_data import Test_xiaoe_data


class Test_han_data:
    t = Test_xiaoe_data()
    username = ["15222222222", "15813174909", "15813174945", "15813175020", "15813175055"]
    enterpriseName = ["福建尤建科技有限公司", "国函通科技有限公司",
                      "江西九润建设工程有限公司", "天一科技有限公司", "火炬招商服务中心有限公司",
                      ]
    username1 = ["15212345678", "15287654321", "13412841346"]
    password = ["ndx111", "111111"]
    deal_login_url = t.deal_login_url.replace('jiaoyi', 'han')  # 交易平台地址
    expert_login_url = t.expert_login_url.replace('jiaoyi', 'han')  # 专家端登陆地址
    expert_projectList_url = t.expert_projectList_url.replace('jiaoyi', 'han')  # 专家端选择项目列表地址
    extract_login_url = t.extract_login_url.replace('jiaoyi', 'han')  # 抽取系统登录地址
    workbeach_url = t.workbeach_url.replace('jiaoyi', 'han')  # 工作台地址
    back_url = t.back_url.replace('jiaoyi', 'han')  # 总后台地址
    extract_username = "15212345678"
    extract_password = "ndx111"
    environment = "测试"
    marginApplyWay = 2
    tenderMan = '江西鸿业生态环境建设集团有限公司'  # 招标代理创建项目时，填写的招标人
    tenderManUnicode = '91350200MA2YNRF9XT3'  # 招标代理创建项目时，填写的社会统一信用代码
