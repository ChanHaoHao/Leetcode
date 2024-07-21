class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        if k==1:
            return [[n]]

        def backtracking(i, combi):
            # if only one is left to put in
            if i==k-1:
                # ensure the remain number is strictly greater and <10
                if n-sum(combi)>combi[-1] and n-sum(combi)<10:
                    combi.append(n-sum(combi))
                    ans.append(combi)
                return
            
            # make the combi strictly greater to prevent duplicate
            for x in range(combi[-1]+1, 10):
                if x+sum(combi)<n:
                    combi.append(x)
                    backtracking(i+1, combi)
                    combi = combi[0:i]
                else:
                    break
            return

        for y in range(1, 9):
            if y<n:
                backtracking(1, [y])
        return ans