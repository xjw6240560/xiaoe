"""
read_csv: 读取csv文本
generate_script: 生成xpath
读取csv文本的数据生成xpath，例如：search = "div/div\input"
"""
import csv
from base.base import Base
class Generate_script(Base):
    base = Base()
    def generate_script_method(self):#生成脚本方法
        data = self.read_data_csv(begin=62,end=63,place=self.csv_place)#读取数据
        self.base.clear_text(self.script_place)#清除xpath文本
        """
        生成xpath
        """
        for i in data:
            with open(self.script_place,'a+',encoding="gbk") as f:
                f.write(i[0]+" = "+"\""+i[1]+"\""+i[3]+"\n")
        self.text_enter()#文本换行
        """
        生成定位器
        """
        for i in data:
            with open(self.script_place,'a+',encoding='gbk') as f:
                f.write(i[0]+'_locator = (By.XPATH,'+i[0]+')\n')
        self.text_enter()#文本换行
        """
        生成方法
        """
        for i in data:
            oneLines = "def "+i[0]+"_"+i[2]+"(self):"+i[3]+"\n"
            if i[2] == "send_keys":
                twoLines = "    self."+i[2]+"(self."+i[0]+"_locator,"+i[4]+")\n"
            else:
                twoLines = "    self."+i[2]+"(self."+i[0]+"_locator)\n"
            method = [oneLines,twoLines,"\n"]
            with open(self.script_place,'a+',encoding='gbk',newline="\n") as f:
                f.writelines(method)

if __name__ == '__main__':
    generate_script = Generate_script()
    generate_script.generate_script_method()
