from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        tmp = None
        while curr.next is not None:
            next_curr = curr.next
            curr.next = tmp
            tmp = curr
            curr = next_curr
        curr.next = tmp
        return curr

def print_ll(head):
    curr = head
    while curr.next is not None:
        print(curr.val, end=' ')
        curr = curr.next
    print(curr.val)

a = Solution()
l5 = ListNode(5)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
print_ll(a.reverseList(l1))