class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(nums, subset, used):
            if len(subset) == len(nums):
                ans.append(subset.copy())
                return
            
            for i in nums:
                if i in used:
                    continue
                
                used.add(i)
                subset.append(i)
                backtrack(nums, subset, used)
                subset.pop()
                used.remove(i)

        
        backtrack(nums, [], set())
        return ans