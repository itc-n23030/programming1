w = "{:>4s}{:>4s}{:>4s}{:>4s}{:>4s}\033[32m{:>4s}\033[0m\033[31m{:>4s}\033[0m".format(
    "Mon", "Tue", "Wen", "Thu", "Fri", "Sat", "Sun"
)
w += "\n" + "            "
w2 = "{:4s}".format("")
for i in range(1, 31):
    if i % 7 == 2:
        w2 += "\033[32m{:>4s}\033[0m".format(str(i))
    elif i % 7 == 3:
        w2 += "\033[31m{:>4s}\033[0m".format(str(i))
        w2 += "\n"
    else:
        w2 += "{:>4s}".format(str(i))
print(w + w2)
