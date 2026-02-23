class Solution {
public:
    vector<vector<int>> ans;

    void backtrack(vector<int>& nums, vector<bool>& used, vector<int>& subset) {
        if (subset.size() == nums.size()) {
            ans.push_back(subset);
            return;
        }

        for (int i=0; i<nums.size(); ++i) {
            if (!used[i]) {
                subset.push_back(nums[i]);
                used[i] = true;
                backtrack(nums, used, subset);
                used[i] = false;
                subset.pop_back();
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> subset;
        vector<bool> used(nums.size(), false);

        backtrack(nums, used, subset);
        return ans;
    }
};