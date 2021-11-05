#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
#


class Solution:
    @staticmethod
    def LRU(operators, k):
        data_lt = [0 for i in range(k)]
        index_lt = [i for i in range(k)]
        print(data_lt, index_lt)


if __name__ == '__main__':
    res = Solution.LRU([[1, 1, 1], [1, 2, 2], [1, 3, 2], [2, 1], [1, 4, 4], [2, 2]], 3)
    print(res)
    # [1, -1]
