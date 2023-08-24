with open("my_math.py", "w") as i:
    i.write(
        """def my_pow(x, y):
            return x**y\n"""
    )

import my_math

print(my_math.my_pow(2, 4))
