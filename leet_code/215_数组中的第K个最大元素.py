class Solution:
    def findKthLargest(self, nums, k) -> int:
        l = len(nums)
        for i in range((l - 2) // 2, -1, -1):
            self.heap_sink(nums, l, i)
            print("mid:", nums)

        for i in range(l - 1, -1, -1):
            if l - i == k:
                return nums[0]
            nums[i], nums[0] = nums[0], nums[i]
            self.heap_sink(nums, i, 0)
        return 0

    def heap_sink(self, heap, heap_max_size, parent_index):
        child_index = parent_index * 2 + 1
        ori_heap_node = heap[parent_index]
        while child_index < heap_max_size:
            if child_index + 1 < heap_max_size and heap[child_index] < heap[child_index + 1]:
                child_index += 1
            if ori_heap_node >= heap[child_index]:
                break

            heap[parent_index] = heap[child_index]

            parent_index = child_index
            child_index = parent_index * 2 + 1

        heap[parent_index] = ori_heap_node


if __name__ == '__main__':
    a = [5, 9, 2, 6, 7, 10, 4, 3, 1]
    print(Solution().findKthLargest(a, 4))
    # print(merge([1, 3], [2, 4]))
