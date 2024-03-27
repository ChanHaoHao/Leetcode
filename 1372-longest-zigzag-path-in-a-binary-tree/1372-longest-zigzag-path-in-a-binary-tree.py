# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root, path):
            if root is None:
                if len(path)-1>self.ans:
                    self.ans = len(path)-1
                return
            
            if path[-1]=="l":
                # if it goes zigzag, keep going, else restart the path
                dfs(root.right, path+"r")
                dfs(root.left, "l")
            else:
                dfs(root.left, path+"l")
                dfs(root.right, "r")

        self.ans = 0
        dfs(root.left, "l")
        dfs(root.right, "r")

        return self.ans