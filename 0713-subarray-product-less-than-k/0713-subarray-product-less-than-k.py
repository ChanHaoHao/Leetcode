class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # O(n^2) TLE
        ans = 0

        for x in range(len(nums)):
            tmp = 1
            end = True
            for y in range(x, len(nums)):
                tmp *= nums[y]
                if tmp>=k:
                    end = False
                    ans += y-x
                    break
            
            # if a index can go through the rest of the index means that all the rest will be less than k
            if end:
                for y in range(x, len(nums)):
                    ans += len(nums)-y
                return ans

        return ans