a = [(x, y, x * y) for x in range(1, 10) for y in range(1, 10)]
s = ""
for x, y, z in a:
    s += "{:4d}".format(z)
    if y == 9:
        s += "\n"
print(s)
