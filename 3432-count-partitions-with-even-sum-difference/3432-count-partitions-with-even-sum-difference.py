class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans = 0
        left = nums[0]
        right = sum(nums[1:])
        if (right-left)%2 == 0:
            ans += 1

        i = 1
        while i<len(nums)-1:
            left += nums[i]
            right -= nums[i]
            if (right-left)%2==0:
                ans += 1
            i += 1
        
        return ans