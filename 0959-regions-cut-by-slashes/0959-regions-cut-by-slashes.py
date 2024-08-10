class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        # divide each character into 3 spaces
        # / -> 001, 010, 100
        # \ -> 100, 010, 001
        # then count the number of isolated islands
        magnified_map = [[0]*(3*n) for _ in range(3*n)]

        # initialize the map
        for row_index in range(n):
            row = grid[row_index]
            for col_index in range(n):
                if row[col_index]=="/":
                    magnified_map[row_index*3][col_index*3+2]=1
                    magnified_map[row_index*3+1][col_index*3+1]=1
                    magnified_map[row_index*3+2][col_index*3]=1
                elif row[col_index]=="\\":
                    magnified_map[row_index*3][col_index*3]=1
                    magnified_map[row_index*3+1][col_index*3+1]=1
                    magnified_map[row_index*3+2][col_index*3+2]=1

        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ans = 0
        for y in range(n*3):
            for x in range(n*3):
                if magnified_map[y][x]==0:
                    ans += 1
                    queue = deque()
                    queue.append([y, x])
                    magnified_map[y][x] = 1
                    # search using dfs
                    while queue:
                        curr_y, curr_x = queue.pop()
                        for dy, dx in direction:
                            if 0<=curr_y+dy<3*n and 0<=curr_x+dx<3*n and magnified_map[curr_y+dy][curr_x+dx]==0:
                                queue.append([curr_y+dy, curr_x+dx])
                                magnified_map[curr_y+dy][curr_x+dx] = 1
        
        return ans