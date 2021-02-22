class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return list(set(nums))

if __name__ == '__main__':
    s = Solution()
    r = s.longestCommonPrefix(["flower", "flow", "flight"])
    print(f"res:{r}")
    r = s.longestCommonPrefix( ["reflower", "flow", "flight"])
    print(f"res:{r}")
    # r = s.longestCommonPrefix(-4)
    # print(f"res:{r}")
