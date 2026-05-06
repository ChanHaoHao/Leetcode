class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        // Apply gravity
        int ROW = boxGrid.size(), COL = boxGrid[0].size();

        for (int r=0; r<ROW; ++r) {
            int next_free = COL-1;
            for (int c=COL-1; c>=0; --c) {
                // stationary obstacle
                if (boxGrid[r][c] == '*') {
                    next_free = c-1;
                }
                else if (boxGrid[r][c] == '#') {
                    boxGrid[r][c] = '.';
                    boxGrid[r][next_free] = '#';
                    next_free -= 1;
                }
            }
        }

        vector<vector<char>> rotate(COL, vector<char>(ROW, '.'));
        for (int r=0; r<ROW; ++r) {
            for (int c=0; c<COL; ++c) {
                rotate[c][ROW-1-r] = boxGrid[r][c];
            }
        }  

        return rotate;
    }
};