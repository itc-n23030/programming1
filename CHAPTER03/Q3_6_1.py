from random import sample

n = [str(i) for i in range(0, 10)]
while True:
    u = input()
    h = "".join(sample(n, 4))
    if h == u:
        print("Good Job")
        break
