class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        
        n, i=min(len(word1), len(word2)), 0
        while i!=n:
            ans+=word1[i]+word2[i]
            i+=1
        if n<len(word1):
            ans+=word1[n::]
        elif n<len(word2):
            ans+=word2[n::]
        return ans