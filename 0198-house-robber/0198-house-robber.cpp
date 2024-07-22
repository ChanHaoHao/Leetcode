class Solution {
public:
    int rob(vector<int>& nums) {
        const int n = nums.size();

        if (n==1)
            return nums[0];
        if (n==2)
        {
            if (nums[0]>nums[1])
                return nums[0];
            else
                return nums[1];
        }

        int dp[3] = {nums[0], nums[1], nums[0]+nums[2]};

        for (int i=3; i<n; i++)
        {
            int curr = nums[i];
            if (dp[0]>dp[1])
                curr += dp[0];
            else
                curr += dp[1];
            dp[0] = dp[1];
            dp[1] = dp[2];
            dp[2] = curr;
        }

        if (dp[1]>dp[2])
            return dp[1];
        return dp[2];
    }
};