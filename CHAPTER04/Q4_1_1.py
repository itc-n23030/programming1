def f(n):
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b


n = int(input())
print(f(n))
