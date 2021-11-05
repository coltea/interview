from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        half_sum = sum(nums) // 2
        dp = [1] + [0] * half_sum

        if nums[0] <= half_sum:
            dp[nums[0]] = 1

        for i in range(1, len(nums)):
            for j in range(half_sum, -1, -1):
                if nums[i] <= j:
                    dp[j] = dp[j] or dp[j - nums[i]]
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    r = [1, 5, 11, 5]
    s = Solution()
    print(s.canPartition(r))
    r = [2]
    s = Solution()
    print(s.canPartition(r))
