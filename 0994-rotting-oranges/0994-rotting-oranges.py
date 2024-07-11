class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])

        # find the number of fresh fruits and the position of the rotten fruits
        fresh = 0
        rotten = deque()
        for y in range(m):
            for x in range(n):
                if grid[y][x]==2:
                    rotten.append([y, x])
                elif grid[y][x]==1:
                    fresh+=1
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        # while there are still fresh fruit remain
        while fresh!=0:
            count += 1
            # to check whether there are fresh fruit that can still be changed
            changed = False
            # bfs
            for x in range(len(rotten)):
                pos = rotten.popleft()
                # check if fresh fruit exist in the four directions of the rotten fruit
                for y in range(4):
                    if dy[y]+pos[0]<m and dy[y]+pos[0]>-1 and dx[y]+pos[1]<n and dx[y]+pos[1]>-1:
                        if grid[dy[y]+pos[0]][dx[y]+pos[1]]==1:
                            fresh-=1
                            grid[dy[y]+pos[0]][dx[y]+pos[1]] = 2
                            rotten.append([dy[y]+pos[0], dx[y]+pos[1]])
                            changed = True
            # if no fruit is changed (this guarentees fresh fruit remains)
            if not changed:
                return -1
        return count