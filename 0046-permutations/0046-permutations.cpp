class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans = {{}};

        for (int i=0; i<nums.size(); ++i) {
            vector<vector<int>> new_perms;
            for (auto perm: ans) {
                for (int it=0; it<=perm.size(); ++it) {
                    vector<int> p = perm;
                    p.insert(p.begin()+it, nums[i]);
                    new_perms.push_back(p);
                } 
            }
            ans = new_perms;
        }

        return ans;
    }
};