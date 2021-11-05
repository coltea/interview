from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = [0] * len(matrix), [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = col[j] = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] or col[j]:
                    matrix[i][j] = 0


if __name__ == '__main__':
    s = Solution()
    r2 = s.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])

    print(f"res:{r2}")
