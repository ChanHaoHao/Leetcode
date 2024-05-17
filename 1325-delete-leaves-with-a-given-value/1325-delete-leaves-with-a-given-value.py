# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # inspired by the hint, use dfs to remove leaf node
        def dfs(root, target):
            if root==None:
                return None

            root.left = dfs(root.left, target)
            root.right = dfs(root.right, target)

            # this will remove the leaf node
            if root.val==target and root.left==None and root.right==None:
                return None

            return root

        root = dfs(root, target)
        return root