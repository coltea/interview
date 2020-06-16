"""
全排列
"""

def permute(nums):
    def backtrack(ori_lt, tmp_lt):
        if len(ori_lt) == 0:
            res.append(tmp_lt)
        else:
            for i in range(len(ori_lt)):
                backtrack(ori_lt[:i] + ori_lt[i + 1:], tmp_lt + [ori_lt[i]])

    global res
    res = []
    backtrack(nums, [])
    return res


if __name__ == '__main__':
    # res = permute([1, 2, 3])
    res = permute([1, 2, 3])
    print(res)
