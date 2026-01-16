class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals = sorted(intervals)
        # n = len(intervals)
        # i = 0
        # while i<n-1:
        #     if intervals[i][1]>=intervals[i+1][0]:
        #         if intervals[i][1] < intervals[i+1][1]:
        #             intervals[i][1] = intervals[i+1][1]
        #         intervals.pop(i+1)
        #         n = len(intervals)
        #     else:
        #         i += 1

        # return intervals
        if len(intervals)<2:
            return intervals

        intervals = sorted(intervals)
        start, end = intervals[0][0], intervals[0][1]

        overlap = []
        for i in range(1, len(intervals)):
            if intervals[i][0]>end:
                overlap.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(end, intervals[i][1])
        
        overlap.append([start, end])
        return overlap