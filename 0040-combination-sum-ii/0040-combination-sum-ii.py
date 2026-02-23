class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # first sort the array to prevent duplicate
        candidates.sort()

        ans = []

        def backtrack(i, remain, subset):
            if remain == 0:
                ans.append(subset.copy())
                return
            
            if i == len(candidates) or remain < 0:
                return
            
            subset.append(candidates[i])
            backtrack(i+1, remain-candidates[i], subset)
            subset.pop()

            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            backtrack(i, remain, subset)
        
        backtrack(0, target, [])
        return ans