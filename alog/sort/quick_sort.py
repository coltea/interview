def quick_sort(lt):
    if len(lt) <= 1:
        return lt
    mid = lt[len(lt) // 2]
    lt.remove(mid)
    left_lt, right_lt = [], []
    for i in lt:
        if i <= mid:
            left_lt.append(i)
        if i > mid:
            right_lt.append(i)
    print(f"l:{left_lt} m:{mid} r:{right_lt}")
    return quick_sort(left_lt) + [mid] + quick_sort(right_lt)


def qs(lt):
    left_lt, right_lt = [], []
    if len(lt) <= 1:
        return lt
    mid = lt[int(len(lt) / 2)]
    lt.remove(mid)
    for i in lt:
        if i > mid:
            right_lt.append(i)
        else:
            left_lt.append(i)
    return qs(left_lt) + [mid] + qs(right_lt)


if __name__ == '__main__':
    a = [1, 909, 4, 656, 54, 2, 2, 909]
    print(qs(a))