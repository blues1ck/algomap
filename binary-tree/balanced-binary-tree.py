from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> int:
        def dfs(curr_root):
            if curr_root is None:
                return 0
            left_depth = dfs(curr_root.left)
            right_depth = dfs(curr_root.right)
            if left_depth is False or right_depth is False:
                return False
            elif abs(left_depth - right_depth) < 2:
                depth = 1 + max(left_depth, right_depth)
                return depth
            else:
                return False
        res = dfs(root)
        if res is False:
            return False
        else:
            return True

N = TreeNode(val = 11)
M = TreeNode(val = 10, left = N)
A = TreeNode(val=4, left = M)
B = TreeNode(val=5)
C = TreeNode(val=6)
D = TreeNode(val=7)
E = TreeNode(val=2, left=A, right=B)
F = TreeNode(val=3, left=C, right=D)
G = TreeNode(val=1, left=E, right=F)
a = Solution()
print(a.isBalanced(G))