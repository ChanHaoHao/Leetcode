class Solution {
public:
    void backtrack(vector<int>& candidates, int i, int remain, vector<int>& subset, vector<vector<int>>& ans) {
        if (remain == 0) {
            ans.push_back(subset);
            return;
        }

        if (i == candidates.size() || remain < 0) {
            return;
        }

        subset.push_back(candidates[i]);
        backtrack(candidates, i, remain-candidates[i], subset, ans);
        subset.pop_back();
        backtrack(candidates, i+1, remain, subset, ans);
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> subset;

        backtrack(candidates, 0, target, subset, ans);
        return ans;
    }
};