a = {x for x in range(21)}
b = {y for y in range(21) if y % 2 == 0}
c = {z for z in a | b if z % 2 == 1}
print(a)
print(b)
print(c)
