# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = [(root, root.val)]

        while queue:
            node, s = queue.pop()

            if not node.left and not node.right:
                if s==targetSum:
                    return True

            if node.left:
                queue.append((node.left, s+node.left.val))
            if node.right:
                queue.append((node.right, s+node.right.val))
        
        return False