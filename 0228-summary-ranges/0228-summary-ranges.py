class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        for n in nums:
            if ranges and ranges[-1][1]==n-1:
                ranges[-1][1] = n
            else:
                ranges.append([n, n])
        
        ans = []
        for x, y in ranges:
            if x==y:
                ans.append(f"{x}")
            else:
                ans.append(f"{x}->{y}")
        return ans