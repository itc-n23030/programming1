def f(n):
    a, b = 0, 1
    L = [0]
    while b < n:
        L.append(b)
        a, b = b, a + b
    return L


n = int(input())
print(f(n))

