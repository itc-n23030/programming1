from random import randint


def ls(h=10):
    m = []
    for i in range(h):
        name = "n" + str(randint(10, 50))
        height = randint(150, 190)
        weight = randint(50, 80)
        m.append((name, height, weight))
    return m


# 身長順
for n in sorted(ls(10), key=lambda x: x[1]):
    print(n)
# 体重順
for n in sorted(ls(10), key=lambda x: x[2]):
    print(n)
