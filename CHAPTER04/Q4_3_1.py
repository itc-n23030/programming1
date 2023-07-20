def f(*n, sep="."):
    return sep.join(n)


n = map(str, input().split())
print(f(*n, sep=input("間の記号:")))
