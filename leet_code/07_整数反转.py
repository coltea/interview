class Solution:

    @staticmethod
    def check(x):
        if -(2 ** 31) <= x <= 2 ** 31 - 1:
            return True
        return False

    def reverse(self, x: int) -> int:
        if not Solution.check(x):
            return 0
        if x < 0:
            res = -int(str(x)[:0:-1])

        else:
            res = int(str(x)[::-1])
        if not Solution.check(res):
            return 0
        return res


if __name__ == '__main__':
    s = Solution()
    r = s.reverse(-32123123)
    print(f"res:{r}")
    r = s.reverse(2 ** 31)
    print(f"res:{r}")
    r = s.reverse(-4)
    print(f"res:{r}")
