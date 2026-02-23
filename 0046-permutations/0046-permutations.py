class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(nums, subset):
            if len(subset) == len(nums):
                ans.append(subset.copy())
                return
            
            for i in nums:
                if i not in subset:
                    subset.append(i)
                    backtrack(nums, subset)
                    subset.pop()
        
        backtrack(nums, [])
        return ans