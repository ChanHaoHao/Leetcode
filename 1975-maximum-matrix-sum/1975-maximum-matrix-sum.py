class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negs, suma, minim = 0, 0, float("inf")
        M, N = len(matrix), len(matrix[0])

        for m in range(M):
            for n in range(N):
                if matrix[m][n]<0:
                    negs += 1
                suma += abs(matrix[m][n])
                minim = min(minim, abs(matrix[m][n]))
        
        if negs%2==0:
            return suma
        else:
            return suma - minim*2