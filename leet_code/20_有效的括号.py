class Solution:
    def isValid(self, s: str) -> bool:
        lt = [s[0]]
        map_dt = {
            "]": "[",
            "}": "{",
            ")": "(",
        }
        for i in s[1:]:
            # print(i,lt)
            if i in ["(", '[', '{']:
                lt.append(i)
            else:
                if len(lt) == 0:
                    return False
                if map_dt[i] == lt[-1]:
                    lt = lt[:-1]
                else:
                    return False
        if len(lt) == 0:
            return True
        return False


if __name__ == '__main__':
    # t = ["()", "()[]{}", "(]", "([)]", "{[]}",'[']
    t = ["{[]}"]
    for i in t:
        s = Solution()
        print(s.isValid(i))
