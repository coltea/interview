n = int(input())


def fn(n):
    for i in range(2, n + 1):
        if n % i == 0:
            if n // i == 1:
                print(i, end=' ')
                break
            print(i, end=' ')
            n = n // i
            fn(n)
            break


fn(n)
