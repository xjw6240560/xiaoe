from base.base import Base


class Demo:
    def aaa(self, num):
        def retry(func):  # 报错重新执行
            def wrapper(*args, **kwargs):
                for i in range(num):
                    result = func(*args, **kwargs)
                    if result is not False:
                        break

            return wrapper

        return retry

    def test(self):
        print('1231331')
        return False

    test()
