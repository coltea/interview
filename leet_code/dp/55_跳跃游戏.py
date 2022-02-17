from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right_most = 0
        for i in range(len(nums) - 1):
            right_most = max(right_most, i + nums[i])  # 当前位置上，最远能跳到哪
            if right_most <= i:
                return False
        return True


if __name__ == '__main__':
    # a = [1, 2]  # false
    # print(Solution().canJump(a))
    a = [2, 3, 1, 1, 4]  # true
    print(Solution().canJump(a))
    a = [3, 2, 1, 0, 4]  # false
    print(Solution().canJump(a))
