"""
斐波那契数列
"""


# def fibonacci(n):
#     lt = [1, 1]
#     if n <= 2:
#         return lt[:n]
#     for i in range(2, n):
#         lt.append(lt[i - 1] + lt[i - 2])
#     return lt

def fibonacci(a):
    res = [1, 1]
    if a <= 2:
        return res[:a]
    for i in range(2, a):
        res.append(res[i - 1] + res[i - 2])
    return res


if __name__ == '__main__':
    print(fibonacci(0))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(10))
    # lt = [1, 1]
    # n = 10
    # res = [lt[i - 1] + lt[i - 2] for i in range(n-2)]
    # print(res)
