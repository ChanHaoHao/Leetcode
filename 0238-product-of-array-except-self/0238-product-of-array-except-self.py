class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = 1
        # Each number will be the multiplication of its precount and postcount
        # take index=3 for example, it will be the multiplication of 0~2 and 4~end
        # And 0~2 will be the prefix, and 4~end will be the postfix
        # So we first iterate through with prefix, and initialize the first number with 1
        for i in range(len(nums)-1):
            ans[i+1] = ans[i] * nums[i]
        
        # Then we start to iterate through postfix
        post_count = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            ans[i] *= post_count
            post_count *= nums[i]
        return ans