class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        std::sort(nums.begin(), nums.end());

        for (int i=0; i<nums.size()-2; i++)
        {
            if (i-1>=0 && nums[i]==nums[i-1])
            {
                cout << "Duplicate " << nums[i] << "\n";
                continue;
            }

            int target=-nums[i], l=i+1, r=nums.size()-1;
            while (l<r)
            {
                if (nums[l]+nums[r]==target)
                {
                    ans.push_back(vector<int>{nums[i], nums[l], nums[r]});
                    l++;
                    r--;
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