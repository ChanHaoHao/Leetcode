class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        std::vector<int> sortedNums = nums;
        std::sort(sortedNums.rbegin(), sortedNums.rend());

        std::unordered_map<int, int> countMap;
        for (int i=0; i<k; ++i) {
            countMap[sortedNums[i]]++;
        }

        std::vector<int> ans;
        for (int n: nums) {
            if (countMap[n] > 0) {
                ans.push_back(n);
                countMap[n] -= 1;
            }
        }

        return ans;
    }
};