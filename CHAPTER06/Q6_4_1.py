import random

random.seed(1)
msgs = [
    "Hi",
    "Hello",
    "Good mornig",
    "Good night",
    "See you later",
    "How are you",
    "Have a good day",
]
with open("some.txt", "w") as f:
    for i in range(1000000):
        f.write(f"{i}, {random.choice(msgs)}\n")


n = open("some.txt")
a = 0
for t in n:
    if a < 3:
        print(t)
        a += 1
n.close()
