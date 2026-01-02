class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        map<int, int> count;
        for (int n: nums)
            count[n]++;

        int acc = 0;
        unordered_map<int, int> accum;
        for (auto n: count)
        {
            accum[n.first] = acc;
            acc += n.second;
        }

        vector<int> ans(nums.size());
        for (int i=0; i<nums.size(); i++)
        {
            ans[i] = accum[nums[i]];
        }

        return ans;
    }
};