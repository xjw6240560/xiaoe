def test(num):
    for i in range(1, num + 1):
        print(' ' * (num - i) + ('*_' * (i-1))+"*")


test(10)
