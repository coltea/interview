from typing import *


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = obstacleGrid
        if dp[0][0] == 1:
            return 0
        dp[0][0] = 1
        for h in range(len(obstacleGrid)):
            for l in range(len(obstacleGrid[0])):
                if h == l == 0:
                    continue
                if dp[h][l] == 1:
                    dp[h][l] = 0
                    continue
                h_again = 0 if h == 0 else dp[h - 1][l]
                l_again = 0 if l == 0 else dp[h][l - 1]
                # print(h, l, h_again, l_again)
                dp[h][l] = h_again + l_again
        # print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
