from functools import lru_cache


class Solution:
    @lru_cache(10 ** 8)
    def climbStairs(self, n: int) -> int:
        if n in [1, 2]:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == '__main__':
    s = Solution()
    lt = [2, 3, 4, 5]
    [print(s.climbStairs(i)) for i in lt]
    for i in range(1,2):
        pass
