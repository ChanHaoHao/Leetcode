class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[0:k])/k
        window = ans
        
        for x in range(k, len(nums)):
            window = window-nums[x-k]/k+nums[x]/k
            ans = max(ans, window)
        
        return ans