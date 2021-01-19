class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        return sorted(nums1[:m] + nums2[:n])


if __name__ == '__main__':
    s = Solution()
    r = s.merge([1,2,3,0,0,0], 3, [2, 5, 6], n=3)
    print(f"res:{r}")
    # r = s.reverse(2 ** 31)
    # print(f"res:{r}")
    # r = s.reverse(-4)
    # print(f"res:{r}")
