class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int j=1;
        for (int i=1; i<nums.size(); ++i)
        {
            if (nums[i]!=nums[i-1])
            {
                nums[j]=nums[i];
                ++j;
            }
        }

        return j;
        
        // int i=0, n=nums.size();
        // while (i<n-1)
        // {
        //     if (nums[i]==nums[i+1])
        //     {
        //         nums.erase(nums.begin()+i);
        //         --n;
        //     }
        //     else
        //         ++i;
        // }

        // return n;
    }
};