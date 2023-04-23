class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        changeDict={}
        usedT=[]
        for x in range(len(s)):
            if s[x] not in changeDict:
                if t[x] in usedT:
                    return False
                changeDict[s[x]]=t[x]
                usedT.append(t[x])
            else:
                if changeDict[s[x]]!=t[x]:
                    return False
        return True