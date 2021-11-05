from typing import List


class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        _, a, b, __ = self.get_lt(piles, 0, 0, 0)
        print(a, b)
        return True if a > b else False

    def get_lt(self, piles, a, b, flag):
        print(piles, a, b, flag)
        if len(piles) <= 0:
            return piles, a, b, flag

        get_num = 0

        if len(piles) == 1 or piles[0] > piles[-1]:
            get_num = piles[0]
            piles = piles[1:]
        elif piles[0] < piles[-1]:
            get_num = piles[-1]
            piles = piles[:-1]
        else:
            _, h_a, h_b, _ = self.get_lt(piles[1:], a, b, 0)
            _, l_a, l_b, _ = self.get_lt(piles[:-1], a, b, 0)
            print(h_a,l_a)
            if h_a >= l_a:
                get_num = piles[0]
                piles = piles[1:]
            else:
                get_num = piles[-1]
                piles = piles[:-1]

        if flag == 0:
            a += get_num
            flag = 1
        else:
            b += get_num
            flag = 0

        return self.get_lt(piles, a, b, flag)


if __name__ == '__main__':
    r = [2, 1, 3, 2]
    s = Solution()
    print(s.stoneGame(r))
    # r = [2, 1]
    # s = Solution()
    # print(s.stoneGame(r))
#
