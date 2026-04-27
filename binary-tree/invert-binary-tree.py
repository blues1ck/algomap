from typing import Optional

# # Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(curr_root):
            curr_root.left, curr_root.right = curr_root.right, curr_root.left
            if curr_root.left is not None:
                dfs(curr_root.left)
            if curr_root.right is not None:
                dfs(curr_root.right)
        if root is None:
            return None
        dfs(root)
        return root

def dfs(curr_root):
    print(curr_root.val)
    if curr_root.left is not None:
        dfs(curr_root.left)
    if curr_root.right is not None:
        dfs(curr_root.right)
    
def bfs(curr_root):
    q = deque()
    q.append(curr_root)
    while q:
        for _ in range(len(q)):
            next_node = q.popleft()
            if next_node is not None:
                print(next_node.val)
                q.append(next_node.left)
                q.append(next_node.right)


A = TreeNode(val=4)
B = TreeNode(val=5)
C = TreeNode(val=6)
D = TreeNode(val=7)
E = TreeNode(val=2, left=A, right=B)
F = TreeNode(val=3, left=C, right=D)
G = TreeNode(val=1, left=E, right=F)
a = Solution()
a.invertTree(G)
bfs(G)