n = 23
a = ""
while n != 0:
    n, r = divmod(n, 2)
    a += str(r)
print(a)
