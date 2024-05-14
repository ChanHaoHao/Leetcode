class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.ans = 0
        height = len(grid)
        width = len(grid[0])

        def findMax(y, x, acumalate, grid):
            acumalate += grid[y][x]
            mem = grid[y][x]
            grid[y][x] = 0
            end = True

            if y-1>=0 and grid[y-1][x]!=0:
                end = False
                findMax(y-1, x, acumalate, grid)
            if y+1<height and grid[y+1][x]!=0:
                end = False
                findMax(y+1, x, acumalate, grid)
            if x-1>=0 and grid[y][x-1]!=0:
                end = False
                findMax(y, x-1, acumalate, grid)
            if x+1<width and grid[y][x+1]!=0:
                end = False
                findMax(y, x+1, acumalate, grid)
            
            # restore the grid
            grid[y][x] = mem
            if end:
                self.ans = max(self.ans, acumalate)
        
        for y in range(height):
            for x in range(width):
                if grid[y][x]!=0:
                    findMax(y, x, 0, grid)
        
        return self.ans