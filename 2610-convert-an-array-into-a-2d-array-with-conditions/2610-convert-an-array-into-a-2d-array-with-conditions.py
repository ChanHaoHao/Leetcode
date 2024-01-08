class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        index = 0
        ans, local_ans = [], []

        while len(nums)>0:
            if index==len(nums):
                ans.append(local_ans)
                local_ans = []
                index = 0
            else:
                if nums[index] not in local_ans:
                    local_ans.append(nums.pop(index))
                else:
                    index += 1

        if len(local_ans)>0:
            ans.append(local_ans)
        return ans