class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min_num = min(nums)
            nums[nums.index(min_num)] *= multiplier
        
        return nums