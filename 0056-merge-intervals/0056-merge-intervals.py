class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        n = len(intervals)
        i = 0
        while i<n-1:
            if intervals[i][1]>=intervals[i+1][0]:
                if intervals[i][1] < intervals[i+1][1]:
                    intervals[i][1] = intervals[i+1][1]
                intervals.pop(i+1)
                n = len(intervals)
            else:
                i += 1

        return intervals