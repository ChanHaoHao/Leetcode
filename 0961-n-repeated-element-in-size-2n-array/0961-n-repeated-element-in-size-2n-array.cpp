class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        // since there are n distinct numbers, and nums have n*2 numbers
        // only one number we be repeated
        unordered_set<int> seen;
        for (int n: nums)
        {
            if (seen.count(n))
                return n;
            seen.insert(n);
        }

        return -1;
    }
};