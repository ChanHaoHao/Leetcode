class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNumberList = [1]
        heapq.heapify(uglyNumberList)
        uglyNumberSet = set()
        uglyNumberSet.add(1)
        primeFactors = [2, 3, 5]

        for _ in range(1,n):
            curr = heapq.heappop(uglyNumberList)
            for x in primeFactors:
                if curr*x not in uglyNumberSet:
                    uglyNumberSet.add(curr*x)
                    heapq.heappush(uglyNumberList, curr*x)
        return heapq.heappop(uglyNumberList)