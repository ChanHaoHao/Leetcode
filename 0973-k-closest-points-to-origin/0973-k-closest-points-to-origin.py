class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use a max_heap to push longer distant points out when size exceed k
        max_heap = []

        for p in points:
            dist = sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(max_heap, (-dist, p))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        ans = []
        while len(max_heap)!=0:
            (_, point) = max_heap.pop()
            ans.append(point)
        return ans