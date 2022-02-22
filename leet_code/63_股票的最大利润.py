class Solution:
    def maxProfit(self, prices):
        res = 0
        for e, p in enumerate(prices[:-1]):
            if max(prices[e + 1:]) - p > res:
                res = max(prices[e + 1:]) - p
        return res

    def maxProfit2(self, prices):
        if len(prices) <= 1:
            return 0
        cost, profit = prices[0], 0
        # print(cost)
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
            print(f"{price}: {cost}, {profit}")
        return profit


if __name__ == '__main__':
    t = [
        [],
        [1],
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1]
    ]
    for i in t:
        s = Solution()
        print(s.maxProfit2(i))
