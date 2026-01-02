class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        unordered_set<int> count;
        for (int n: nums)
            count.insert(n);

        vector<int> ans;
        for (int i=0; i<nums.size(); i++)
        {
            if (count.find(i+1)==count.end())
                ans.push_back(i+1);
        }

        return ans;
    }
};