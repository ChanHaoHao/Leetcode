class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.Kth=k
        heapq.heapify(nums)
        self.nums=nums
        # shorten the heap, since we don't care about the small ones
        while len(self.nums)>k:
            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums)>self.Kth:
            heapq.heappop(self.nums)
        return self.nums[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)