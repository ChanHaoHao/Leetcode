# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # use dfs to find all the leaves on the depth
        def dfs(root, cur_level):
            if not root:
                return

            # if the depth is found, add the nodes
            if cur_level==depth-1:
                left_node = root.left
                right_node = root.right
                root.left = TreeNode(val, left_node, None)
                root.right = TreeNode(val, None, right_node)
                return
            
            # if the depth is not reached, go further
            dfs(root.left, cur_level+1)
            dfs(root.right, cur_level+1)

        # wrote another method using bfs
        def bfs():
            q = [[root, 1]]

            while q:
                current = q.pop()
                # if the depth is reached, add the nodes
                if current[1]==depth-1:
                    left_node = current[0].left
                    right_node = current[0].right
                    current[0].left = TreeNode(val, left_node, None)
                    current[0].right = TreeNode(val, None, right_node)
                else:
                    if current[0].left:
                        q.append([current[0].left, current[1]+1])
                    if current[0].right:
                        q.append([current[0].right, current[1]+1])

        if depth==1:
            start_node = TreeNode(val, root, None)
            return start_node
        
        dfs(root, 1)
        # bfs()

        return root
            