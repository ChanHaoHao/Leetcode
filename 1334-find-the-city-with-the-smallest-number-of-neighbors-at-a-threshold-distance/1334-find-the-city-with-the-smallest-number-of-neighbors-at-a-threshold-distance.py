class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]

        # create a graph to store the relations between each cities
        for start, end, dist in edges:
            if dist<=distanceThreshold:
                graph[start].append([end, dist])
                graph[end].append([start, dist])
        
        ans, count = 0, n
        for index in range(n):
            visited = set()
            # store the possible neighbors into a min-heap, determined by distance to the current index
            queue = [(0, index)]

            while queue:
                # pop the smallest distance to current index
                dist_to_curr, curr = heapq.heappop(queue)
                if curr not in visited:
                    visited.add(curr)
                    for neighbor, dist in graph[curr]:
                        total_distance = dist_to_curr+dist
                        # add all the possible cities into the queue
                        if total_distance<=distanceThreshold:
                            heapq.heappush(queue, (total_distance, neighbor))
            
            # minus the starting city
            if len(visited)-1<=count:
                count = len(visited)-1
                ans = index

        return ans