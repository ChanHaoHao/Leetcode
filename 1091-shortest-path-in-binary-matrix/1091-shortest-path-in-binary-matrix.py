class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # # if start or goal is 1, then impossible
        # if grid[0][0]==1 or grid[-1][-1]==1:
        #     return -1
            
        # # each queue stores (r, c, steps)
        # queue = deque()
        # queue.append((0, 0, 1))
        # N = len(grid)
        # # 8 direction to find clear path
        # dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        # visited = set()

        # while queue:
        #     cur_r, cur_c, steps = queue.popleft()
        #     if (cur_r, cur_c) in visited:
        #         continue
        #     if (cur_r, cur_c)==(N-1, N-1):
        #         return steps
        #     visited.add((cur_r, cur_c))
        #     for d in dirs:
        #         nxt_r = cur_r + d[0]
        #         nxt_c = cur_c + d[1]

        #         # if in boundary, and is a clear path, and not visited or found a shorter path
        #         if (0<=nxt_r<N and 0<=nxt_c<N) and grid[nxt_r][nxt_c]==0 and (nxt_r, nxt_c) not in visited:
        #             queue.append((nxt_r, nxt_c, steps+1))
        
        # return -1

        N = len(grid)
        if grid[0][0]!=0 or grid[N-1][N-1]!=0:
            return -1
        
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        def heuristic(r, c):
            return max(N-1-r, N-1-c)

        heap = []
        heapq.heappush(heap, (1+heuristic(0, 0), 1, 0, 0))
        visited = set()

        while heap:
            f, g, r, c = heapq.heappop(heap)
            if (r, c) == (N-1, N-1):
                return g
            if (r, c) in visited:
                continue
            visited.add((r, c))

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0<=nr<N and 0<=nc<N and grid[nr][nc]==0 and (nr, nc) not in visited:
                    heapq.heappush(heap, (g+1+heuristic(nr, nc), g+1, nr, nc))
    
        return -1