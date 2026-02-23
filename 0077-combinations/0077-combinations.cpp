class Solution {
public:
    vector<vector<int>> ans;

    void backtrack(int n, int k, int i, vector<int>& subset) {
        if (subset.size() == k) {
            ans.push_back(subset);
            return;
        }

        if (i > n) {
            return;
        }

        for (int j=i; j<=n; ++j) {
            subset.push_back(j);
            backtrack(n, k, j+1, subset);
            subset.pop_back();
        }
    }

    vector<vector<int>> combine(int n, int k) {
        vector<int> subset;
        backtrack(n, k, 1, subset);
        return ans;

    }
};