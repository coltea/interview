class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def sum2(a, b, jw):
        print(a, b, jw)
        if not a:
            a = 0
        if not b:
            b = 0
        if a + b + jw >= 10:
            return 1, (a + b + jw) % 10
        else:
            return 0, a + b + jw

    def addTwoNumbers(self, l1, l2):
        jw, val = self.sum2(l1.val, l2.val, 0)
        res = ListNode(val)
        t_node = res
        while 1:
            # print(t_node.val)
            if not l1.next and not l2.next and not jw:
                return res
            l1 = l1.next if l1.next else ListNode(0, None)
            l2 = l2.next if l2.next else ListNode(0, None)
            jw, val = self.sum2(l1.val, l2.val, jw)
            t_node.next = ListNode(val)
            t_node = t_node.next
            # l1.val + l2.val = sum(l1.val, l2.val)


if __name__ == '__main__':
    s = Solution()
    # r = s.addTwoNumbers(
    #     ListNode(2, ListNode(4, ListNode(3))),
    #     ListNode(5, ListNode(6, ListNode(4)))
    # )
    # print(f"res:{r.val, r.next.val, r.next.next.val}")
    r = s.addTwoNumbers(
        ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ))))))),
        ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    )
    while 1:
        print(r.val)
        r = r.next
        if not r:
            break

    # r = s.reverse(-4)
    # print(f"res:{r}")
