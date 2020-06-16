class Solution:
    def maxSubArray(self, nums) -> int:
        res = []
        for i, num in enumerate(nums[1:]):
            nums[i+1] = num + max(nums[i],0)
            print(nums)
        return max(nums)


#     def maxSubArray2(self, nums) -> int :
#         for i, num in enumerate(nums):


if __name__ == '__main__':
    a = [[-2, 1, -3, 4, -1, 2, 1, -5, 4]
         [1, 2]
         ]
    s = Solution()
    [print(s.maxSubArray(i)) for i in a]