class Solution {
public:
    int edgeScore(vector<int>& edges) {
        std::vector<long long int> value(edges.size(), 0);

        for (int i=0; i<edges.size(); ++i) {
            value[edges[i]] += i;
        }

        int ans=0;
        for (int i=0; i<edges.size(); ++i) {
            if (value[ans] < value[i]) {
                ans = i;
            }
        }

        return ans;
    }
};