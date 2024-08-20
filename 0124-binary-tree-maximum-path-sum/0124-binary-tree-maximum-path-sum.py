# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        
        self.dfs(root)
        return self.ans
    
    # search bottom up, getting the maximum of all the subtree
    def dfs(self, root):
        if not root:
            return 0

        # get the max of the left and right subtree
        leftmax = max(0, self.dfs(root.left))
        rightmax = max(0, self.dfs(root.right))

        self.ans = max(self.ans, root.val+leftmax+rightmax)

        return root.val+max(leftmax, rightmax)