# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        path = dict()
        odd = 0

        def dfs(root):
            nonlocal odd
            if not root:
                return 0

            # add the value into the path
            if root.val not in path:
                path[root.val] = 1
            else:
                path[root.val] += 1

            # count how many odds are there after adding the current node
            if path[root.val]%2:
                odd += 1
            else:
                odd -= 1

            # if this is the last node of the path
            if not root.left and not root.right:
                if odd <= 1:
                    ans = 1
                else:
                    ans = 0
            else:
                ans = dfs(root.left) + dfs(root.right)

            # after dealing with the node, remove it from the path
            if path[root.val]%2:
                odd -= 1
            else:
                odd += 1
            path[root.val] -= 1
            return ans

        return dfs(root)