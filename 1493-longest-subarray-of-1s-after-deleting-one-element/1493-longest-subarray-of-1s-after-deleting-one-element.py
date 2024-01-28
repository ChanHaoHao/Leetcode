class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # a question similar to question 1005
        l, r, k = 0, 0, 1
        
        for r in range(len(nums)):
            if nums[r]==0:
                k -= 1

            if k<0:
                if nums[l]==0:
                    k += 1
                l += 1
        return r-l
