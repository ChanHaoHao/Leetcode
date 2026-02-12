class Solution {
public:
    int triangularSum(vector<int>& nums) {
        while (nums.size() > 1) {
            vector<int> tmp;
            for (int i=0; i<nums.size()-1; ++i) {
                tmp.push_back((nums[i] + nums[i+1]) % 10);
            }
            nums = tmp;
        }

        return nums[0];
    }
};