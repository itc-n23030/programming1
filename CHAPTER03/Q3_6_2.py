from random import sample

n = [str(i) for i in range(10)]
ss = "".join(sample(n, 4))
while True:
    h = input()
    if h == ss:
        print(h)
        print("congratulation")
        break
    a = ""
    for i in range(4):
        if h[i] != ss[i]:
            a += "x"
        else:
            a += h[i]
    print(a)
