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


if __name__ == '__main__':
    a = [1, 909, 4, 656, 54, 2, 2, 909]
    print(quick_sort(a))


def quick_sort(arr):
    """快速排序"""
    if len(arr) <= 1:
        return arr
    # 选取基准，随便选哪个都可以，选中间的便于理解
    mid = arr[len(arr) // 2]
    # 定义基准值左右两个数列
    left, right = [], []
    # 从原始数组中移除基准值
    arr.remove(mid)
    for item in arr:
        # 大于基准值放右边
        if item >= mid:
            right.append(item)
        else:
            # 小于基准值放左边
            left.append(item)
    # 使用迭代进行比较
    # print(f'l:{left} m:{mid} r:{right}  res: {quick_sort(left) + [mid] + quick_sort(right)}')
    print(f'l:{left} m:{mid} r:{right} ')

    return quick_sort(left) + [mid] + quick_sort(right)


if __name__ == '__main__':
    a = [1, 909, 4, 656, 54, 2,2,909]
    res = quick_sort(a)
    print(res)
