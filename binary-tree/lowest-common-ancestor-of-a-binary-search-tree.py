# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', 
            p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            nonlocal p, q
            if p.val == node.val or q.val == node.val:
                return node
            elif p.val > node.val and q.val > node.val:
                if node.right is not None:
                    return dfs(node.right)
                else:
                    return
            elif p.val < node.val and q.val < node.val:
                if node.left is not None:
                    return dfs(node.left)
                else:
                    return
            else:
                return node 
        
        return dfs(root)