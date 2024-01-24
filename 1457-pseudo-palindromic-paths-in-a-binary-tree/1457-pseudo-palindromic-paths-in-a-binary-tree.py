# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
ans = 0

def dfs(root, current_path):
    global ans
    if root.val not in current_path:
        current_path[root.val] = 1
    else:
        current_path[root.val] += 1
    
    if root.left or root.right:
        if root.left:
            dfs(root.left, current_path)
        if root.right:
            dfs(root.right, current_path)
    else:
        single = False
        for x in current_path:
            if current_path[x]%2:
                if single:
                    print("got single")
                    ans -= 1
                    break
                single = True
        ans += 1

    current_path[root.val] -= 1

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        global ans
        ans = 0
        dfs(root, dict())
        return ans