class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        int n = nums.size()/2;
        unordered_map<int, int> count;

        for (auto i: nums)
        {
            if (count.find(i)==count.end())
            {
                count[i] = 1;
            }
            else
            {
                count[i] += 1;
                if (count[i]==n)
                    return i;
            }
        }

        return -1;
    }
};