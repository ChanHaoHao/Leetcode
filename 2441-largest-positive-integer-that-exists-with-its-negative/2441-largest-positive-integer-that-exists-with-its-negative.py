class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # store the candidates in storage
        # storage = set()
        # ans = 0

        # for x in nums:
        #     if -x in storage:
        #         storage.remove(-x)
        #         if abs(x)>ans:
        #             ans = abs(x)
        #     else:
        #         storage.add(x)
        
        # if ans==0:
        #     return -1
        # return ans

        nums.sort()
        left, right = 0, len(nums)-1
        ans = -1

        while left<right:
            if nums[left]+nums[right]==0:
                if ans<nums[right]:
                    ans = nums[right]
                left+=1
                right-=1
            elif nums[left]+nums[right]<0:
                left+=1
            else:
                if nums[left]>0:
                    break
                right-=1
        return ans