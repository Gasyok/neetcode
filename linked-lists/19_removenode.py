from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
            self,
            head: Optional[ListNode],
            n: int
    ) -> Optional[ListNode]:
        if not head:
            return None
        first = second = ListNode(0, head)
        for _ in range(n):
            second = second.next
        curr = first
        while second.next:
            curr = curr.next
            second = second.next
        curr.next = curr.next.next
        return first.next


x = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(Solution().removeNthFromEnd(x, 5))
