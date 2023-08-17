w = "{:>3s}{:>3s}{:>3s}{:>3s}{:>3s}\033[32m{:>3s}\033[0m\033[31m{:>3s}\033[0m".format(
    "月", "火", "水", "木", "金", "土", "日"
)
w += "\n"
w2 = "{:4s}".format("")
for i in range(1, 32):
    if i % 7 == 5:
        w2 += "\033[32m{:>4s}\033[0m".format(str(i))
    elif i % 7 == 6:
        w2 += "\033[31m{:>4s}\033[0m".format(str(i))
        w2 += "\n"
    else:
        w2 += "{:>4s}".format(str(i))
print(w + w2)
