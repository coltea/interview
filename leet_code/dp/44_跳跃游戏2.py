from typing import *


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] + [float("inf")] * (len(nums) - 1)
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().jump([2, 3, 0, 1, 4]))
