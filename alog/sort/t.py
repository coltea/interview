def heap_sort(lt):
    l = len(lt)
    for i in range((l - 2) // 2, -1, -1):
        heap_sink(lt, l, i)
    print("构建完成:", lt)
    for i in range(l - 1, -1, -1):
        print(i)
        lt[i], lt[0] = lt[0], lt[i]
        heap_sink(lt, i, 0)


def heap_sink(heap, heap_max_size, parent_index):
    print(heap, heap_max_size, parent_index)
    ori_parent_node = heap[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < heap_max_size:
        if child_index + 1 < heap_max_size and heap[child_index] < heap[child_index + 1]:
            child_index += 1
            print("改用右节点:", child_index)

        if ori_parent_node >= heap[child_index]:
            break

        heap[parent_index] = heap[child_index]

        parent_index = child_index
        child_index = 2 * parent_index + 1

    heap[parent_index] = ori_parent_node
    print("end:", heap, heap_max_size, parent_index)
    return


if __name__ == '__main__':
    a = [8, 9, 1, 4, 10]
    heap_sort(a)
    print(a)
