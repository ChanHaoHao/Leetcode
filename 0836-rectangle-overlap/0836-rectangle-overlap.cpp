class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        int x_max = max(rec1[0], rec2[0]);
        int x_min = min(rec1[2], rec2[2]);
        int y_max = max(rec1[1], rec2[1]);
        int y_min = min(rec1[3], rec2[3]);

        if (x_max < x_min && y_max < y_min) {
            return true;
        }
        return false;
    }
};