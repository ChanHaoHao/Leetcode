class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # using heap will cause TLE
        # pair_dist = []
        # heapq.heapify(pair_dist)

        # for x in range(len(nums)-1):
        #     for y in range(x+1, len(nums)):
        #         heapq.heappush(pair_dist, -abs(nums[y]-nums[x]))
        #         if len(pair_dist)>k:
        #             heapq.heappop(pair_dist)
        
        # return -heapq.heappop(pair_dist)

        nums.sort()

        def count_pairs(m):
            l, count = 0, 0
            for r in range(len(nums)):
                while nums[r]-nums[l]>m:
                    l+=1
                count += r-l
            return count

        l, r = 0, max(nums)
        while l<r:
            m = (l+r)//2

            # count the pairs that is leq to m
            pairs = count_pairs(m)
            # means that kth smallest might fall here, so we set r=m
            if pairs>=k:
                r = m
            else:
                l = m+1
        return r