def f(*x):
    return [i**2 for i in x]


n = list(range(100))
print(f(*n))
