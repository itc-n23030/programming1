name_age = {"tanaka": 35, "satou": 25, "suzuki": 27}


def dict_info(dict_tbl, key):
    try:
        return dict_tbl[key]
    except:
        return "Key is not found"


print(dict_info(name_age, "satou"))
print(dict_info(name_age, "yamada"))
