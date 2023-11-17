# 创建时间  2023-05-24 14:10
# 作者  小酒窝
from xiaoe_data.test_xiaoe_data import Test_xiaoe_data


class Formal_xiaoe_data(Test_xiaoe_data):
    t = Test_xiaoe_data()
    username = ["18567985980", "17600228350", "15260621329", "15216189856"]
    enterpriseName = ["内部测试企业号", "国函通科技有限公司", "厦建设发展有限公司", "农大侠（厦门）信息技术有限公司"]
    username1 = ["15212345678", "15287654321", "15000000000"]
    password = ["ndx111", "ndx111"]
    deal_login_url = t.deal_login_url.replace('jiaoyi', 'xiaoeztb').replace('http', 'https')  # 交易正式登录地址
    expert_login_url = t.expert_login_url.replace('jiaoyi', 'xiaoeztb').replace('http', 'https')  # 专家正式登陆地址
    expert_projectList_url = t.expert_projectList_url.replace('jiaoyi', 'xiaoeztb').replace('http',
                                                                                            'https')  # 专家端选择项目列表地址
    extract_login_url = t.extract_login_url.replace('jiaoyi', 'xiaoeztb').replace('http', 'https')  # 专家抽取系统登陆地址
    workbeach_url = t.workbeach_url.replace('jiaoyi', 'xiaoeztb').replace('http', 'https')
    back_url = t.back_url.replace('jiaoyi', 'xiaoeztb').replace('http', 'https')  # 总后台地址
    extract_username = "15212345678"
    extract_password = "ndx111"
    marginApplyWay = 0
    tenderMan = '厦门翔安建设发展有限公司'  # 招标代理创建项目时，填写的招标人
    tenderManUnicode = '91350213751625538W'  # 招标代理创建项目时，填写的社会统一信用代码
    tenderGencyName = '厦门城市开发建设有限公司'
