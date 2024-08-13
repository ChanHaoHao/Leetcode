class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the candidates so we can exclude the same number
        candidates.sort()
        
        ans = []

        def dfs(i, combination):
            if sum(combination)==target:
                ans.append(combination.copy())
                return

            if i==len(candidates) or sum(combination)>target:
                return

            combination.append(candidates[i])
            dfs(i+1, combination)
            combination.pop()

            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1, combination)
        
        dfs(0, [])
        return ans
