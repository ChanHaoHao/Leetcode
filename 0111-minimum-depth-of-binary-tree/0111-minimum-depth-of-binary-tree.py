# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = -1

        def dfs(node, depth):
            nonlocal ans

            if not node.left and not node.right:
                if ans == -1:
                    ans = depth
                else:
                    ans = min(ans, depth)
            
            if (ans!=-1 and depth<ans) or ans==-1:
                if node.left:
                    dfs(node.left, depth+1)
                if node.right:
                    dfs(node.right, depth+1)
        
        if not root:
            return 0
            
        dfs(root, 1)

        return ans
