from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        dummy = ListNode(0, head)
        fast: Optional[ListNode] = head
        slow: ListNode = dummy

        for _ in range(n):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


def print_ll(head):
    if head is None:
        print()
        return
    curr = head
    while curr.next is not None:
        print(curr.val, end=' ')
        curr = curr.next
    print(curr.val)

a = Solution()
l9 = ListNode(12)
l8 = ListNode(11, l9)
l7 = ListNode(9, l8)
l6 = ListNode(7, l7)
l5 = ListNode(5, l6)
l4 = ListNode(4, l5)
l3 = ListNode(4, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
print_ll(l1)
print_ll(a.removeNthFromEnd(l1, 5))

