class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # By the hint, we know that only three occassion exist, 0, 1, 2
        visited = set()
        direction = [[1,0], [-1,0], [0,-1], [0,1]]
        m, n = len(grid), len(grid[0])

        def dfs(y, x, visited):
            visited.add((y, x))
            for dy, dx in direction:
                if 0<=dy+y<m and 0<=dx+x<n and grid[y+dy][x+dx]==1 and (y+dy, x+dx) not in visited:
                    dfs(dy+y, dx+x, visited)

        # find how many islands exist
        islands = 0
        for y in range(m):
            for x in range(n):
                if (y, x) not in visited and grid[y][x]==1:
                    dfs(y, x, visited)
                    islands += 1

        if islands!=1:
            return 0
        
        # try to remove 1 island, if still can't find a solution, return 2
        islands = list(visited)
        for y, x in islands:
            grid[y][x] = 0
            visit = set()
            count = 0
            for r in range(m):
                for c in range(n):
                    if (r, c) not in visit and grid[r][c]==1:
                        dfs(r, c, visit)
                        count += 1

            if count!=1:
                return 1
            grid[y][x] = 1
        
        return 2

        