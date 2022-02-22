from typing import *


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0]]
        for i in range(1, len(triangle)):
            new_lt = [0] * len(triangle[i])
            for j in range(len(new_lt)):
                if j == 0:
                    num = dp[i - 1][0] + triangle[i][j]
                elif j == len(new_lt) - 1:
                    num = dp[i - 1][-1] + triangle[i][j]
                else:
                    num = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

                new_lt[j] = num

            dp.append(new_lt)

        return min(dp[-1])


if __name__ == '__main__':
    print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print(Solution().minimumTotal([[-10]]))
