struct Node {
    pair<int, int> coord;
    int g;
    int h;
    int f() {return g+h;}
};

struct Compare {
    bool operator()(Node* a, Node* b) {
        if (a->f() == b->f()) {
            return a->g > b->g;
        }

        return a->f() > b->f();
    }
};

bool operator<(pair<int, int> a, pair<int, int> b) {
    if (a.first == b.first)
        return a.second < b.second;
    return a.first < b.first;
}

class Solution {
public:
    int ROW, COL;

    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        ROW = grid.size();
        COL = grid[0].size();

        int dr[8] = {-1, -1, -1, 1, 1, 1, 0, 0};
        int dc[8] = {-1, 0, 1, -1, 0, 1, -1, 1};

        // First check if the start and goal is valid
        if (grid[0][0] == 1 || grid[ROW-1][COL-1] == 1)
            return -1;

        Node* startNode = new Node();
        startNode->g = 1;
        startNode->h = ROW + COL - 2 * min(ROW, COL);
        startNode->coord = {0, 0};
        Node* goalNode = new Node();
        goalNode->coord = {ROW-1, COL-1};

        // Use a priority_queue to find the shortest path
        priority_queue<Node*, vector<Node*>, Compare> openNodeList;
        openNodeList.push(startNode);
        // Use a set to store the visited coord
        set<pair<int, int>> visited;

        while (!openNodeList.empty()) {
            Node* currNode = openNodeList.top();
            openNodeList.pop();
            
            if (visited.find(currNode->coord) != visited.end())
                continue;
            
            if (currNode->coord == goalNode->coord)
                return currNode->g;
            
            visited.insert(currNode->coord);
            for (int i=0; i<8; ++i) {
                int nxt_r = currNode->coord.first + dr[i];
                int nxt_c = currNode->coord.second + dc[i];

                // Check if nxt_r, nxt_c is in bound and is not obstacle
                if (0 <= nxt_r && nxt_r < ROW && 0 <= nxt_c && nxt_c < COL && grid[nxt_r][nxt_c]==0) {
                    if (visited.find({nxt_r, nxt_c}) != visited.end())
                        continue;
                    
                    Node* nxtNode = new Node();
                    nxtNode->coord = {nxt_r, nxt_c};
                    nxtNode->g = currNode->g + 1;

                    int diff_r = ROW - 1 - nxt_r;
                    int diff_c = COL - 1 - nxt_c;
                    nxtNode->h = diff_r + diff_c - 2 * min(diff_r, diff_c);
                    openNodeList.push(nxtNode);
                }
            }
        }

        return -1;  
    }
};