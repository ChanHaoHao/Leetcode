class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(n, k, i, subset):
            if len(subset) == k:
                ans.append(subset.copy())
                return
            
            for j in range(i, n-(k-len(subset))+2):
                subset.append(j)
                backtrack(n, k, j+1, subset)
                subset.pop()
        
        backtrack(n, k, 1, [])
        return ans