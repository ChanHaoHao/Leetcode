class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        if (source == destination) return true;
        // Store all valid paths into mp
        unordered_map<int, vector<int>> mp;
        for (int i=0; i<edges.size(); ++i) {
            // because all paths are bi-directional
            mp[edges[i][0]].push_back(edges[i][1]);
            mp[edges[i][1]].push_back(edges[i][0]);
        }

        unordered_set<int> visited;
        queue<int> q;
        q.push(source);
        visited.insert(source);

        while (!q.empty()) {
            int nxt = q.front();
            q.pop();

            if (nxt == destination)
                return true;

            for (auto it=mp[nxt].begin(); it<mp[nxt].end(); ++it) {
                // if not visited before
                if (visited.find(*it) == visited.end()) {
                    q.push(*it);
                    visited.insert(*it);
                }
            }
        }

        return false;
    }
};