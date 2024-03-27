# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # my method, use len(path) will greatly slow down the program
        # def dfs(root, path):
        #     if root is None:
        #         if len(path)-1>self.ans:
        #             self.ans = len(path)-1
        #         return
            
        #     if path[-1]=="l":
        #         # if it goes zigzag, keep going, else restart the path
        #         dfs(root.right, path+"r")
        #         dfs(root.left, "l")
        #     else:
        #         dfs(root.left, path+"l")
        #         dfs(root.right, "r")

        # self.ans = 0
        # dfs(root.left, "l")
        # dfs(root.right, "r")

        # return self.ans

        self.ans = 0
        def dfs(root, dir, size):
            self.ans = max(self.ans, size)

            if root.left is not None:
                if dir=="l":
                    dfs(root.left, "l", 1)
                else:
                    dfs(root.left, "l", size+1)

            if root.right is not None:
                if dir=="r":
                    dfs(root.right, "r", 1)
                else:
                    dfs(root.right, "r", size+1)

        dfs(root, "", 0)

        return self.ans