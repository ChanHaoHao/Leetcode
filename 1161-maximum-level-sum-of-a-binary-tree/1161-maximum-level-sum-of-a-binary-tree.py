# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root, level, levels):
            if len(levels)==level:
                levels.append(root.val)
            else:
                levels[level]+=root.val

            if root.left is not None:
                dfs(root.left, level+1, levels)
            if root.right is not None:
                dfs(root.right, level+1, levels)

            return levels
        
        result = dfs(root, 0, [])

        return result.index(max(result))+1