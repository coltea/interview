from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for i in coins:
            for i2 in range(i, amount + 1):
                dp[i2] += dp[i2 - i]
                print(i2, i2 - i, dp)
            print(dp)
        return dp[-1]


if __name__ == '__mai' \
               'n__':
    amount, coins = 6, [1, 2, 3]  # 4
    print(Solution().change(amount, coins))
    # a = [3, 2, 1, 0, 4]  # 2
    # print(Solution().i2ump(a))
