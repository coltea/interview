def merge(left, right):
    print(f'merge:{left}, {right}')
    res = []
    while left and right:
        min_val = left.pop(0) if left[0] < right[0] else right.pop(0)
        res.append(min_val)
    res += left if left else right
    return res


def merge_sort(A):
    print(f"merge_sort: {A}")
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left, right = merge_sort(A[:mid]), merge_sort(A[mid:])
    res = merge(left, right)
    return res


if __name__ == '__main__':
    a = [1, 909, 4, 656, 54, 2, 2, 909]
    # a = [5, 4, 1, 3]
    print(merge_sort(a))
