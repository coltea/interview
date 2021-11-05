class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        tmp = ""
        for i in s:
            if i not in tmp:
                tmp += i
            else:
                tmp = tmp[tmp.index(i) + 1:] + i
                print(tmp)
            if len(tmp) > res:
                res = len(tmp)
        return res


if __name__ == '__main__':
    s = Solution()
    # r = s.lengthOfLongestSubstring("abcabcbb")
    # print(f"res:{r}")
    # r = s.lengthOfLongestSubstring("bbbbb")
    # print(f"res:{r}")
    r = s.lengthOfLongestSubstring("pwwkew")
    # print(f"res:{r}")
    # r = s.lengthOfLongestSubstring("au")
    print(f"res:{r}")
