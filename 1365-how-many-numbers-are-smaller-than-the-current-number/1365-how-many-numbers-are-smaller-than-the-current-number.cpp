class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        // map<int, int> count;
        // for (int n: nums)
        //     count[n]++;

        // int acc = 0;
        // unordered_map<int, int> accum;
        // for (auto n: count)
        // {
        //     accum[n.first] = acc;
        //     acc += n.second;
        // }

        // vector<int> ans(nums.size());
        // for (int i=0; i<nums.size(); i++)
        // {
        //     ans[i] = accum[nums[i]];
        // }

        // return ans;

        vector<int> sorted=nums;
        sort(sorted.begin(), sorted.end());
        unordered_map<int, int> m;
        for (int i=0; i<nums.size(); i++)
        {
            // Use the sorted array as index, for how many number is smaller ahead
            if (m.find(sorted[i])==m.end())
                m[sorted[i]] = i;
        }

        vector<int> ans(nums.size());
        for (int i=0; i<nums.size(); i++)
            ans[i] = m[nums[i]];

        return ans;
    }
};