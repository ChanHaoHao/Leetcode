# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subTreeSum = []
        def dfs(root):
            if root==None:
                return 0

            tmp = dfs(root.left) + dfs(root.right) + root.val
            subTreeSum.append(tmp)
            return tmp

        dfs(root)
        total = max(subTreeSum)

        return max((total-x)*x for x in subTreeSum) % (10**9+7)