# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # used to count the sum of each level
        def dfs_sum(root, depth):
            if not root:
                return
            m[depth]+=root.val
            dfs_sum(root.left, depth+1)
            dfs_sum(root.right, depth+1)

        # used to count the cousins
        def dfs_cousins(root, depth, curr):
            # get the sum of the below level
            sum_of_cousins=m[depth+1]
            # remove itself and its brother, leaving only the cousins
            if root.left:
                sum_of_cousins-=root.left.val
            if root.right:
                sum_of_cousins-=root.right.val

            # create the node for return and dfs
            if root.left:
                curr.left=TreeNode(sum_of_cousins)
                dfs_cousins(root.left, depth+1, curr.left)
            if root.right:
                curr.right=TreeNode(sum_of_cousins)
                dfs_cousins(root.right, depth+1, curr.right)

            return curr
        
        m=Counter()
        dfs_sum(root, 0)
        return dfs_cousins(root, 0, TreeNode(0))