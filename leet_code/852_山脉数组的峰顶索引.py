class Solution:

    @staticmethod
    def peakIndexInMountainArray(arr):
        t = arr[0]
        e_t = 0
        for i in arr[1:]:
            if t > i:
                break
            else:
                e_t += 1
                t = i
        return e_t


if __name__ == '__main__':
    grid = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
    res = Solution.peakIndexInMountainArray(grid)
    print(res)

    grid = [0,10,5,2]
    res = Solution.peakIndexInMountainArray(grid)
    print(res)
