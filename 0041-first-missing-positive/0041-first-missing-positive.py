class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Place each positive integer i at index i-1 if possible
        for i in range(n):
            # the only possible answer lies only between [1, n+1]
            # the second condition will fail when the number at the right index is found
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                tmp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[tmp-1] = tmp
        
        # Find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positive integers from 1 to n are present, return n + 1
        return n + 1