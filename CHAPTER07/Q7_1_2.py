def f(x):
    try:
        return sum(x) / len(x)
    except:
        return None


print(f([1.2, 2.3, 3.4, 2.3, 5.9]))
print(f(0))
