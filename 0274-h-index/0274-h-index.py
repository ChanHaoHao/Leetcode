class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # count how many times a citation has happened
        count = Counter(citations)
        papers = len(citations)
        
        ans = 0
        # go through all possible h-index
        for key in range(max(count.keys())+1):
            # if the remaining papers have citations greater than the h-index
            if papers>=key:
                ans = key
            # remove the papers less than h-index
            if key in count.keys():
                papers -= count[key]
        
        return ans