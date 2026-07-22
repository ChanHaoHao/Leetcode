class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i, n in enumerate(nums):
            heapq.heappush(heap, (n, i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [val for val, idx in sorted(heap, key=lambda x: x[1])]