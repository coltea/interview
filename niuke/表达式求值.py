# a = input()


def run(a):
    num_lt = [str(i) for i in range(9)]
    lt = []
    n = ""
    for i in a:
        if i in num_lt:
            n += i
        else:
            lt.append(n)
            lt.append(i)
            n = ''
    lt.append(n)
    res = int(lt[0])
    t = 0
    for i in range(1, len(lt) - 1, 2):
        if lt[i] == '*':
            res *= int(lt[i + 1])
        if lt[i] == '/':
            res /= int(lt[i + 1])

    for i in range(1, len(lt) - 1, 2):
        if lt[i] == '+':
            res += int(lt[i + 1])
        if lt[i] == '-':
            res -= int(lt[i + 1])
    return res


if __name__ == '__main__':
    print(run("3*5+8-0*3-6+0+0"))
