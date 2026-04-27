from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def path_sum(root, tmp_sum = 0):
            tmp_sum += root.val
            if root.left is None and root.right is None:
                nonlocal targetSum
                return tmp_sum == targetSum
            a = False 
            b = False
            if root.left is not None:
                a = path_sum(root.left, tmp_sum=tmp_sum)
            if root.right is not None:
                b = path_sum(root.right, tmp_sum=tmp_sum)
            return a or b
        
        if root is None:
            return False

        return path_sum(root)
            

