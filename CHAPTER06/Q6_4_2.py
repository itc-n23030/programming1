def gene(a=30):
    for i in range(2, a):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i


e = gene()
for n in range(10):
    print(next(e), end=" ")
