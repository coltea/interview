class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        print(nums)
        res = []
        for i in range(len(nums)):
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


if __name__ == '__main__':
    s = Solution()
    r = s.threeSum([3, 0, -2, -1, -1, 1, 2])
    print(f"res:{r}")
