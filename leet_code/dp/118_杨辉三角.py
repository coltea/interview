from typing import *


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        for rows in range(2, numRows):
            l = rows +1
            new_lt = [1] + (l - 2) * [0] + [1]
            for i in range(1, l - 1):
                new_lt[i] = res[rows - 1][i - 1] + res[rows - 1][i]
            res.append(new_lt)

        return res


if __name__ == '__main__':
    print(Solution().generate(3))  # 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    print(Solution().generate(5))  # 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
