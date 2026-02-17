class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        start, end = intervals[0][0], intervals[0][1]
        for i in intervals[1:]:
            if i[0] <= end:
                end = max(end, i[1])
            else:
                ans.append([start, end])
                start, end = i[0], i[1]
        ans.append([start, end])
        
        return ans