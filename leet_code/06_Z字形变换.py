class Solution:
    @staticmethod
    def dict_add(lt, a):
        if a not in lt:
            lt

    def convert(self, s: str, numRows: int) -> str:
        res = {i: "" for i in range(numRows)}
        row_tmp = 0
        go = 1
        if numRows == 1:
            return s
        for i in s:
            res[row_tmp] += i
            if row_tmp < numRows - 1 and go == 1:
                row_tmp += 1
            elif row_tmp == numRows - 1 and go == 1:
                row_tmp -= 1
                go = -1
            elif row_tmp > 0 and go == -1:
                row_tmp -= 1
            else:
                row_tmp += 1
                go = 1
        return "".join([i for i in res.values()])


if __name__ == '__main__':
    s = Solution()
    r = s.convert("PAYPALISHIRING", 3)
    print(f"res:{r}")
    r = s.convert("PAYPALISHIRING", 4)
    print(f"res:{r}")
    r = s.convert("a", 1)
    print(f"res:{r}")
    r = s.convert("ab", 2)
    print(f"res:{r}")
