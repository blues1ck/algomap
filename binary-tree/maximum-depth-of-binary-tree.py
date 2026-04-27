from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(curr_root):
            if curr_root is None:
                return 0
            depth = 1 + max(dfs(curr_root.left), dfs(curr_root.right))
            return depth
        return dfs(root)

M = TreeNode(val = 10)
A = TreeNode(val=4, left = M)
B = TreeNode(val=5)
C = TreeNode(val=6)
D = TreeNode(val=7)
E = TreeNode(val=2, left=A, right=B)
F = TreeNode(val=3, left=C, right=D)
G = TreeNode(val=1, left=E, right=F)
a = Solution()
print(a.maxDepth(G))