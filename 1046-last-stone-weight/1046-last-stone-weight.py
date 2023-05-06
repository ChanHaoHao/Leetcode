class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for x in range(len(stones)):
            stones[x]*=-1
        heapq.heapify(stones)
        while len(stones)>1:
            tmp1=heapq.heappop(stones)
            tmp2=heapq.heappop(stones)

            if tmp1==tmp2:
                continue
            else:
                heapq.heappush(stones, tmp1-tmp2)
        if len(stones)==0:
            return 0
        else:
            return -stones[0]