class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
             'CM': 800, 'M': 1000}
        res = [d.get(s[k - 1:k + 1], d[v]) for k, v in enumerate(s)]

        for k, v in enumerate(s):
            print(s[max(k - 1, 0):k + 1])
            print(k-1, k+1)
            # print(d[v])
            print(d.get(s[max(k - 1, 0):k + 1], d[v]))

        return sum(res)


if __name__ == '__main__':
    s = Solution()
    r = s.romanToInt("IX")
    print(f"res:{r}")
    # r = s.romanToInt("MCMXCIV")
    # print(f"res:{r}")
    # r = s.romanToInt("LVIII")
    # print(f"res:{r}")

