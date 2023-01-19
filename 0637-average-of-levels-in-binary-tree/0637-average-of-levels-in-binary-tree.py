# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans, num = defaultdict(float), defaultdict(int)
        
        def ansSum(node, h):
            if (node == None):
                return
            
            ansSum(node.left, h+1)
            ansSum(node.right, h+1)
            ans[h] += node.val
            num[h] += 1
        
        ansSum(root, 0)
        realAns = [];
        for x in range(len(ans)):
            realAns.append(ans[x]/num[x])
        return realAns