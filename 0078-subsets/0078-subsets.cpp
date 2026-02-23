class Solution {
public:
    void backtrack(vector<int>& nums, int i, vector<int>& subset, vector<vector<int>>& ans) {
        if (i == nums.size()) {
            ans.push_back(subset);
            return;
        }

        subset.push_back(nums[i]);
        backtrack(nums, i+1, subset, ans);
        subset.pop_back();
        backtrack(nums, i+1, subset, ans);
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> subset;

        backtrack(nums, 0, subset, ans);
        return ans;    
    }
};