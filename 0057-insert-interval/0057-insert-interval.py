class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        merged = False
        merge = [-1, -1]
        for interval in intervals:
            # No overlap with newInterval
            if interval[1]<newInterval[0]:
                ans.append(interval)
            elif interval[0]>newInterval[1]:
                if not merged:
                    if merge[0]==-1:
                        merge[0] = newInterval[0]
                    if merge[1]==-1:
                        merge[1] = newInterval[1]
                    ans.append(merge)
                    merged = True
                ans.append(interval)
            else:
                if merge[0]==-1:
                    merge[0] = min(interval[0], newInterval[0])
                merge[1] = max(interval[1], newInterval[1])
        
        if not merged:
            if sum(merge)==-2:
                ans.append(newInterval)
            else:
                ans.append(merge)

        return ans