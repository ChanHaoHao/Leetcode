class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row_sum, col_sum = [], []
        height, width = len(grid), len(grid[0])
        
        for x in range(height):
            row_sum.append(sum(grid[x]))
        for y in range(width):
            col_sum.append(sum([row[y] for row in grid]))
        
        left, right = row_sum[0], sum(row_sum)-row_sum[0]
        for x in range(1, height):
            if left==right:
                return True
            left += row_sum[x]
            right -= row_sum[x]
        
        left, right = col_sum[0], sum(col_sum)-col_sum[0]
        for x in range(1, width):
            if left==right:
                return True
            left += col_sum[x]
            right -= col_sum[x]
            
        return False