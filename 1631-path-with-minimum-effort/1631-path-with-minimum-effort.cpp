struct Node {
    pair<int, int> coord;
    int g;
    Node* parent;
};

struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->g > b->g;
    }
};

bool operator<(pair<int, int> a, pair<int, int> b) {
    if (a.first == b.first)
        return a.second < b.second;
    return a.first < b.first;
}

class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int ROW = heights.size(), COL = heights[0].size();
        int dr[4] = {-1, 1, 0, 0};
        int dc[4] = {0, 0, -1, 1};

        Node* startNode = new Node();
        startNode->coord = {0, 0};
        startNode->g = 0;
        startNode->parent = nullptr;
        Node* goalNode = new Node();
        goalNode->coord = {ROW-1, COL-1};

        priority_queue<Node*, vector<Node*>, Compare> openNodeList;
        openNodeList.push(startNode);
        set<pair<int, int>> visited;

        while (!openNodeList.empty()) {
            Node* currNode = openNodeList.top();
            openNodeList.pop();

            if (currNode->coord == goalNode->coord) {
                int ans = 0;
                while (currNode->parent != nullptr) {
                    ans = max(ans, abs(heights[currNode->coord.first][currNode->coord.second] - heights[currNode->parent->coord.first][currNode->parent->coord.second]));
                    currNode = currNode->parent;
                }

                return ans;
            }

            if (visited.find(currNode->coord) != visited.end())
                continue;
            visited.insert(currNode->coord);

            for (int i=0; i<4; ++i) {
                int nxt_r = currNode->coord.first + dr[i];
                int nxt_c = currNode->coord.second + dc[i];

                // Check inbound and not visited
                if (0 <= nxt_r && nxt_r < ROW && 0 <= nxt_c && nxt_c < COL && visited.find({nxt_r, nxt_c}) == visited.end()) {
                    Node* nxtNode = new Node();
                    nxtNode->coord = {nxt_r, nxt_c};
                    nxtNode->g = abs(heights[nxt_r][nxt_c] - heights[currNode->coord.first][currNode->coord.second]);
                    nxtNode->parent = currNode;
                    openNodeList.push(nxtNode);
                }
            }
        }

        return -1;
    }
};