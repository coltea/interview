# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head.next or not head:
            return None
        follow = None
        while head:
            next_head = head.next  # 存储下一位 方便下次循环计算计算

            head.next = follow  # 该方向
            follow = head  # 标志位右移

            head = next_head  # 切换到下一位 用于下次循环计算
        return follow


if __name__ == '__main__':
    s = Solution()

    r = s.reverseList(
        ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(5, ListNode(9, ))))))),
    )
    print(f"true res:{r.val, r.next.val, r.next.next.val, r.next.next.next.val}")
