class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        vector<int> count(nums.size());

        for (int n: nums)
        {
            count[n-1]++;
        }

        vector<int> ans(2);
        for (int i=0; i<nums.size(); i++)
        {
            if (count[i]==0)
                ans[1] = i+1;
            else if (count[i]==2)
                ans[0] = i+1;
        }

        return ans;
    }
};