class Solution:
    dir_x = [0, 0, -1, 1]
    dir_y = [1, -1, 0, 0]

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        q = deque()
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1

        length = 1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for i in range(4):
                    dy = curr[0]+self.dir_y[i]
                    dx = curr[1]+self.dir_x[i]
                    if dy>=0 and dy<n and dx>=0 and dx<n and grid[dy][dx]==-1:
                        grid[dy][dx] = length
                        q.append((dy, dx))
            length += 1
        
        start, end, res = 0, 0, -1
        for i in range(n):
            for j in range(n):
                end = max(end, grid[i][j])

        while start<=end:
            # uses binary search to find faster
            mid = start + (end-start)//2
            if self.safe(grid, mid):
                res = mid
                start = mid+1
            else:
                end = mid-1
        
        return res

    def safe(self, grid, mid):
        n = len(grid)
        # means that the current point is not the greatest safeteness in the path
        if grid[0][0]<mid or grid[n-1][n-1]<mid:
            return False

        # then use bfs to go through and find a path
        trav_q = deque([(0, 0)])
        visited = [[False]*n for _ in range(n)]
        visited[0][0] = True

        while trav_q:
            curr = trav_q.popleft()
            # a path is found
            if curr[0] == n-1 and curr[1] == n-1:
                return True

            for i in range(4):
                dy = curr[0]+self.dir_y[i]
                dx = curr[1]+self.dir_x[i]
                if dy>=0 and dy<n and dx>=0 and dx<n and not visited[dy][dx] and grid[dy][dx]>=mid:
                    visited[dy][dx] = True
                    trav_q.append((dy ,dx))
        
        return False