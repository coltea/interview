t = ""
while 1:
    # try:
    if len(t) >= 8:
        print(t[:8])
        t = t[8:]
        continue
    elif len(t) > 0:
        print(t + "0" * (8 - len(t)))
    t = input()
    # except:
    #     break
