class Solution:
    def splitArray(self, nums: List[int]) -> int:
        max_num_index = nums.index(max(nums))

        for i in range(max_num_index):
            if nums[i]>=nums[i+1]:
                return -1
        for i in range(max_num_index+1, len(nums)-1):
            if nums[i]<=nums[i+1]:
                return -1
        
        if max_num_index<len(nums)-1 and nums[max_num_index]==nums[max_num_index+1]:
            return abs(sum(nums[:max_num_index+1]) - sum(nums[max_num_index+1:]))

        diff1 = abs(sum(nums[:max_num_index]) - sum(nums[max_num_index:]))
        diff2 = abs(sum(nums[:max_num_index+1]) - sum(nums[max_num_index+1:]))

        return min(diff1, diff2)