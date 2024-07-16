class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        merged_list = list(zip(nums1, nums2))
        # this allows the merged_list to sort by x[1], then x[0] and in the reverse order
        merged_list.sort(key=lambda x:(-x[1], -x[0]))

        # initialize the process
        ans, presum = 0, 0
        heap = []
        heapq.heapify(heap)
        for x in range(k-1):
            presum += merged_list[x][0]
            heapq.heappush(heap, merged_list[x][0])
        
        n = len(nums1)
        for x in range(k-1, n):
            presum += merged_list[x][0]
            heapq.heappush(heap, merged_list[x][0])
            # because nums2 is sorted in the reverse order, so the minimum will always be the last number of nums2
            ans = max(presum*merged_list[x][1], ans)
            # remove the minimum in nums1
            presum -= heapq.heappop(heap)

        return ans

        return 0