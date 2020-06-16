class Solution:
    def permutation(self, S: str):
        dic = {}
        for s in S:
            dic[s] = dic.get(s, 0) + 1
        res = []

        def generate(curStr: str):
            if sum(dic.values()) == 0:
                res.append(curStr)
            for char, num in dic.items():
                if num != 0:
                    dic[char] -= 1
                    generate(curStr + char)
                    dic[char] += 1  # 恢复现场

        generate("")
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.permutation("qwefs")
    print(res)
