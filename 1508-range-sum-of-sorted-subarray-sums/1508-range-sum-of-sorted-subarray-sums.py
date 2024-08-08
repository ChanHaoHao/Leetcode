class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        window = []
        heapq.heapify(window)

        for x in range(n):
            sub_num = 0
            for y in range(x, n):
                sub_num -= nums[y]
                heapq.heappush(window, sub_num)
                if len(window)>right:
                    heapq.heappop(window)
        
        window.sort(reverse=True)
        
        return -sum(window[left-1:right])%(10**9+7)