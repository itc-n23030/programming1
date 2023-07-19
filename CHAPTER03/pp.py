from random import sample

n = [str(i) for i in range(10)]
e = sample(n, 4)
a = ""
while list(a) == e:
    num = list(input())
    for i in e:
        if num != i:
            a += "x"
        else:
            a += str(num)
    print(a)
