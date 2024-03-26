# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0

        # using dfs to go through all the paths and store the possible results in an array
        def dfs(root, array):
            if root is None:
                return
            
            for x in range(len(array)):
                array[x]+=root.val
                if array[x]==targetSum:
                    self.ans+=1
            array.append(root.val)
            if array[-1]==targetSum:
                self.ans+=1

            dfs(root.right, array.copy())
            dfs(root.left, array.copy())

        dfs(root, [])
       
        return self.ans
                