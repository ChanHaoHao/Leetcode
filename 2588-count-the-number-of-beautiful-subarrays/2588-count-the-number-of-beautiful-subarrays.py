class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        dp=Counter({0:1})
        res=pre=0

        for a in nums:
            # the bitwise operator xor^ will eliminate the 2^x we can subtract
            pre^=a
            # if we have reached the element before
            res+=dp[pre]
            # add the times we reached the element
            dp[pre]+=1
        return res