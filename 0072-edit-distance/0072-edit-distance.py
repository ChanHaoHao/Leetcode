class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # use dp to store the minimum operations to reach the current index
        dp = [[0]*(n+1) for _ in range(m+1)]

        # initialize for word1
        for i in range(1, m+1):
            dp[i][0] = i
        # initialize for word2
        for j in range(1, n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                # if they are the same, no operation is needed
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # dp[i-1][j-1]+1 => replace the char at i-1 with j-1
                    # dp[i-1][j]+1 => delete the char at i-1 in word1
                    # dp[i][j-1]+1 => insert the char at j-1 in word2
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
        
        return dp[m][n]