class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = nums[0:k]

        heapq.heapify(max_heap)
        for x in range(k, len(nums)):
            # if the value is greater than the min in heap
            # pop the min out and push the curr value in
            heapq.heappushpop(max_heap, nums[x])
        
        return heapq.heappop(max_heap)