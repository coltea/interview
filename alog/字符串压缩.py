def str_zip(a):
    if len(a) <= 1:
        return a
    cur = a[0]
    num = 0
    res = ""
    for i in a:
        if i == cur:
            num += 1
        else:
            res += cur + str(num)
            num = 1
            cur = i
    res += cur + str(num)
    return res


r = str_zip("aaabbcddhf")
print(r)
