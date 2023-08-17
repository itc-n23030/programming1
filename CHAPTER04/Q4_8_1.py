import time


def fun(func):
    def n(*args, **kwargs):
        print("==begin")
        result = func(*args, **kwargs)
        return result

    return n


@fun
def my_func():
    print("Sleeping")
    time.sleep(2)
    print("Done Sleeping")
    return "==end"


print(my_func())
# 2秒後に関数が実行される
