"""
斐波那契数列
"""


def fibonacci(n):
    lt = [1, 1]
    if n <= 2:
        return lt[:n]
    for i in range(2, n):
        lt.append(lt[i - 1] + lt[i - 2])
    return lt


if __name__ == '__main__':
    print(fibonacci(100))
