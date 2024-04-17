# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.smallestString = ""
        def dfs(root, currentString):
            if not root:
                return 
            
            currentString = chr(root.val+97)+currentString

            # if it is the leaf node
            if not root.left and not root.right:
                # check lexicography
                if not self.smallestString or self.smallestString>currentString:
                    self.smallestString = currentString
            else:
                dfs(root.left, currentString)
                dfs(root.right, currentString)
        
        dfs(root, "")

        return self.smallestString