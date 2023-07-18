import pickle

with open("test.pkl", "rb") as f:
    d = pickle.load(f)
    print(d)
# [1,2,3,4,5,6,7,8,9,10]
