class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if len(nums1) == 0 and len(nums2) == 0:
            return round(0, 5)
        lt = nums1 + nums2
        lt.sort()
        a = len(lt) // 2
        b = len(lt) % 2
        if b == 1:
            return round(lt[a], 5)
        else:
            print(lt[a - 1] + lt[a])
            return round((lt[a - 1] + lt[a]) / 2.0, 5)


if __name__ == '__main__':
    s = Solution()
    r = s.findMedianSortedArrays([1, 2], [3, 4])
    print(f"res:{r}")
    r = s.findMedianSortedArrays([], [1])
    print(f"res:{r}")
    r = s.findMedianSortedArrays([1, 3], [2])
    print(f"res:{r}")
    r = s.findMedianSortedArrays([0, 0], [0, 0])
    print(f"res:{r}")
    r = s.findMedianSortedArrays([2], [])
    print(f"res:{r}")
