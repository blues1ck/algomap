from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return None
        if root.left is not None:
            ans = abs(root.val - root.left.val)
        elif root.right is not None:
            ans = abs(root.val - root.right.val)
        else:
            return None 
        prev = None

        def dfs(root):
            nonlocal ans, prev
            if root is None:
                return
            dfs(root.left)
            if prev is not None:
                ans = min(ans, abs(root.val - prev))
            prev = root.val
            dfs(root.right)


        dfs(root)
        return ans


def dfs(root):
    if root.left is not None:
        prev = dfs(root.left)
    print(root.val)
    if root.right is not None:
        prev = dfs(root.right)


a = TreeNode(0)
b = TreeNode(6)
c = TreeNode(12)
d = TreeNode(18)
e = TreeNode(2, a, b)
f = TreeNode(15, c, d)
g = TreeNode(7, e, f)
dfs(g)