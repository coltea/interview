"""
全排列
"""


def permute(nums):
    n = len(nums)
    res = []

    def backTrack(mark, temp_list):
        if len(mark) == n:
            res.append(temp_list)

        for j in range(0, n):
            if j in mark:
                continue
            if j > 0 and nums[j] == nums[j - 1] and j - 1 not in mark:  # 去重，
                continue
            backTrack(mark + [j], temp_list + [nums[j]])

    backTrack([], [])
    return res


if __name__ == '__main__':
    # res = permute([1, 2, 3])
    res = permute([1, 1, 2])
    # res = permute([2, 1])20
    print(res)
