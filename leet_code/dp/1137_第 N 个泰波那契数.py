class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n <= 2:
            return dp[n]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
        # print(dp)
        return dp[n]


if __name__ == '__main__':
    # 入：n = 25 1389537
    # a = [10, 9, 2, 5, 3, 7, 101, 18]
    r = Solution().tribonacci(25)
    print(r)
