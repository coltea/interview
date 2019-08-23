"""
二分法
"""


def binary_search(lt, target):
    print(f"lt: {lt}, target:{target}")
    if target < lt[0] or target > lt[-1] or len(lt) == 0:
        return False
    mid = len(lt) // 2
    if lt[mid] == target:
        return True
    elif lt[mid] > target:
        return binary_search(lt[:mid], target)
    else:
        return binary_search(lt[mid:], target)


if __name__ == '__main__':
    print(binary_search(list(range(1, 15)), 13))
