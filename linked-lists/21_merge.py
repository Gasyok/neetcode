from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
            self,
            list1: Optional[ListNode],
            list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        root = curr = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next

            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next

            curr = curr.next

        if not list1:
            curr.next = list2
        if not list2:
            curr.next = list1

        return root.next


x = ListNode(1, ListNode(2, ListNode(3)))
y = ListNode(1, ListNode(1, ListNode(2)))


t = (Solution().mergeTwoLists(x, y))
root = t
while root:
    print(root.val)
    root = root.next
