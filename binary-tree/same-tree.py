from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def bfs(p, q):
            qs = deque()
            qs.append(q)
            ps = deque()
            ps.append(p)
            while qs:
                for _ in range(len(qs)):
                    next_node_q = qs.popleft()
                    next_node_p = ps.popleft()
                    if next_node_q is None and next_node_p is None:
                        continue
                    if next_node_q is None or next_node_p is None:
                        return False       
                    if next_node_p.val != next_node_q.val:
                        return False
                    qs.append(next_node_q.left)
                    qs.append(next_node_q.right)
                    ps.append(next_node_p.left)
                    ps.append(next_node_p.right)
            return True
        
        return bfs(p, q)


