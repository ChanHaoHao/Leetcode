class UnionFind:
    def __init__(self, father, size):
        # father stores the parent of the current node
        # size stores the size of the union
        self.father = father
        self.size = size
    
    def find(self, node):
        # if we have been to the upper parent of the union
        if node == self.father[node]:
            return node
        # else keep get to the parent
        self.father[node] = self.find(self.father[node])
        return self.father[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        # if the roots are unioned already
        if root1==root2:
            return 0
        
        # determine whick union is greater and union the smaller one into the larger one
        if self.size[root1]>self.size[root2]:
            self.father[root2] = root1
            self.size[root1] += self.size[root2]
        else:
            self.father[root1] = root2
            self.size[root2] += self.size[root1]
        return 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        father = [node for node in range(len(isConnected))]

        unionfind = UnionFind(father, [1]*(len(isConnected)+1))
        result = len(father)
        
        for x in range(len(father)):
            for y in range(len(father)):
                if isConnected[x][y]==1:
                    result -= unionfind.union(x, y)
        
        return result