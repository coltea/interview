class Solution:
    def rob(self, nums) -> int:
        if len(nums) <= 3:
            return max(nums)

        def dp_num(nums):
            dp = nums[:2] + [nums[0] + nums[2]]
            for i in range(3, len(nums)):
                dp.append(max(dp[i - 2], dp[i - 3]) + nums[i])
            return max(dp[-1], dp[-2])

        return max(dp_num(nums[1:]), dp_num(nums[:-1]))


if __name__ == '__main__':
    a = [2, 3, 2]  # 3
    print(Solution().rob(a))
    # a = [1, 3, 1]  # 3
    # print(Solution().rob(a))
    a = [1, 2, 3, 1]  # 4
    print(Solution().rob(a))
    # a = [2, 7, 9, 3, 1]  # 12
    # print(Solution().rob(a))
    # # print(merge([5, 9], [2, 6]))
