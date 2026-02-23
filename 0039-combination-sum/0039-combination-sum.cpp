class Solution {
public:
    vector<vector<int>> ans;

    void backtrack(vector<int>& candidates, int i, int remain, vector<int>& subset) {
        if (remain == 0) {
            ans.push_back(subset);
            return;
        }

        if (remain < 0 || i == candidates.size()) {
            return;
        }

        subset.push_back(candidates[i]);
        backtrack(candidates, i, remain-candidates[i], subset);
        subset.pop_back();
        backtrack(candidates, i+1, remain, subset);
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> subset;
        backtrack(candidates, 0, target, subset);

        return ans;
    }
};