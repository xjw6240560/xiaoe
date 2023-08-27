from base.base import Base
from xiaoe_testcase.deal_testcase import CreateProject
import datetime
import random
def selectList(list):
    dic = set(list)
    if len(list) == len(dic):

        print("True")
    else:
        print("False")


class Pkq(Base):
    def selectList2(self,list2):
        for i in list2:
            if list2.count(i) >= 2:
                print("False")
                break
        else:
            print("True")


    def selectList3(self,list3):
        flag = True
        for i in range(len(list3)):
            if flag == False:
                break
            for j in range(len(list3)):
                if (list3[i] ==list3[j]) and (i!=j):
                    print("False")
                    flag = False

        if flag == True:
            print("True")


    def selectList4(self,nums,n):
        if n not in nums:
            return -1
        else:
            return nums.index(n)

    def selectList5(self):
        list4 = [3,5,1,2,6,8,7,7,6,5,4,9,3,2,2]

        for i in list4:
            while list4.count(i)>1:
                del list4[list4.index(i,list4.index(i)+1)]

        print(list4)

    def longestAddList(self):
        list5 = [1,2,1,3,5,3,7,9,1,3,4]


if __name__ == '__main__':
    pkq = Pkq()
    createProject = CreateProject()
    createProject.test_judge_score()
    # pkq.random_code()
    # list = [3,5,8,1,4,56]
    # # pkq.selectList(list)
    # # pkq.selectList2(list)
    # # pkq.selectList3(list)
    # # print(pkq.selectList4(list,1))
    # pkq.selectList5()
from functools import reduce
def asdas(s):
    disa = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    return disa[s]
def adbgf(x,y):
    return x*10+y
a = reduce(adbgf,map(asdas,"130579"))


def ab(s):
    disa = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
    return disa[s]
def ba(x,y):
    if x ==1:
        return 1
    x,y = y,x+y
    return ba(y,y-x)
b = reduce(ba,[1,1])
