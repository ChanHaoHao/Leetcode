class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> ans(n*2);

        int front=0, back=n, i=0;
        while (i<n*2)
        {
            ans[i] = nums[front];
            ++i;
            ans[i] = nums[back];
            ++i;

            ++front;
            ++back;
        }

        return ans;
    }
};