class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heapify dist after it is calculated will be better
        dist = []
        for point in points:
            dist.append((point[0]**2+point[1]**2, point))
        dist = sorted(dist)

        ans = []
        for i in range(k):
            ans.append(dist[i][1])
        return ans