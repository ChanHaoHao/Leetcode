# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # store the Tree into a graph
        graph = {}
        graph[root] = []
        leaf = set()

        # traverse the tree, find the neighbors and find the leaf nodes
        def traverseTree(root):
            # if a leaf node is reached
            if not root.left and not root.right:
                leaf.add(root)
                return

            if root.left:
                if root.left not in graph:
                    graph[root.left] = []
                # add the neighbor into the graph
                graph[root.left].append(root)
                graph[root].append(root.left)
                traverseTree(root.left)

            if root.right:
                if root.right not in graph:
                    graph[root.right] = []
                graph[root.right].append(root)
                graph[root].append(root.right)
                traverseTree(root.right)
        
        traverseTree(root)
        ans = 0

        # go through all the leaf nodes in bfs
        for x in leaf:
            # keep a record of which node is passed
            passed = set()
            queue = deque()
            queue.append(x)
            passed.add(x)
            dist = 0

            # bfs
            while len(queue)!=0:
                n = len(queue)
                for y in range(n):
                    node = queue.popleft()
                    passed.add(node)
                    if node in leaf and dist!=0:
                        print(node.val, x.val)
                        ans += 1
                    else:
                        for z in graph[node]:
                            if z not in passed:
                                queue.append(z)
                if distance==dist:
                    break
                dist+=1
        return ans//2

