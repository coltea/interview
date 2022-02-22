from typing import *


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m
        dp[0] = [1] * n
        for i in range(len(dp)):
            dp[i][0] = 1
        for row in range(1, m):
            for i in range(1, n):
                dp[row][i] = dp[row][i - 1] +dp[row-1][i]
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))
