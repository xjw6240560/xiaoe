#创建时间  2023-07-19 17:13
#作者  小酒窝
import requests
import re
import json
from fake_useragent import UserAgent
class Demo3():
    def get_one_data(self):
        url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1689757686322&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'
        headers = {'UserAgent': UserAgent().random}
        html = requests.get(url=url,headers=headers).text
        dict_data = json.loads(html)
        two_url = re.findall('jobdesc.html\?postId=(.*?)","',html)
        # recruitPostName = []
        # locationName = []
        # for i in dict_data['Data']['Posts']:
        #     with open(r'D:\123.txt','a+',encoding='utf-8') as f:
        #         f.write(str(i['RecruitPostName']+'  '+i['LocationName'])+'\r\n')
        #         f.write(str(i['Responsibility']).replace(r'\r\n','\r\n')+'\r\n')
        return two_url

    def get_two_data(self):#获取二级页面数据
        two_url = self.get_one_data()
        url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?'
        headers = {'UserAgent': UserAgent().random}
        for i in two_url:
            params = {
                'timestamp':'1689821704030',
                'language':'zh-cn',
                'postId':i
            }
            html = requests.get(url=url,params=params,headers=headers).text

            print(html)


if __name__ == '__main__':
    demo3 = Demo3()
    demo3.get_two_data()