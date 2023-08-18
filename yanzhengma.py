class Yanzhengma:
    def __init__(self, student, score):
        self.__student = student
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
            print(self.__score)
        else:
            print("分数格式不符")


if __name__ == '__main__':
    yzm = Yanzhengma("张三", 120)
    print(yzm.get_score())
    try:
      yzm.set_score(12)
    except:
         print("分数格式不符121212")
