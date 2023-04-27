"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(root, ans):
            if not root:
                return
            ans.append(root.val)
            children=root.children
            while children:
                dfs(children.pop(0), ans)

        ans=[]
        dfs(root, ans)
        return ans
        