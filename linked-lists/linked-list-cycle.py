from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        st = set()
        curr = head
        while curr.next is not None:
            if curr.next in st:
                return True
            st.add(curr.next)
            curr = curr.next
        return False


a = Solution()
l5 = ListNode(8)
l4 = ListNode(6)
l4.next = l5
l3 = ListNode(4)
l3.next = l4
l2 = ListNode(2)
l2.next = l3
l1 = ListNode(0)
l1.next = l2

print(a.hasCycle(l1))