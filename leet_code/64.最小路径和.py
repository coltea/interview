class Solution:

    @staticmethod
    def minPathSum(grid):
        for height, w_lt in enumerate(grid):
            for width, i in enumerate(w_lt):
                if height == width == 0:
                    continue
                pre_h = grid[height - 1][width] if height > 0 else float("inf")
                pre_w = grid[height][width - 1] if width > 0 else float("inf")
                grid[height][width] += min(pre_h, pre_w)

        return grid[-1][-1]


if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    res = Solution.minPathSum(grid)
    print(res)

    grid = [[1, 2, 3], [4, 5, 6]]
    res = Solution.minPathSum(grid)
    print(res)
