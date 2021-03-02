class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        cur = 0
        while cur <= right:
            print(nums, cur, left, right)
            if nums[cur] == 0 and nums[cur] != nums[left]:
                nums[cur], nums[left] = nums[left], nums[cur]
                left += 1
            elif nums[cur] == 2 and nums[cur] != nums[right]:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
                continue
            cur += 1
            print('1',nums, cur, left, right)

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, curr, p2 = 0, 0, len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0: # 为0，做出决策
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:   # 为2，做出决策
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            else:                   # 为1，做出决策
                curr += 1



if __name__ == '__main__':
    s = Solution()
    # r = s.sortColors([2, 0, 2, 1, 1, 0])
    # r = s.sortColors([0])
    r= [0,1,0]
    s.sortColors(r)
    # r = s.sortColors([2, 0, 2, 1, 1, 0])
    # r = s.sortColors([2, 0, 2, 1, 1, 0])/
    print(f"true res:{r}")
