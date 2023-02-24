import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        
        pq=[-num*2 if num%2==1 else -num for num in nums]
        heapq.heapify(pq)
        min_val=float('inf')
        for num in nums:
            min_val=min(min_val, num if num%2==0 else num*2)
        min_deviation=float('inf')

        while True:
            max_val=-heapq.heappop(pq)
            if (max_val-min_val<min_deviation):
                min_deviation=max_val-min_val

            if max_val%2==1:
                break

            min_val=min(min_val, max_val/2)
            heapq.heappush(pq, -max_val/2)

        return int(min_deviation)