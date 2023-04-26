class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=collections.Counter(s)
        ans=0
        thres=False
        for x in count:
            ans+=(count[x]//2)*2
            if count[x]%2==1:
                thres=True
        if thres:
            return ans+1
        return ans