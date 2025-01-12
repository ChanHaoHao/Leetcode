class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums)//2

        # count = {}
        # for x in nums:
        #     if x not in count:
        #         count[x] = 0
        #     count[x] += 1
        #     if count[x]>n:
        #         return x
        m, c = 0, 0

        for x in nums:
            if c==0:
                m = x
                c = 1
            elif m==x:
                c += 1
            else:
                c -= 1
        
        return m
        