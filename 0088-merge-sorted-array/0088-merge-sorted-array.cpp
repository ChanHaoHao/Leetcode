class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // start from the end of 2 arrays
        int i1=m-1, i2=n-1, index=m+n-1;
        while (i1>=0 && i2>=0)
        {
            // put the greater to the last of the array
            if (nums1[i1]>nums2[i2])
            {
                nums1[index] = nums1[i1];
                nums1[i1] = 0;
                --i1;
            }
            else
            {
                nums1[index] = nums2[i2];
                --i2;
            }
            --index;
        }

        // if there are still nums2 remaining
        for (i2; i2>=0; --i2)
        {
            nums1[i2] = nums2[i2];
        }
    }
};