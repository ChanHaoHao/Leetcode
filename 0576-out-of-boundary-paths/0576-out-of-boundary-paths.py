class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9+7

        # use dfs to traverse through all the path and use cache to save result
        # cache = {}
        # def dfs(x, y, remain):
        #     if x<0 or y<0 or x==m or y==n:
        #         return 1
        #     elif remain==0:
        #         return 0
        #     elif (x, y, remain) in cache:
        #         return cache[(x, y, remain)]

        #     cache[(x, y, remain)] = (dfs(x+1, y, remain-1)+dfs(x-1, y, remain-1)+
        #             dfs(x, y+1, remain-1)+dfs(x, y-1, remain+1)) % MOD
        #     return cache[(x, y, remain)]

        # return dfs(startRow, startColumn, maxMove)

        # bottom up dynamic programming method
        # use this to save the result of the previous remaining move
        bottomUp_dp = [[0]*n for _ in range(m)]
        # start counting the result of each remaining moves
        for remain in range(1, maxMove+1):
            # this counts the result of the current remaining move
            tmp = [[0]*n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    # add up the result of the block
                    # if it moves out of bounds
                    if x+1==m:
                        tmp[x][y] = (tmp[x][y] + 1) % MOD
                    # if it doesn't move out of bounds, so add the result moving down
                    else:
                        tmp[x][y] = (tmp[x][y]+bottomUp_dp[x+1][y]) % MOD
                    
                    # if it moves out of bounds
                    if x-1<0:
                        tmp[x][y] = (tmp[x][y]+1) % MOD
                    # if it doesn't move out of bounds, so add the result moving up
                    else:
                        tmp[x][y] = (tmp[x][y] + bottomUp_dp[x-1][y]) % MOD

                    # if it moves out of bounds
                    if y+1==n:
                        tmp[x][y] = (tmp[x][y]+1) % MOD
                    # if it doesn't move out of bounds, so add the result moving right
                    else:
                        tmp[x][y] = (tmp[x][y] + bottomUp_dp[x][y+1]) % MOD

                    # if it moves out of bounds
                    if y-1<0:
                        tmp[x][y] = (tmp[x][y]+1) % MOD
                    # if it doesn't move out of bounds, so add the result moving left
                    else:
                        tmp[x][y] = (tmp[x][y] + bottomUp_dp[x][y-1]) % MOD
            # update the previous remain
            bottomUp_dp = tmp

        return bottomUp_dp[startRow][startColumn]