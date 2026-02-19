void dfs(char** grid, int gridSize, int* gridColSize, int r, int c) {
    if (r < 0 || r >= gridSize || c < 0 || c >= gridColSize[r] || grid[r][c]=='0')
        return;
    
    grid[r][c] = '0';
    dfs(grid, gridSize, gridColSize, r-1, c);
    dfs(grid, gridSize, gridColSize, r+1, c);
    dfs(grid, gridSize, gridColSize, r, c-1);
    dfs(grid, gridSize, gridColSize, r, c+1);
}

int numIslands(char** grid, int gridSize, int* gridColSize) {
    int ans = 0;

    for (int r=0; r<gridSize; ++r) {
        for (int c=0; c<gridColSize[r]; ++c) {
            if (grid[r][c] == '1') {
                dfs(grid, gridSize, gridColSize, r, c);
                ans++;
            }
        }
    }

    return ans;
}