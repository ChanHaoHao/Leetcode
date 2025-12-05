class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        zeros = []
        H, W = len(matrix), len(matrix[0])
        for h in range(H):
            for w in range(W):
                if matrix[h][w]==0:
                    zeros.append((h, w))
        
        for zero in zeros:
            for h in range(H):
                matrix[h][zero[1]] = 0
            for w in range(W):
                matrix[zero[0]][w] = 0
        
