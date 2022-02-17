class Solution:
    def minCostClimbingStairs(self, cost):
        dp = cost[:2]
        for i in range(2, len(cost)):
            dp.append(min(dp[i-1], dp[i-2]) + cost[i])
        return min(dp[-1], dp[-2])


if __name__ == '__main__':
    a = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(Solution().minCostClimbingStairs(a))
    a = [10, 15, 20]  # 15
    print(Solution().minCostClimbingStairs(a))
