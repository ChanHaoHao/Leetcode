class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        count = Counter(s)
        
        if len(count) <= k:
            return 0
        
        sort = sorted(count.items(), key=lambda item: item[1])
    
        ans = 0
        for x in range(len(count) - k):
            ans += sort[x][1]
        
        return ans