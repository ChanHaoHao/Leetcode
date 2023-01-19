class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        #limit time exceed
        if k==len(cardPoints):
            return sum(cardPoints)
        ans=sum(cardPoints[0:k])
        if sum(cardPoints[len(cardPoints)-k::])>ans:
            ans=sum(cardPoints[len(cardPoints)-k::])
        tmp2=sum(cardPoints[0:k])
        for x in range(1,k):
            tmp=sum(cardPoints[0:x])+sum(cardPoints[len(cardPoints)-k+x::])
            if tmp>ans:
                ans=tmp
        return ans
        """

        n=len(cardPoints)
        #start the remains from 0~n-k-1
        remain=sum(cardPoints[:n-k])
        minRemain=remain
        #shift the window from 0~n-k-1 to k~n-1
        for x in range(n-k,n):
            remain+=cardPoints[x]
            remain-=cardPoints[x-n+k]
            minRemain=min(minRemain, remain)
            
        return sum(cardPoints)-minRemain