# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            # this checks if we are at the end of a branch or found the node
            if root is None or root==p or root==q:
                return root

            l = dfs(root.left)
            r = dfs(root.right)

            # if we found p and q in the current subtree of the current node
            # it means that we got the lca
            if l and r:
                return root

            return l or r
            
        return dfs(root)