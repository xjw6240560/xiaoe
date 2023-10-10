# 创建时间  2023-06-21 15:20
# 作者  小酒窝
import random


class Random_generate_project_type:
    role = ['招标人', '招标代理']
    projectType = ['工程', '政采']
    tenderOrganizationType = ['自主招标', '委托招标']
    tenderWay = ['公开招标', '邀请招标', '竞争性磋商', '竞争性谈判', '单一来源']
    bidEvaluationMethod = ['综合评标办法', '均值评标办法', '最大值评标办法', '最小值评标办法', '线下评标', '单一来源',
                           '竞争性磋商', '竞争性谈判']

    def random_generate_project_type(self, num):
        for i in range(num):
            projectType = self.projectType_random()
            role = self.role_random()
            tenderOrganizationType = self.tenderOrganizationType_random()
            if projectType == '工程':
                if role == '招标人':
                    tenderWay = self.tenderWay_random(0, 1)
                    bidEvaluationMethod = self.bidEvaluationMethod_random(4)
                    print(
                        projectType + '  ' + role + '  ' + tenderOrganizationType + '  ' + tenderWay + '  ' + bidEvaluationMethod)
                    continue
                else:
                    tenderWay = self.tenderWay_random(0, 1)
                    bidEvaluationMethod = self.bidEvaluationMethod_random(4)
                    print(projectType + '  ' + role + '  ' + '委托招标' + '  ' + tenderWay + '  ' + bidEvaluationMethod)
                    continue
            else:
                if role == '招标人':
                    tenderWay = self.tenderWay_random()
                    if tenderWay in ('竞争性磋商', '竞争性谈判', '单一来源'):
                        bidEvaluationMethod = self.bidEvaluationMethod_random()
                        while bidEvaluationMethod in (
                                '竞争性磋商', '竞争性谈判', '单一来源') and bidEvaluationMethod != tenderWay:
                            bidEvaluationMethod = self.bidEvaluationMethod_random()
                        print(
                            projectType + '  ' + role + '  ' + tenderOrganizationType + '  ' + tenderWay + '  ' + bidEvaluationMethod)
                        continue
                    else:
                        bidEvaluationMethod = self.bidEvaluationMethod_random(4)
                        print(
                            projectType + '  ' + role + '  ' + tenderOrganizationType + '  ' + tenderWay + '  ' + bidEvaluationMethod)
                        continue
                else:
                    tenderWay = self.tenderWay_random()
                    if tenderWay in ('竞争性磋商', '竞争性谈判', '单一来源'):
                        bidEvaluationMethod = self.bidEvaluationMethod_random()
                        while bidEvaluationMethod in (
                                '竞争性磋商', '竞争性谈判', '单一来源') and bidEvaluationMethod != tenderWay:
                            bidEvaluationMethod = self.bidEvaluationMethod_random()
                        print(
                            projectType + '  ' + role + '  ' + tenderOrganizationType + '  ' + tenderWay + '  ' + bidEvaluationMethod)
                        continue
                    else:
                        bidEvaluationMethod = self.bidEvaluationMethod_random(4)
                        print(
                            projectType + '  ' + role + '  ' + '委托招标' + '  ' + tenderWay + '  ' + bidEvaluationMethod)
                        continue

    def role_random(self):  # 产生角色
        count1 = random.randint(0, 1)
        return self.role[count1]

    def projectType_random(self):  # 产生项目类型
        count1 = random.randint(0, 1)
        return self.projectType[count1]

    def tenderOrganizationType_random(self):  # 产生招标组织方式
        count1 = random.randint(0, 1)
        return self.tenderOrganizationType[count1]

    def tenderWay_random(self, begin=0, end=4):  # 产生招标方式
        count1 = random.randint(begin, end)
        return self.tenderWay[count1]

    def bidEvaluationMethod_random(self, num=7):  # 产生招标方式
        count1 = random.randint(0, num)
        return self.bidEvaluationMethod[count1]


if __name__ == '__main__':
    random_generate_project_type = Random_generate_project_type()
    random_generate_project_type.random_generate_project_type(5)
