class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        # store the highest possible score for the current value, -1 for the initial dist
        high = values[0]-1
        n = len(values)
        for x in range(1, n):
            # each score will be high+cur_value
            res = max(res, high+values[x])
            # update the highest possible score for the remainings
            high = max(high, values[x])
            high -= 1
        
        return res