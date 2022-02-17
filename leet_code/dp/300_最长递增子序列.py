class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for i2 in range(i):
                # print(i, i2, dp)
                if nums[i] > nums[i2]:
                    dp[i] = max(dp[i], dp[i2] + 1)
            print(i, dp)
        return max(dp)


if __name__ == '__main__':
    # a = [10, 9, 2, 5, 3, 7, 101, 18]
    a = [3, 4, 1, 5, 6]
    r = Solution().lengthOfLIS(a)
    print(r)
