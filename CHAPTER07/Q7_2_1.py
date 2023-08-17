def list_del(list, index):
    try:
        del list[index]
        return list
    except IndexError:
        return "Index Not Found"
    except:
        return "UnexpectedError"
    else:
        return "Successfully"


print(list_del([1, 2, 3, 4, 5, 6, 7, 8], 5))
print(list_del([1, 2, 3, 4], None))
print(list_del([1, 2, 3, 4], 7))
