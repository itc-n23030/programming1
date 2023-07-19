def f(d):
    a, b, c = 3, 0, 2
    n = []
    while a < d:
        n.append(a)
        a, b, c = b, c, a + b
    return n


d = int(input())
print(f(d))
