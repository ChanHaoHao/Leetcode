class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        ans = [[-1 for _ in range(n)] for _ in range(m)]
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