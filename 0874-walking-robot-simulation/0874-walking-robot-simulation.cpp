class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        vector<vector<int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int ans = 0;
        int dir = 0;
        int x = 0, y = 0;
        set<pair<int, int>> obs_set;
        for (int i=0; i<obstacles.size(); ++i) {
            obs_set.insert({obstacles[i][0], obstacles[i][1]});
        }

        for (int i=0; i<commands.size(); ++i) {
            // turn right 90 degrees
            if (commands[i] == -1) {
                dir++;
                dir = dir%4;
            }
            // turn left 90 degrees
            else if (commands[i] == -2) {
                dir--;
                dir = (dir + 4) % 4;
            }
            else {
                for (int c=commands[i]; c>0; --c) {
                    if (obs_set.find({x+dirs[dir][0], y+dirs[dir][1]}) != obs_set.end())
                        break;
                    x += dirs[dir][0];
                    y += dirs[dir][1];
                }

                ans = max(ans, x*x + y*y);
            }
        }

        return ans;
    }
};