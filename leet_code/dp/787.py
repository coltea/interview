from typing import *


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = [float("inf")] * len(flights)
        f[src] = 0
        ans = f[dst]
        print(f)

        for i in range(k + 1):
            dp = [float("inf")] * len(flights)
            for src_dt, target_dt, cost in flights:
                dp[target_dt] = min(dp[target_dt], f[src_dt] + cost)
                # print(dp)
            f = dp
            print(f)
            ans = min(ans, f[dst])

        ans = -1 if ans == float("inf") else ans
        return ans


if __name__ == '__main__':
    s = Solution()
    res = s.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 300]], 0, 2, 1)
    print(res)
