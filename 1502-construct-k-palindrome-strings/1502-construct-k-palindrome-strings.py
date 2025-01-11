class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        
        chars = Counter(s)
        odd = 0
        for x in chars:
            if chars[x]%2==1:
                odd += 1
        if odd>k:
            return False

        return True
