class Solution {
public:
    bool dfs(unordered_map<int, vector<int>>& mp, unordered_set<int>& visited, int source, int destination) {
        // iterate through all the neighbors of source
        for (auto it=mp[source].begin(); it<mp[source].end(); ++it) {
            // if the neighbor is not visited before
            if (visited.find(*it) == visited.end()) {
                visited.insert(*it);
                if (*it == destination)
                    return true;
                else if (dfs(mp, visited, *it, destination))
                    return true;
            }
        }

        return false;
    }

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
        return dfs(mp, visited, source, destination);
    }
};