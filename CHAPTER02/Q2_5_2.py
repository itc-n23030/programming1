def f(n):
    a = ""
    for i in range(n):
        for j in range(n):
            if i == j:
                a += "○ "
            else:
                a += "● "
        a += "\n"
    return a


print(f(4))
