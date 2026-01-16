class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        count = 0
        for i in nums:
            if count < 0:
                count = 0
            count += i
            ans = max(ans, count)
        
        return ans