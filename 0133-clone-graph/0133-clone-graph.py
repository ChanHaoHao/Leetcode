"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # if the node is empty
        if not node:
            return node

        dq, clone = deque([node]), {node.val: Node(node.val, [])}
        # do bfs
        while dq:
            cur_node = dq.popleft()
            cur_clone = clone[cur_node.val]

            for neighbor in cur_node.neighbors:
                # found a new node
                if neighbor.val not in clone:
                    clone[neighbor.val] = Node(neighbor.val, [])
                    dq.append(neighbor)
                cur_clone.neighbors.append(clone[neighbor.val])
        
        return clone[node.val]