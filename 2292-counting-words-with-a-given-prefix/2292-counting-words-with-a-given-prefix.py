class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        n = len(pref)
        for x in words:
            if x[:n]==pref:
                ans += 1
        
        return ans