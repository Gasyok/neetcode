from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        if not curr:
            return

        def printing(root):
            while root:
                print(root.val, end=" ")
                root = root.next
            print()

        arr = []
        ptr = head
        while ptr:
            arr.append(ptr)
            ptr = ptr.next

        # print(len(arr))
        left = 0
        right = len(arr) - 1
        auto = True

        while left < right:
            if auto:
                # print(arr[left].val)
                arr[left].next = arr[right]
                auto = False
                left += 1
            else:
                arr[right].next = arr[left]
                auto = True
                right -= 1

        arr[left].next = None
        # printing(head)


x = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# x = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# x = ListNode()

Solution().reorderList(x)
# root = x
# while root:
#     print(root.val)
#     root = root.next
