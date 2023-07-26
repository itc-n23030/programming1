f = [sum, max, min]
n = [i for i in range(1, 11)]
for func in f:
    print(f"{func.__name__}:{func(n)}")
