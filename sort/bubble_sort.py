# def bubble_sort(alist):
#     # count = 0
#     for j in range(0, len(alist) - 1):  # 整个数列排序循环
#         for i in range(0, len(alist) - j - 1):
#             # 元素从头走到尾，走完一次，排好一个数
#             if alist[i] > alist[i + 1]:
#                 # 因为要和下一个数相比，所以i只需要走到len(alist) - 1 - j
#                 print(alist[i], alist[i + 1])
#                 alist[i], alist[i + 1] = alist[i + 1], alist[i]
#             # print(alist)
#             # count += 1
#             print(f'end j:{j},i:{i}')
#     # print(count)
#     return alist
#
#


def bubble_sort(lt):
    if len(lt) <= 1:
        return lt
    for i in range(0, len(lt) - 1):
        for i2 in range(0, len(lt) - 1 - i):
            print(i, i2)
            if lt[i2] > lt[i2 + 1]:
                lt[i2], lt[i2 + 1] = lt[i2 + 1], lt[i2]
    return lt


if __name__ == "__main__":
    li = [53, 26, 93, 17, 77, 31, 443, 232, 3, 3]
    print(li)
    res = bubble_sort(li)
    print(res)



