class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1, 1]
        if n <= 2:
            return dp[n]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]


if __name__ == '__main__':
    # a = [10, 9, 2, 5, 3, 7, 101, 18]
    a = [3, 4, 1, 5, 6]
    r = Solution().lengthOfLIS(a)
    print(r)
