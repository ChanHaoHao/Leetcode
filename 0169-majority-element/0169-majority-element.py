class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2

        count = {}
        for x in nums:
            if x not in count:
                count[x] = 0
            count[x] += 1
            if count[x]>n:
                return x
        