class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 26:
            columnNumber, n = divmod(columnNumber, 26)
            if n == 0:
                res.append(26)
                columnNumber
            else:
                res.append(n)
        res.append(columnNumber)
        lt = res[::-1]
        print(lt)
        return ''.join([chr(i+96).upper() for i in lt])


if __name__ == '__main__':
    s = Solution()
    # print(s.convertToTitle(1))
    print(s.convertToTitle(26))
    # print(s.convertToTitle(28))
    print(s.convertToTitle(52))
    # print(s.convertToTitle(701))
    # print(s.convertToTitle(2147483647))
