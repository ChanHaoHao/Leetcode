class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        // sorte the nums
        std::sort(nums.begin(), nums.end());

        // Treat it as a two sum problem
        for (int i=0; i<nums.size()-2; i++)
        {
            // If the target is the same as the previous index, skip it
            if (i-1>=0 && nums[i]==nums[i-1])
                continue;

            int target=-nums[i], l=i+1, r=nums.size()-1;
            while (l<r)
            {
                // if the goal is found
                if (nums[l]+nums[r]==target)
                {
                    ans.push_back(vector<int>{nums[i], nums[l], nums[r]});
                    l++;
                    r--;
                    // prevent existing same pairs
                    while (l<r && nums[l]==nums[l-1])
                        l++;
                    while (l<r && nums[r]==nums[r+1])
                        r--;
                }
                else if (nums[l]+nums[r]>target)
                    r--;
                else
                    l++;
            }
        }

        return ans;
    }
};