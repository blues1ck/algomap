from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        # 1) A -> A' -> B -> B' -> ...
        curr = head
        while curr is not None:
            nxt = curr.next
            copy = Node(curr.val, nxt)
            curr.next = copy
            curr = nxt

        # 2) random у копии: если у оригинала random -> R, то у копии -> R.next (это копия R)
        curr = head
        while curr is not None:
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # 3) разрезать список
        dummy = Node(0)
        tail = dummy
        curr = head
        while curr is not None:
            copy = curr.next
            nxt = copy.next
            curr.next = nxt
            tail.next = copy
            tail = copy
            curr = nxt

        return dummy.next


def print_ll(head):
    if head is None:
        print()
        return
    curr = head
    while curr.next is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print(curr.val)


a = Solution()
l9 = Node(12)
l8 = Node(11, l9)
l7 = Node(9, l8)
l6 = Node(7, l7)
l5 = Node(5, l6)
l4 = Node(4, l5)
l3 = Node(4, l4)
l2 = Node(2, l3)
l1 = Node(1, l2)
print_ll(l1)
print_ll(a.copyRandomList(l1))
