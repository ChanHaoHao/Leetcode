class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        index = -1
        zeros = 0
        product = 1

        for n in range(len(nums)):
            if nums[n]==0:
                zeros += 1
                if zeros==2:
                    return ans
                index = n
            else:
                product *= nums[n]
        
        if zeros==1:
            ans[index] = product
        else:
            for i in range(len(nums)):
                ans[i] = int(product / nums[i])
        return ans