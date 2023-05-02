class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # def multi(num):
        #     ans=1
        #     for x in range(2, num+1):
        #         ans*=x
        #     return ans
        
        # return int(multi(m+n-2)/(multi(m-1)*multi(n-1)))
        Map=[[0 for _ in range(n)] for _ in range(m)]

        for x in range(m):
            for y in range(n):
                if x==0 or y==0:
                    Map[x][y]=1
                else:
                    Map[x][y]=Map[x-1][y]+Map[x][y-1]
        
        return Map[m-1][n-1]