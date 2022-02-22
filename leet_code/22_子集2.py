from typing import *


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [[], [nums[0]]]
        res = [[], [nums[0]]]
        for i in range(1, len(nums)):
            new_lt2 = []
            for j in res:
                new_lt = j + [nums[i]]
                new_lt.sort()
                if new_lt not in res:
                    new_lt2.append(new_lt)
            res.extend(new_lt2)
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.subsetsWithDup([]))
    # print(s.subsetsWithDup([1]))
    # print(s.subsetsWithDup([1, 2, 3]))
    print(s.subsetsWithDup([4, 4, 4, 1, 4]))
    print(len(s.subsetsWithDup([4, 4, 4, 1, 4])))
    print(len([[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]))
