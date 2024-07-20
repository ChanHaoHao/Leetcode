class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        ans = [[-1 for _ in range(n)] for _ in range(m)]

        # thres = min(m, n)

        # for y in range(thres):
        #     if rowSum[y]>colSum[y]:
        #         ans[y][y] = colSum[y]
        #         rowSum[y] -= colSum[y]
        #         for x in range(m):
        #             if x!=y:
        #                 ans[x][y] = 0
        #     else:
        #         ans[y][y] = rowSum[y]
        #         colSum[y] -= rowSum[y]
        #         for x in range(n):
        #             if x!=y:
        #                 ans[y][x] = 0

        # for y in range(m):
        #     for x in range(n):
        #         if ans[y][x]==-1:
        #             if rowSum[y]>colSum[x]:
        #                 ans[y][x] = colSum[x]
        #                 rowSum[y] -= colSum[x]
        #                 for z in range(m):
        #                     if ans[z][x]==-1:
        #                         ans[z][x] = 0
        #             else:
        #                 ans[y][x] = rowSum[y]
        #                 colSum[x] -= rowSum[y]
        #                 for z in range(n):
        #                     if ans[y][z]==-1:
        #                         ans[y][z] = 0

        row, col = 0, 0

        while row<m and col<n:
            if rowSum[row]<colSum[col]:
                ans[row][col] = rowSum[row]
                colSum[col] -= rowSum[row]
                rowSum[row] = 0
                for x in range(n):
                    if ans[row][x]==-1:
                        ans[row][x] = 0
                row+=1
            else:
                ans[row][col] = colSum[col]
                rowSum[row] -= colSum[col]
                colSum[col] = 0
                for x in range(m):
                    if ans[x][col]==-1:
                        ans[x][col] = 0
                col += 1
        return ans