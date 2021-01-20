class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if len(s) == 0:
            return 0
        lt = [str(i) for i in range(10)]
        nagetive = False
        if s[0] == "-":
            nagetive = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        ans = ""
        print(s)

        for i in s:
            if i not in lt:
                break
            ans += i
        if ans == "":
            return 0
        ans = int(ans) if not nagetive else -int(ans)

        if ans > 2**31-1:
            return 2**32-1
        if ans < -2**31:
            return -2**31
        return ans

if __name__ == '__main__':
    s = Solution()
    r = s.myAtoi("   +0 123")
    print(f"res:{r}")
    r = s.myAtoi("-+12")
    print(f"res:{r}")
    r = s.myAtoi("   -42")
    print(f"res:{r}")
    r = s.myAtoi("4193 with words")
    print(f"res:{r}")
    r = s.myAtoi("words and 987")
    print(f"res:{r}")
    r = s.myAtoi("-91283472332")
    print(f"res:{r}")
    r = s.myAtoi(" ")
    print(f"res:{r}")
