# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        root_candidate = set()
        known_child = set()
        dict_description = dict()
        for x in descriptions:
            if x[0] not in dict_description:
                dict_description[x[0]] = [0, 0]
            
            if x[2]==1:
                dict_description[x[0]][0] = x[1]
            else:
                dict_description[x[0]][1] = x[1]

            if x[1] in root_candidate:
                root_candidate.remove(x[1])
                known_child.add(x[1])
            elif x[1] not in known_child:
                known_child.add(x[1])
            if x[0] not in root_candidate and x[0] not in known_child:
                root_candidate.add(x[0])
        
        # set is not subscriptable, so this is the only way to get
        for i in root_candidate:
            root = TreeNode(i, None, None)

        def dfs(root):
            if not root or root.val not in dict_description:
                return

            childs = dict_description[root.val]
            if childs[0]!=0:
                root.left = TreeNode(childs[0], None, None)
                dfs(root.left)
            if childs[1]!=0:
                root.right = TreeNode(childs[1], None, None)
                dfs(root.right)

        dfs(root)
        return root