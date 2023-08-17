def square(x):
    if isinstance(x, (int, float)):
        return x**2
    else:
        raise ValueError("square", x)
    return x**2


print(square(4))
print(square(4.3))
print(square("aaaaa"))
