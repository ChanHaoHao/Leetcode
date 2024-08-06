class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # first sort the intervals by their ending time
        # so that we guarentee [2,3], [3,4] won't be behind [2,4]
        intervals.sort(key=lambda x: x[1])
        count = 1
        prev = 0

        for i in range(1, len(intervals)):
            if intervals[i][0]>=intervals[prev][1]:
                prev = i
                count += 1
        
        return len(intervals)-count