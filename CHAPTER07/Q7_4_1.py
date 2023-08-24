n = "out_test.txt"
with open("n", "w") as f:
    f.write("Hello out_test.txt")
with open("n", "r") as f:
    for i in f:
        print(i)
