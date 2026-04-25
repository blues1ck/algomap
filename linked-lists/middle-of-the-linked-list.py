import itertools
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head
        middle = head
        iterator = 0
        while curr.next is not None:
            iterator += 1
            if iterator % 2 == 1:
                middle = middle.next
            curr = curr.next
        return middle

def print_ll(head):
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
print_ll(a.middleNode(l1))
print_ll(l1)



