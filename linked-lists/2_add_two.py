from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        keep = 0
        sum = 0

        res = ListNode(0, None)

        curr = res

        while l1 or l2:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            sum = l1val + l2val + keep
            keep = sum // 10

            curr.next = ListNode(sum % 10, None)
            curr = curr.next

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        if keep:
            curr.next = ListNode(keep, None)

        return res.next


sol = Solution()

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
sol.addTwoNumbers(l1, l2)
