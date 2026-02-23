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
        backtrack(candidates, i+1, remain-candidates[i], subset, ans);
        subset.pop_back();
        i++;
        while (i < candidates.size() && candidates[i] == candidates[i-1]) {
            i++;
        }
        backtrack(candidates, i, remain, subset, ans);
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());

        vector<vector<int>> ans;
        vector<int> subset;

        backtrack(candidates, 0, target, subset, ans);
        return ans;
    }
};