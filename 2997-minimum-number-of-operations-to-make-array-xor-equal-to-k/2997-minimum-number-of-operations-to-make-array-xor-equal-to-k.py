class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        tmp = nums[0]

        # find out all the xor result for nums
        for x in nums[1::]:
            tmp ^= x
        
        # get the difference between the result and k
        diff = bin(tmp^k)
        ans = 0
        for x in diff[2::]:
            if x=='1':
                ans += 1
        
        return ans