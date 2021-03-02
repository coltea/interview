while 1:
    try:
        lt_len = input()
        lt = []
        for i in range(int(lt_len)):
            lt.append(int(input()))
        [print(i) for i in sorted(list(set(lt)))]
    except:
        break
