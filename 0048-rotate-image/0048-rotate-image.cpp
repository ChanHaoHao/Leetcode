class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();

        // For the layers
        for (int c=0; c<n/2; ++c) {
            // For the layer elements
            for (int i=c; i<n-1-c; ++i) {
                int tmp = matrix[c][i];
                matrix[c][i] = matrix[n-1-i][c];
                matrix[n-1-i][c] = matrix[n-1-c][n-1-i];
                matrix[n-1-c][n-1-i] = matrix[i][n-1-c];
                matrix[i][n-1-c] = tmp;
            }
        }
    }
};