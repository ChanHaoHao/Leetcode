class Solution {
public:
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int N1 = nums1.size(), N2 = nums2.size();
        int max_dist = -1, n1 = 0, n2 = 0;

        while (n1 < N1 && n2 < N2) {
            if (n1 <= n2) {
                if (nums1[n1] <= nums2[n2]) {
                    max_dist = max(max_dist, n2 - n1);
                    ++n2;
                }
                else {
                    ++n1;
                }
            }
            else {
                n2 = n1;
            }
        }
        
        if (max_dist == -1)
            return 0;
        return max_dist;
    }
};