# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # using dfs to get all the root->leaf path
        self.ans = 0

        def dfs(root, string):
            string+=str(root.val)

            if root.left or root.right:
                if root.left:
                    dfs(root.left, string)
                if root.right:
                    dfs(root.right, string)
            else:
                self.ans += int(string)

        dfs(root, "")
        return self.ans
