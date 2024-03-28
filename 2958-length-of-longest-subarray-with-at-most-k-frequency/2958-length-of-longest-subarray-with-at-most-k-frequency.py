class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        window, left, right, ans = dict(), 0, 0, 0
        for right in range(len(nums)):
            if nums[right] in window:
                # while the frequency of a nums is already at its max
                while window[nums[right]]==k and left<=right:
                    window[nums[left]]-=1
                    left+=1
                window[nums[right]]+=1
            else:
                window[nums[right]]=1

            ans = max(ans, right-left+1)
        
        return ans