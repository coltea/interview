# 归并排序
def merge_sort(lt):
    if len(lt) <= 1:
        return lt
    mid = len(lt) // 2
    left = merge_sort(lt[:mid])
    right = merge_sort(lt[mid:])
    res = merge(left, right)
    return res


def merge(left, right):
    res = []
    while left and right:
        n = left.pop(0) if left[0] < right[0] else right.pop(0)
        res.append(n)
    res += left if len(right) == 0 else right
    return res


if __name__ == '__main__':
    a = [5, 9, 2, 6, 7]
    print(merge_sort(a))
    # print(merge([1, 3], [2, 4]))
