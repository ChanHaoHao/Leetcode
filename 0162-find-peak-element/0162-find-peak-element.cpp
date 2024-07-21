class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();

        if (n==1 || nums[0]>nums[1])
            return 0;
        else if (nums[n-1]>nums[n-2])
            return n-1;

        int left=1, right=n-2;
        int mid = (left+right)/2;

        while (left<right)
        {
            if (nums[mid]<nums[mid+1])
                left = mid+1;
            else
                right = mid; // this guarentees right will stand on the greatest value
            mid = (left+right)/2;
        }

        return left;
    }
};