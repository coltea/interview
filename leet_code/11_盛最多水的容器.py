class Solution:

    def maxArea(self, height):
        res = 0
        while height:
            count = min(height[0], height[-1]) * (len(height)-1)
            res = max(res, count)

            if height[0] < height[-1]:
                height = height[1:]

            else:
                height = height[:-1]

        return res


if __name__ == '__main__':
    s = Solution()
    r = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(f"true res:{r}")
