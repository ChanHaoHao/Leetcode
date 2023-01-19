import numpy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tmp = 1
        zeros = []
        ans = []
        for x in range(len(nums)):
            if nums[x] != 0:
                tmp *= nums[x]
            else:
                zeros.append(x)
        
        if len(zeros)>=2:
            ans = numpy.zeros(len(nums), dtype=int)
        elif len(zeros)==1:
            ans = numpy.zeros(len(nums), dtype=int)
            ans[zeros[0]] = tmp
        else:
            for x in range(len(nums)):
                ans.append(int(tmp/nums[x]))
        return ans