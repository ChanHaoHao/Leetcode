class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        // tried to write it in cpp
        int height=maze.size(), width=maze[0].size();
        int dx[4] = {0, 0, 1, -1};
        int dy[4] = {1, -1, 0, 0};

        queue<pair<int, int>> q;
        q.push({entrance[0], entrance[1]});
        maze[entrance[0]][entrance[1]] = '+';

        int step = 0;
        while (!q.empty())
        {
            for (int size=q.size(); size>0; size--)
            {
                int y=q.front().first, x=q.front().second;
                q.pop();

                for (int i=0; i<4; i++)
                {
                    int loc_y = dy[i]+y;
                    int loc_x = dx[i]+x;
                    printf("%i, %i\n", loc_y, loc_x);
                    if (loc_y>=0 && loc_y<height && loc_x>=0 && loc_x<width && maze[loc_y][loc_x]=='.')
                    {
                        if (loc_y==0 || loc_y==height-1 || loc_x==0 || loc_x==width-1)
                            return step+1;
                        q.push({loc_y, loc_x});
                        maze[loc_y][loc_x] = '+';
                    }
                }
            }
            step++;
        }

        return -1;
    }
};