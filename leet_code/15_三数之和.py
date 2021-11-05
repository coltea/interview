class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        print(nums)
        res = []
        for i in range(len(nums)):
            print(i)
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                print(i, nums[i], nums[i - 1])
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r - 1]:
                        r = r - 1
                    l = l + 1
                    r = r - 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r = r - 1
                else:
                    l = l + 1
        return res

    def threeSum2(self, nums):
        # print(3434343)
        if len(nums) < 3:
            return []
        nums.sort()
        # print(nums)
        res = []
        for i in range(len(nums)):
            # print(i)
            if nums[i] > 0:
                break
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l = l + 1
                    r = r - 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r = r - 1
                else:
                    l = l + 1
        res2 = []
        # print(res)
        for i in res:
            # print(i)
            if i not in res2:
                # print(res2)
                res2.append(i)

        return


if __name__ == '__main__':
    s = Solution()
    # r = s.threeSum([3, 0, -2, -1, -1, 1, 2])
    r2 = s.threeSum2([3, 0, -2, -1, -1, 1, 2])
    # res:[[-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]
    # print(f"res:{r}")
    print(f"res:{r2}")
