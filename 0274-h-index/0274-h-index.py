class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # count how many times a citation has happened
        count = Counter(citations)
        keys = sorted(count.keys())
        papers = len(citations)
        
        ans = 0
        for key in range(keys[-1]+1):
            if papers>=key:
                ans = key
            if key in keys:
                papers -= count[key]
        
        return ans