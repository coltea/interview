from typing import *


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def find_min(lt):
            min_index = 0
            min_value = lt[0]
            for index, v in enumerate(lt):
                if v < min_value:
                    min_index, min_value = index, v
            return min_index, min_value

        res = nums[:3]
        dis = abs(sum(res) - target)
        for i in range(3, len(nums)):
            n1 = abs(sum([nums[i]] + nums[1:]) - target)
            n2 = abs(sum(nums[:1] + [nums[i]] + nums[2:]) - target)
            n3 = abs(sum(nums[:2] + [nums[i]]) - target)

            min_index, min_value = find_min([n1, n2, n3])
            print(i, min_index, min_value, [n1, n2, n3])

            if min_value < dis:
                print(min_value, dis)
                res[min_index] = [n1, n2, n3][min_index]
                dis = abs(sum(res) - target)
        print(res)
        return sum(res)


if __name__ == '__main__':
    # print(Solution().threeSumClosest([-1, 2, 1, -4], 1))  # 2
    print(Solution().threeSumClosest([-1, 2, 20, -4, 50, -3, 10], 100))  # 2
