import random


def f(func):
    def n(*args, **kwargs):
        print("==begin")
        result = func()
        return result

    return n


def my_func(n=random.randint(1, 100)):
    s = 0
    for i in range(1, n + 1):
        s += i
        print(s)
    return "==end"


deco_func = f(my_func)
print(deco_func())
