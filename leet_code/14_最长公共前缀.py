class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        len_lt = [len(i) for i in strs]
        res = strs[len_lt.index(min(len_lt))]
        for i in strs:
            if res == i[:len(res)]:
                continue
            else:
                t = ""
                for e,i2 in enumerate(res):
                    if i2 == i[e]:
                        t += i2
                    else:
                        break
                if not t:
                    return ""
                res = t

        return res


if __name__ == '__main__':
    s = Solution()
    r = s.longestCommonPrefix(["flower", "flow", "flight"])
    print(f"res:{r}")
    r = s.longestCommonPrefix( ["reflower", "flow", "flight"])
    print(f"res:{r}")
    # r = s.longestCommonPrefix(-4)
    # print(f"res:{r}")
