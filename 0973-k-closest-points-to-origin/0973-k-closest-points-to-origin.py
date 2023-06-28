class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # if len(points) equals the number of points we need to return
        if k==len(points):
            return points
        distance=[]
        
        # save the distance and cordinates in the same list, then heapify it
        # it will be heapified using the first element of the sublist
        for cord in points:
            distance.append([cord[0]*cord[0]+cord[1]*cord[1], cord])
            
        heapq.heapify(distance)
        ans=[]
        while len(ans)<k:
            ans.append(heapq.heappop(distance)[1])
        return ans