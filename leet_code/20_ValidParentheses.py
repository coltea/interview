class Solution:
    def isValid(self, s: str) -> bool:
        left_lt = ["(", "[", "{"]
        right_lt = [")", "]", "}"]
        temp = []
        for i in s:
            if i in left_lt:
                temp.append(i)
            else:
                if len(temp) == 0:
                    return False
                elif right_lt.index(i) == left_lt.index(temp.pop()):
                    continue
                else:
                    return False
        if len(temp) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    t = ["()", "()[]{}", "(]", "([)]", "{[]}",'[']
    for i in t:
        s = Solution()
        print(s.isValid(i))




