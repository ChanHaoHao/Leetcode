class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int count = 0, m = grid.size(), n = grid[0].size();
        int fresh = 0;
        queue<pair<int, int>> rotten;

        for (int i=0; i<m; i++)
        {
            for (int j=0; j<n; j++)
            {
                if (grid[i][j]==2)
                {
                    rotten.push(make_pair(i, j));
                }
                else if (grid[i][j]==1)
                {
                    fresh += 1;
                }
            }
        }

        vector<pair<int, int>> delta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        bool changed = false;
        while (fresh!=0)
        {
            count++;
            int level = rotten.size();
            for (int i=0; i<level; i++)
            {
                pair<int, int> pos = rotten.front();
                rotten.pop();
                for(int j=0; j<4; j++)
                {
                    int dy = delta[j].first, dx = delta[j].second;
                    if (pos.first+dy<m && pos.first+dy>-1 && pos.second+dx<n && pos.second+dx>-1)
                    {
                        if (grid[pos.first+dy][pos.second+dx]==1)
                        {
                            fresh--;
                            grid[pos.first+dy][pos.second+dx] = 2;
                            rotten.push(make_pair(pos.first+dy, pos.second+dx));
                            changed = true;
                        }
                    }
                }
            }
            if (!changed)
            {
                return -1;
            }
            changed = false;
        }
        return count;
    }
};