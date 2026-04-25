from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        iter1 = list1
        iter2 = list2
        if iter1 is None:
            return iter2
        if iter2 is None:
            return iter1

        if iter1.val <= iter2.val:
            head = ListNode(iter1.val)
            iter1 = iter1.next
        else:
            head = ListNode(iter2.val)
            iter2 = iter2.next

        curr = head
        while iter1 is not None and iter2 is not None:
            if iter1.val <= iter2.val:
                curr.next = ListNode(iter1.val)
                iter1 = iter1.next
                curr = curr.next
            else:
                curr.next = ListNode(iter2.val)
                iter2 = iter2.next
                curr = curr.next

        while iter1 is not None:
            curr.next = ListNode(iter1.val)
            iter1 = iter1.next
            curr = curr.next

        while iter2 is not None:
            curr.next = ListNode(iter2.val)
            iter2 = iter2.next
            curr = curr.next
        return head

def print_ll(head):
    curr = head
    while curr.next is not None:
        print(curr.val, end=' ')
        curr = curr.next
    print(curr.val)

a = Solution()
l5 = ListNode(8)
l4 = ListNode(6, l5)
l3 = ListNode(4, l4)
l2 = ListNode(2, l3)
l1 = ListNode(0, l2)

a5 = ListNode(9)
a4 = ListNode(7, a5)
a3 = ListNode(5, a4)
a2 = ListNode(3, a3)
a1 = ListNode(1, a2)

print_ll(a.mergeTwoLists(a1, l1))