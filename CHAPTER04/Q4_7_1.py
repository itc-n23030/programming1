def f():
    def ff(a, b):
        return a + b

    return ff


n = f()
print(n(5, 9))
