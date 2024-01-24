class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # original idea
        # the method checking the missing and duplicate number makes it slower 
        # although it seems like O(N), but actually O(N^2)
        # miss_num, dup_num = -1, -1
        # for x in range(len(nums)):
        #     if miss_num != -1 and dup_num != -1:
        #         break

        #     if miss_num == -1 and x+1 not in nums:
        #         miss_num = x+1
            
        #     if dup_num == -1 and nums[x] in nums[x+1::]:
        #         dup_num = nums[x]
        
        # return [dup_num, miss_num]

        # new idea
        # count how many times each number occurs first
        count = [0]*len(nums)
        for x in nums:
            count[x-1] += 1
        
        # then find the missing (count=0) and duplicate(count=2) one
        ans = [0, 0]
        for x in range(len(nums)):
            if ans[0]!=0 and ans[1]!=0:
                break

            if count[x] == 2:
                ans[0] = x+1
            elif count[x] == 0:
                ans[1] = x+1
        return ans