class Solution:
    def numTilings(self, n: int) -> int:
        modulo = 10**9+7

        # store the methods to get to i-th length flat rect in dp
        # dp[i] = dp[i-1] (put a domino standing) + dp[i-2] (put 2 domino laying) + dpa[i-1]*2 (put a tromino)
        dp = [1, 2]+[0]*n
        # store the methods to get to i-1-th length with a square out at i-th
        # dpa[i] = dpa[i-1] (put a domino)+dp[i-2] (put a tromino)
        dpa = [1]*n

        for i in range(2, n):
            dp[i] = (dp[i-1]+dp[i-2]+dpa[i-1]*2)%modulo
            dpa[i] = (dp[i-2]+dpa[i-1])%modulo
        
        return dp[n-1]
