# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Find the path to the node
        def dfs(root, path, value):
            if not root:
                return False

            if root.val==value:
                return True

            if root.left:
                path.append("L")
                if dfs(root.left, path, value):
                    return True
                path.pop()
            if root.right:
                path.append("R")
                if dfs(root.right, path, value):
                    return True
                path.pop()
            
            return False

        path1 = []
        path2 = []

        dfs(root, path1, startValue)
        dfs(root, path2, destValue)

        i = max(len(path1), len(path2))
        
        while len(path1)>0 and len(path2)>0:
            if path1[0]==path2[0]:
                path1.pop(0)
                path2.pop(0)
            else:
                break

        ans = "U"*len(path1)
        for x in path2:
            ans+=x
        return ans