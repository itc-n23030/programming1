from random import sample

i = ["m", "y"]
n = []
while True:
    m = sample([chr(i) for i in range(97, 123)], 2)
    n.append(m)
    if m == i:
        print(n)
        break
