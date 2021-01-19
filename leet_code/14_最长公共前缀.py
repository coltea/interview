class Solution:
    def longestCommonPrefix(self, lt) -> str:
        index_lt = [len(i) for i in lt]
        t = lt[index_lt.index(min(index_lt))]
        for i in lt:
            if len(t) == 0:
                return ""
            if t not in i:
                print(t)
                t = t[:-1]
                print(t)
                continue

        return t


if __name__ == '__main__':
    s = Solution()
    r = s.longestCommonPrefix(["flower", "flow", "flight"])
    print(f"res:{r}")
    # r = s.longestCommonPrefix(2 ** 31)
    # print(f"res:{r}")
    # r = s.longestCommonPrefix(-4)
    # print(f"res:{r}")
