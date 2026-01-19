class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        prefix1 = [0]*(len(s)+1)
        for i in range(len(s)):
            prefix1[i+1] = prefix1[i] + (1 if s[i]=="1" else 0)
        
        res = len(s)
        flip = []
        for i in range(0, len(s)+1):
            res = min(res, prefix1[i] + (len(s) - i - prefix1[-1]+prefix1[i]))
        return res