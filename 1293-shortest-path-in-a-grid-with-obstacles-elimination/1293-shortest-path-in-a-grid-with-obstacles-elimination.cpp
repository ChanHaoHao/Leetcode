struct Node {
    int r;
    int c;
    int g;
    int h;
    int f() { return g+h; }
    int obstacles;

    // bool operator>(Node* other) {
    //     if (f() == other->f()) {
    //         return g > other->g;
    //     }
    //     return f() > other->f();
    // }
};

struct Compare {
    bool operator()(Node* a, Node* b) {
        if (a->f() == b->f())
            return a->g > b->g;
        return a->f() > b-> f();
    }
};

class Solution {
public:
    int shortestPath(vector<vector<int>>& grid, int k) {
        int ROW = grid.size(), COL = grid[0].size();
        int dr[4] = {-1, 1, 0, 0};
        int dc[4] = {0, 0, -1, 1};

        priority_queue<Node*, vector<Node*>, Compare> openNodeList;
        vector<vector<int>> visited(ROW, vector<int>(COL, -1));
        Node* startNode = new Node();
        startNode->r = 0;
        startNode->c = 0;
        startNode->g = 0;
        startNode->h = ROW - 1 + COL - 1;
        startNode->obstacles = k;
        if (grid[0][0] == 1) {
            if (k == 0)
                return -1;
            startNode->obstacles--;
        }

        openNodeList.push(startNode);
        while (!openNodeList.empty()) {
            Node* currNode = openNodeList.top();
            openNodeList.pop();

            if (currNode->r == ROW - 1 && currNode->c == COL - 1)
                return currNode->g;
            if (currNode->obstacles <= visited[currNode->r][currNode->c]) {
                continue; // We've been here before with a better or equal budget
            }
            visited[currNode->r][currNode->c] = currNode->obstacles;

            for (int i=0; i<4; ++i) {
                int nxt_r = currNode->r + dr[i];
                int nxt_c = currNode->c + dc[i];

                // if neighbor in bound
                if (0 <= nxt_r && nxt_r < ROW && 0 <= nxt_c && nxt_c < COL) {
                    int remainingObs = currNode->obstacles - grid[nxt_r][nxt_c];
                    if (remainingObs >= 0) {
                        if (remainingObs > visited[nxt_r][nxt_c]) {

                            Node* nextNode = new Node();
                            nextNode->r = nxt_r;
                            nextNode->c = nxt_c;
                            nextNode->g = currNode->g + 1;
                            nextNode->h = ROW - 1 - nxt_r + COL - 1 - nxt_c;
                            nextNode->obstacles = remainingObs;

                            openNodeList.push(nextNode);
                        }
                    }
                }
            }
        }

        return -1;
    }
};