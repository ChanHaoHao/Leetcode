class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # matching direction values 1, 2, 3, 4
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        n_rows, n_cols = len(grid), len(grid[0])
        pq = [(0, 0, 0)]
        min_cost = [[float("inf")] * n_cols for _ in range(n_rows)]
        min_cost[0][0] = 0

        while pq:
            cost, row, col = heapq.heappop(pq)

            # if a smaller cost is found, skip
            if min_cost[row][col] != cost:
                continue

            for x in range(4):
                (dx, dy) = direc[x]

                nxt_row, nxt_col = row + dx, col + dy
                if 0<=nxt_row<n_rows and 0<=nxt_col<n_cols:
                    new_cost = cost
                    if x != grid[row][col]-1:
                        new_cost += 1
                    
                    if min_cost[nxt_row][nxt_col]>new_cost:
                        min_cost[nxt_row][nxt_col] = new_cost
                        heapq.heappush(pq, (new_cost, nxt_row, nxt_col))
        
        return min_cost[n_rows-1][n_cols-1]