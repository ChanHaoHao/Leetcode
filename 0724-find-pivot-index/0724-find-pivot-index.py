class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        leftsum, rightsum=0, sum(nums)
        for x in range(0, len(nums)):
            if x-1>=0:
                leftsum+=nums[x-1]
            if x+1<len(nums):
                rightsum-=nums[x]
            else:
                rightsum=0
            if leftsum==rightsum:
                return x
        return -1
        