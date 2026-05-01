class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        int sum = 0, F0 = 0, n = nums.size();

        for (int i=0; i<n; ++i) {
            sum += nums[i];
            F0 += i * nums[i];
        }

        int ans = F0;
        for (int i=1; i<n; ++i) {
            F0 += sum - n * nums[n-i];
            ans = max(ans, F0);
        }

        return ans;
    }
};