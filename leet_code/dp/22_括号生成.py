from typing import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(s, l, r):
            # print(l, r)
            if l == r == 0:
                res.append(s)
                return
            elif 0 < l < r:
                generate(s + "(", l - 1, r)
                generate(s + ")", l, r - 1)
            elif r == l:
                generate(s + "(", l - 1, r)
            elif l == 0 and r > 0:
                generate(s + ")", l, r - 1)

        generate("", n, n)
        return res


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
