struct Point {
    pair<int, int> point;
    double g;
    double h;
    double f() {return g + h ;}
    Point* parent;
};

struct Compare {
    bool operator()(Point* a, Point* b) {
        if (a->f() == b->f()) {
            return a->g > b->g;
        }
        return a->f() > b->f();
    }
};

bool operator<(const Point a, const Point b) {
    if (a.point.first == b.point.first)
        return a.point.second < b.point.second;
    return a.point.first < b.point.first;
}

class Solution {
public:
    int ROW, COL;

    vector<pair<int, int>> get_neighbors(vector<vector<int>>& grid, pair<int, int> curr) {
        int dr[8] = {-1, -1, -1, 1, 1, 1, 0, 0};
        int dc[8] = {0, 1, -1, 0, 1, -1, 1, -1};

        vector<pair<int, int>> neighbors;

        for (int i=0; i<8; ++i) {
            int nxt_r = curr.first + dr[i];
            int nxt_c = curr.second + dc[i];

            // if nxt_r, nxt_c is in bound and not a obstacle
            if (0 <= nxt_r && nxt_r < ROW && 0 <= nxt_c && nxt_c < COL && grid[nxt_r][nxt_c]==0) {
                neighbors.push_back({nxt_r, nxt_c});
            }
        }

        return neighbors;
    }

    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        ROW = grid.size();
        COL = grid[0].size();

        // Use a min_heap to store all open nodes, sorted by f and g cost
        priority_queue<Point*, vector<Point*>, Compare> min_heap;
        // Store all visited points
        set<pair<int, int>> visited;
        // Store all open nodes;
        map<pair<int, int>, Point*> mp;

        // Check if start and goal is valid
        if (grid[0][0] == 1 || grid[ROW-1][COL-1])
            return -1;
        
        Point* start = new Point();
        start->point = {0, 0};
        start->g = 0;
        start->h = ROW + COL - 2 * min(ROW, COL);
        start->parent = nullptr;
        mp[start->point] = start;
        min_heap.push(start);
        pair<int, int> goal = {ROW-1, COL-1};

        while (!min_heap.empty()) {
            Point* curr = min_heap.top();
            min_heap.pop();

            // if visited before
            if (visited.find(curr->point) != visited.end())
                continue;
            visited.insert(curr->point);
            
            // if curr is goal
            if (curr->point == goal) {
                int ans = 0;
                while (curr != nullptr) {
                    curr = curr->parent;
                    ans++;
                }

                return ans;
            }

            for (auto nei: get_neighbors(grid, curr->point)) {
                if (visited.find(nei) != visited.end())
                    continue;

                double tmp_g_cost = curr->g + 1;

                // if the neighbor is in the opennode map
                if (mp.find(nei) != mp.end()) {
                    if (mp[nei]->g > tmp_g_cost) {
                        mp[nei]->parent = curr;
                        mp[nei]->g = tmp_g_cost;
                        min_heap.push(mp[nei]);
                    }
                }
                // else create a new Point and add it to the opennode map
                else {
                    Point* neiPoint = new Point();
                    neiPoint->point = nei;
                    neiPoint->g = tmp_g_cost;
                    neiPoint->h = curr->h - 1;
                    neiPoint->parent = curr;
                    min_heap.push(neiPoint);
                    mp[nei] = neiPoint;
                }
            }
        }

        return -1;
    }
};