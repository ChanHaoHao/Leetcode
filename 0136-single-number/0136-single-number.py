class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for x in nums[1::]:
            # use XOR, the duplicate number will be removed 
            ans ^= x

        return ans