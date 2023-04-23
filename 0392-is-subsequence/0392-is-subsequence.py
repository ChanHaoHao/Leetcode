class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indexT, found=0, 0
        for x in s:
            while indexT<len(t):
                if t[indexT]==x:
                    found+=1
                    indexT+=1
                    break
                indexT+=1
        if found==len(s):
            return True
        return False