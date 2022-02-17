class Solution:
    def maxSubArray(self, nums):
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(nums[i])
            dp[i] = dp[i] + max(dp[i - 1], 0)
        return max(dp)


if __name__ == '__main__':
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution().maxSubArray(a)
    print(s)
