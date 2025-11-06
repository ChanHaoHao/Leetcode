# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        l = root.left if root.left else None
        r = root.right if root.right else None

        ans = True
        def dfs(nodeL, nodeR):
            nonlocal ans
            if nodeL and not nodeR:
                ans = False
            elif not nodeL and nodeR:
                ans = False
            elif nodeL and nodeR:
                if nodeL.val!=nodeR.val:
                    ans = False
            
                dfs(nodeL.left, nodeR.right)
                dfs(nodeL.right, nodeR.left)

        dfs(l, r)

        return ans