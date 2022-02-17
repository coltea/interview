class Solution:
    def deleteAndEarn(self, nums):
        dt = dict()
        for i in nums:
            if i not in dt:
                dt[i] = 1
            else:
                dt[i] += 1

        min_v = min(dt.keys())
        max_v = max(dt.keys())

        print(dt, min_v, max_v)

        # 处理数组：最小值->最大值
        dp = [0] * (max_v + 1)
        for i in range(min_v, max_v + 1):
            if i == 1:  # 边界判断
                dp[i] = max(dp[i - 1], i * dt.get(i, 0))
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + i * dt.get(i, 0))
            print(dp)

        return dp[-1]


if __name__ == '__main__':
    a = [3, 4, 2]  # false
    print(Solution().deleteAndEarn(a))
    a = [2, 2, 3, 3, 3, 4]  # false
    print(Solution().deleteAndEarn(a))
