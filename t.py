def permute(lt):
    res = []

    def permute_sort(ori_lt, temp_lt):
        if len(ori_lt) == 0:
            res.append(temp_lt)
        for i in range(len(ori_lt)):
            permute_sort(ori_lt[:i] + ori_lt[i + 1:], temp_lt + [ori_lt[i]])

    permute_sort(lt, [])
    return res


if __name__ == '__main__':
    a = [3, 4, 5]
    print(permute(a))
