class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def recur(i, j):
            # 结束条件
            if j == len(p): return i == len(s)
            # 首字母匹配
            first_match = (len(s) > i) and (p[j] == s[i] or p[j] == '.')
            # 处理 `*`
            if len(p) >= j + 2 and p[j + 1] == '*':
                return recur(i, j + 2) or (first_match and recur(i + 1, j))
            # 处理首字母匹配
            return first_match and recur(i + 1, j + 1)

        return recur(0, 0)


if __name__ == '__main__':
    s = Solution()

    r = s.isMatch("aa", "b*a*c*a")
    print(f"true res:{r}")

    r = s.isMatch("aa", "a*c*a")
    print(f"true res:{r}")
