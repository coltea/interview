from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for coin in coins:
            # print(coin)
            for i2 in range(coin, amount + 1):
                dp[i2] = min(dp[i2 - coin] + 1, dp[i2])
                # print(dp)
            print(coin, dp)
        return -1 if dp[amount] == float('inf') else dp[amount]


if __name__ == '__main__':
    amount, coins = 11, [2, 3, 5]  # 4
    print(Solution().coinChange(coins, amount))
    # a = [3, 2, 1, 0, 4]  # 2
    # print(Solution().i2ump(a))
