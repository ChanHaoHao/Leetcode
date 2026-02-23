class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(i, remain, subset):
            if remain == 0:
                ans.append(subset.copy())
                return
            
            if i == len(candidates) or remain < 0:
                return
            
            subset.append(candidates[i])
            backtrack(i, remain-candidates[i], subset)
            subset.pop()
            backtrack(i+1, remain, subset)
        
        backtrack(0, target, [])
        return ans