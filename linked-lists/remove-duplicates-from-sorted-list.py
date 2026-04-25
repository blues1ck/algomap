# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head is None:
            return head        
        if head.next is None:
            return head
        curr = head
        while curr.next is not None:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

def print_ll(head):
    curr = head
    while curr.next is not None:
        print(curr.val, end=' ')
        curr = curr.next
    print(curr.val)

a = Solution()
l5 = ListNode(5)
l4 = ListNode(4, l5)
l3 = ListNode(4, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
a.deleteDuplicates(l1)


    
