def heap_sort(lt):
    l = len(lt)
    for i in range((l - 2) // 2, -1, -1):
        heap_sink(lt, i, l)
    print("第一次构建完成:", lt)

    for i in range(l - 1, -1, -1):
        lt[0], lt[i] = lt[i], lt[0]
        heap_sink(lt, 0, i)
    print(lt)
    # return


def heap_sink(heap, parent_index, max_len):
    # if max_len != 0:
    #     print("剩余数组:", heap[:max_len])
    # print(heap, parent_index, max_len)
    ori_parent_node = heap[parent_index]
    # print(ori_parent_node)
    child_index = 2 * parent_index + 1

    while child_index < max_len:

        if child_index + 1 < max_len and heap[child_index] < heap[child_index + 1]:
            child_index += 1

        if ori_parent_node >= heap[child_index]:
            # print(parent_index, child_index)
            break

        heap[parent_index] = heap[child_index]

        parent_index = child_index
        child_index = 2 * parent_index + 1

    # print(child_index)
    heap[parent_index] = ori_parent_node
    print("end:", heap)
    return


if __name__ == '__main__':
    # a = [8, 9, 1, 4, 10]
    a = [1, 909, 4, 656, 54, 2, 912, 45]
    heap_sort(a)
    # print(a)
