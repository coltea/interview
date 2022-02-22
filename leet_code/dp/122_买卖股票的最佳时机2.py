from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min = prices[0]
        for i in range(1, len(prices)):
            # print(i , min)
            if min == -1:
                min = prices[i]
                continue
            if min > prices[i]:
                min = prices[i]
            if i != len(prices) - 1:
                if prices[i + 1] > prices[i]:
                    continue

            res += (prices[i] - min)
            min = -1
        return res


if __name__ == '__main__':
    # print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 7
    # print(Solution().maxProfit([1, 2, 3, 4, 5]))  # 4
    print(Solution().maxProfit([2, 1, 2, 0, 1]))  # 4
