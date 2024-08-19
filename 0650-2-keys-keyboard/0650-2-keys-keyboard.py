class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0

        # dynamic programing
        memoization = [[0]*(n//2+1) for _ in range(n+1)]
        # a is the curr length of string A, steps are the length in the curr paste
        def backtracking(a, steps):
            if a==n:
                return 0
            if a>n:
                return 1000

            if memoization[a][steps]!=0:
                return memoization[a][steps]
            # copy+paste
            opt1 = backtracking(a*2, a)+2
            # paste
            opt2 = backtracking(a+steps, steps)+1
            memoization[a][steps] = min(opt1, opt2)
            return memoization[a][steps]
        
        return 1+backtracking(1, 1)