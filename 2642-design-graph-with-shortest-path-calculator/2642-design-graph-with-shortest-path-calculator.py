class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.numNodes=n
        self.paths=[[] for _ in range(n)]
        # the distance is set at first for heapq to pop the smallest costing edge for dijkstra's algorithm
        for From, To, dist in edges:
            self.paths[From].append((dist, To))

    def addEdge(self, edge: List[int]) -> None:
        self.paths[edge[0]].append((edge[2], edge[1]))

    def shortestPath(self, node1: int, node2: int) -> int:
        n, pq=self.numNodes, [(0, node1)]
        dist=[float('inf') for _ in range(self.numNodes)]
        dist[node1]=0
        
        while pq:
            d, node=heappop(pq)
            if node==node2:
                return d
            for cost, neighbor in self.paths[node]:
                newDist=d+cost
                if newDist<dist[neighbor]:
                    dist[neighbor]=newDist
                    heappush(pq, (newDist, neighbor))
        return -1
    
# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)