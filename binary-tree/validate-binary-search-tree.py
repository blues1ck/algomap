from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, low=None, high=None):
            if root is None:
                return True
            if low is not None and root.val <= low:
                return False
            if high is not None and root.val >= high:
                return False
            res_left = dfs(root.left, low, high=root.val)
            res_right = dfs(root.right, low=root.val, high=high)
            return res_left and res_right
        
        return dfs(root)