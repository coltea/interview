def binary_search(items: list, item: int):
    print(items, item)
    if item > items[-1] or item < items[0] or len(items) == 0:
        return False
    n = len(items) // 2
    if items[n] == item:
        return True
    else:
        if items[n] < item:
            return binary_search(items[n:], item)
        else:
            return binary_search(items[:n], item)


print(binary_search([1, 2, 3, 4, 5], 4))
