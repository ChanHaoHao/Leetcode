class Solution {
public:
    void backtrack(int n, int k, int start, vector<int>& subset, vector<vector<int>>& ans) {
        if (subset.size() == k) {
            ans.push_back(subset);
            return;
        }

        for (int i=start; i<=n-(k-subset.size())+1; ++i) {
            subset.push_back(i);
            backtrack(n, k, i+1, subset, ans);
            subset.pop_back();
        }
    }

    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        vector<int> subset;

        backtrack(n, k, 1, subset, ans);
        return ans;    
    }
};