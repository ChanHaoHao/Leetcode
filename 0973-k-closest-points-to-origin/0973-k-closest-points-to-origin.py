class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k==len(points):
            return points
        distance=[]
        
        for cord in points:
            distance.append([cord[0]*cord[0]+cord[1]*cord[1], cord])
            
        heapq.heapify(distance)
        ans=[]
        while len(ans)<k:
            ans.append(heapq.heappop(distance)[1])
        return ans