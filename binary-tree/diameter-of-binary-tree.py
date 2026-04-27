from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(curr_root):
            nonlocal diameter
            if curr_root is None:
                return 0
            left_depth = dfs(curr_root.left)
            right_depth = dfs(curr_root.right)
            diameter = max(diameter, left_depth + right_depth)
            depth = 1 + max(left_depth, right_depth)
            return depth

        diameter = 0
        dfs(root)
        return diameter

M = TreeNode(val = 10)
A = TreeNode(val=4, left = M)
B = TreeNode(val=5)
C = TreeNode(val=6)
D = TreeNode(val=7)
E = TreeNode(val=2, left=A, right=B)
F = TreeNode(val=3, left=C, right=D)
G = TreeNode(val=1, left=E, right=F)
a = Solution()
print(a.diameterOfBinaryTree(G))