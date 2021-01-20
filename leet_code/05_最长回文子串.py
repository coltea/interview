class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            for i_start in range(0, len(s) - i + 1):
                res = s[i_start:i_start + i]
                if res[::-1] == res:
                    return res


if __name__ == '__main__':
    s = Solution()
    r = s.longestPalindrome("cbba")
    print(f"res:{r}")
    r = s.longestPalindrome("bb")
    print(f"res:{r}")
    r = s.longestPalindrome("a")
    print(f"res:{r}")
    r = s.longestPalindrome("ac")
    print(f"res:{r}")
    r = s.longestPalindrome("babad")
    print(f"res:{r}")
