# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return
        else:
            if root.val>key:
                root.left = self.deleteNode(root.left, key)
            elif root.val<key:
                root.right = self.deleteNode(root.right, key)
            # when the key is found
            else:
                # if it only has one child
                if root.left is None:
                    root = root.right
                elif root.right is None:
                    root = root.left
                # if it has two child
                else:
                    cur = root.right
                    # replace the node with the value of the smallest value of right
                    # since the smallest value of the right subtree will be guarenteed to be 
                    # greater than the left subtree and smaller than the right subtree
                    while cur.left:
                        cur = cur.left
                    root.val = cur.val
                    root.right = self.deleteNode(root.right, cur.val)
            
            return root