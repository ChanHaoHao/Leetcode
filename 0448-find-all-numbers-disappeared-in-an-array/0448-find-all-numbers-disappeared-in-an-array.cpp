class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> count(nums.size());
        for (int n: nums)
            count[n-1]++;

        vector<int> ans;
        for (int i=0; i<nums.size(); i++)
        {
            if (count[i]==0)
                ans.push_back(i+1);
        }

        return ans;
    }
};