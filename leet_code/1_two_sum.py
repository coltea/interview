class Solution:
    def twoSum(self, nums, target):
        dt = dict()
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in dt:
                return [dt[another_num], index]
            dt[num] = index
        return None

