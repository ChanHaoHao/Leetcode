class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # used to find the islands
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ans = 0

        M, N = len(grid2), len(grid2[0])
        # store the visited island
        grid2visited = set()
        # go through all grid2
        for y in range(M):
            for x in range(N):
                # if a new island is found
                if grid2[y][x]==1 and (y, x) not in grid2visited:
                    if grid1[y][x]==1:
                        # indicator for the subisland
                        subIsland = True
                    else:
                        subIsland = False
                    grid2visited.add((y, x))
                    # use bfs to find all the islands
                    queue = deque()
                    queue.append((y, x))
                    while queue:
                        point = queue.popleft()
                        for dy, dx in direction:
                            local_y, local_x = point[0]+dy, point[1]+dx
                            if 0<=local_y<M and 0<=local_x<N and (local_y, local_x) not in grid2visited and grid2[local_y][local_x]==1:
                                if grid1[local_y][local_x]!=1:
                                    subIsland = False
                                grid2visited.add((local_y, local_x))
                                queue.append((local_y, local_x))
                    if subIsland:
                        ans += 1
        return ans