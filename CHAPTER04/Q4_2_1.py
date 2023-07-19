def f(n=0):
    if n == 0:
        return "日曜日"
    elif 1 <= n <= 5:
        return "平日"
    elif n == 6:
        return "土曜日"
    else:
        if n < 0:
            return "先週以前"
        else:
            return "来週以降"


n = int(input())
print(f(n))
