class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, n = 0, len(intervals)
        ans = []
        # Seperate the intervals into 3 parts
        # First part: interval[1]<newInterval[0]
        while i<n and intervals[i][1]<newInterval[0]:
            ans.append(intervals[i])
            i += 1
        
        # Second part: Find the overlapping
        while i<n and intervals[i][0]<=newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        ans.append(newInterval)

        # Third part: non-overlap interval[0]>newInterval[1]
        while i<n:
            ans.append(intervals[i])
            i += 1
        
        return ans