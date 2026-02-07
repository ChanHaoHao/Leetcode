class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int ans = 0;
        int ROW = grid.size(), COL = grid[0].size();
        int dr[4] = {-1, 1, 0, 0};
        int dc[4] = {0, 0, -1, 1};

        // Use queue to store all rotten orange
        queue<vector<int>> q;
        // Find all exist rotten orange
        for (int r=0; r<ROW; ++r) {
            for (int c=0; c<COL; ++c) {
                if (grid[r][c] == 2)
                    q.push({r, c});
            }
        }

        // Use BFS to iterate through all oranges that can be infected
        while (!q.empty()) {
            // iterate this level
            int n = q.size();
            for (n; n>0; --n) {
                vector<int> curr = q.front();
                q.pop();

                // Check if there is fresh orange in its neighbors
                int nxt_r, nxt_c;
                for (int i=0; i<4; ++i) {
                    nxt_r = curr[0] + dr[i];
                    nxt_c = curr[1] + dc[i];

                    // first check if out of bound, then check if it is fresh orange
                    if (0 <= nxt_r && nxt_r < ROW && 0 <= nxt_c && nxt_c < COL && grid[nxt_r][nxt_c]==1) {
                        // push it into the queue for bfs
                        q.push({nxt_r, nxt_c});
                        // mark it as rotten
                        grid[nxt_r][nxt_c] = 2;
                    }
                }
            }

            ans++;
        }

        for (int r=0; r<ROW; ++r) {
            for (int c=0; c<COL; ++c) {
                if (grid[r][c] == 1)
                    return -1;
            }
        }

        return (ans > 0) ? ans - 1 : ans;
    }
};