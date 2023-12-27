# 创建时间  2023-05-24 14:10
# 作者  小酒窝
from xiaoe_data.test_xiaoe_data import Test_xiaoe_data


class Formal_han_data:
    t = Test_xiaoe_data()
    username = ["15216189856", '17306010296', '18106099208', '17750626025']
    enterpriseName = ["农大侠（厦门）信息技术有限公司", '国函通科技有限公司', '江西湘昌建设有限公司',
                      '江西省本善建筑有限公司']
    username1 = ["15260621329", "15287654321", "13313707910"]
    password = ["ndx111", "ndx111"]
    deal_login_url = t.deal_login_url.replace('jiaoyi', 'biaohantong').replace('http', 'https')  # 交易正式登录地址
    expert_login_url = t.expert_login_url.replace('jiaoyi', 'biaohantong').replace('http', 'https')  # 专家正式登陆地址
    expert_projectList_url = t.expert_projectList_url.replace('jiaoyi', 'biaohantong').replace('http',
                                                                                               'https')  # 专家端选择项目列表地址
    extract_login_url = t.extract_login_url.replace('jiaoyi', 'biaohantong').replace('http', 'https')  # 专家抽取系统登陆地址
    workbench_url = t.workbench_url.replace('jiaoyi', 'biaohantong').replace('http', 'https')
    back_url = t.back_url.replace('jiaoyi', 'biaohantong').replace('http', 'https')  # 总后台地址
    extract_username = ['15212345678', '15312345678', '15412345678']
    extract_password = "ndx111"
    marginApplyWay = 0
    tenderMan = '厦门翔安建设发展有限公司'  # 招标代理创建项目时，填写的招标人
    tenderManUnicode = '91350213751625538W'  # 招标代理创建项目时，填写的社会统一信用代码
    tenderAgentName = '以招标公告为准'
