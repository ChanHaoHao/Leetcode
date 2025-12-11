class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ans = 0

        H, W = len(grid), len(grid[0])
        for h in range(H):
            for w in range(W):
                if (h, w) not in visited and grid[h][w]=="1":
                    ans += 1
                    visited.add((h,w))
                    queue = [(h, w)]
                    while queue:
                        local_h, local_w = queue.pop()
                        for dir in dirs:
                            cur_h, cur_w = local_h+dir[0], local_w+dir[1]
                            if 0<=cur_h<H and 0<=cur_w<W and (cur_h, cur_w) not in visited and grid[cur_h][cur_w]=="1":
                                visited.add((cur_h, cur_w))
                                queue.append((cur_h, cur_w))
        
        return ans