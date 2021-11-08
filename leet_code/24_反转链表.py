# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # if not head or not head.next:
        #     return head
        pri_pod = None

        while head:
            temp = head.next

            head.next = pri_pod
            pri_pod = head

            head = temp
        return pri_pod


if __name__ == '__main__':
    s = Solution()

    r = s.reverseList(
        ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(5, ListNode(9, ))))))),
    )
    print(f"true res:{r.val, r.next.val, r.next.next.val, r.next.next.next.val}")
