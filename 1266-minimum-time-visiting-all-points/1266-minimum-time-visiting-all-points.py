class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0

        for i in range(len(points)-1):
            dx = abs(points[i][0] - points[i+1][0])
            dy = abs(points[i][1] - points[i+1][1])
            time += dx + dy - min(dx, dy)
        
        return time