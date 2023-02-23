import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # mycode, should have used heapq to accelerate
        # merged=list(zip(capital, profits))
        # merged=[list(t) for t in merged]
        # merged=sorted(merged)

        # while k>0:
        #     canBeDone=[arr for arr in merged if arr[0]<=w]
        #     if (len(canBeDone)==0):
        #         break
        #     canBeDone=sorted(canBeDone, key=lambda x: x[1])
        #     w+=canBeDone[-1][1]
        #     merged.pop(merged.index(canBeDone[-1]))
        #     k-=1

        # return w

        merged=[[capital[i], profits[i]] for i in range(len(profits))]
        merged.sort()
        pq=[]
        i=0
        for _ in range(k):
            while i<len(profits) and merged[i][0]<=w:
                heapq.heappush(pq, -merged[i][1])
                i+=1
            if not pq:
                break
            w-=heapq.heappop(pq)

        return w