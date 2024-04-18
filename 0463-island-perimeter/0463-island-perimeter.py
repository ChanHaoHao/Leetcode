class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for x in grid:
            ans += sum(x)*4

        height = len(grid)
        width = len(grid[0])
        for h in range(height):
            for w in range(width):
                if grid[h][w]:
                    if h-1>=0 and grid[h-1][w]:
                        ans -= 1
                    if h+1<height and grid[h+1][w]:
                        ans -= 1
                    if w-1>=0 and grid[h][w-1]:
                        ans -= 1
                    if w+1<width and grid[h][w+1]:
                        ans -= 1
        
        return ans