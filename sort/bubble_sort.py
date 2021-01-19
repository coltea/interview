def bubble_sort(lt):
    if len(lt) <= 1:
        return lt
    for i in range(0, len(lt) - 1):
        for i2 in range(0, len(lt) - 1 - i):
            print(i, i2)
            if lt[i2] > lt[i2 + 1]:
                lt[i2], lt[i2 + 1] = lt[i2 + 1], lt[i2]
    return lt


def bs(lt):
    if len(lt) <= 1:
        return lt
    for i in range(0, len(lt)-1):
        for i2 in range(0, len(lt)-1-i):
            if lt[i2] > lt[i2+1]:
                lt[i2], lt[i2+1] = lt[i2+1], lt[i2]
    return lt


if __name__ == "__main__":
    li = [53, 26, 93, 17, 77, 31, 443, 232, 3, 3]
    print(li)
    res = bs(li)
    print(res)



