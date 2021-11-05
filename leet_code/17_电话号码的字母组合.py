class Solution:
    @staticmethod
    def letterCombinations(digits: str):
        if len(digits) == 0:
            return []
        phone_map = {
            "2": "abc",
            "3": "def",

        }
        res = list()
        global tmp
        tmp = list()

        def track_back(index):
            global tmp
            print(index, tmp)
            if index == len(digits):
                res.append("".join(tmp))
            else:
                for i in phone_map[digits[index]]:
                    tmp.append(i)
                    track_back(index + 1)
                    tmp = tmp[:-1]
                    # tmp.pop()

        track_back(0)
        return res


if __name__ == '__main__':
    r = "23"
    s = Solution()
    print(s.letterCombinations(r))
