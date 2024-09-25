class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i=0, n=nums.size();
        while (i<n)
        {
            if (nums[i]==val)
            {
                nums.erase(nums.begin()+i);
                --n;
            }
            else
                ++i;
        }

        return n;
    }
};