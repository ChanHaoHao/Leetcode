class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        int ROW = image.size(), COL = image[0].size();
        vector<vector<int>> ans(ROW, vector<int>(COL, 0));

        for (int r=0; r<ROW; ++r) {
            int left = 0, right = COL-1;
            while (left < right) {
                if (image[r][right] == 1)
                    ans[r][left] = 0;
                else
                    ans[r][left] = 1;
                
                if (image[r][left] == 1)
                    ans[r][right] = 0;
                else
                    ans[r][right] = 1;
                
                left++;
                right--;
            }
            if (left == right) {
                if (image[r][left] == 0)
                    ans[r][left] = 1;
                else
                    ans[r][left] = 0;
            }
        }

        return ans;
    }
};