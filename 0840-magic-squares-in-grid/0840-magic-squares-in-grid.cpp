class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        /*
        the rows, cols, and diags sum will be 15
        possible sum==15 are
        1+5+9 / 1+6+8 / 2+4+9 / 2+5+8 / 2+6+7
        3+4+8 / 3+5+7 / 4+5+6
        The number in the middle used 4 times, so it need to be 5
        The number in the corners used 3 times, so it need to be even numbers
        */
        int m=grid.size(), n=grid[0].size(), ans=0;

        for (int i=0; i<m-2; ++i)
        {
            for (int j=0; j<n-2; ++j)
            {
                ans += helper(i, j, grid);
            }
        }

        return ans;
    }

    int helper(int r, int c, vector<vector<int>>& grid)
    {
        set<int> distinct;
        for (int di=r; di<r+3; ++di)
        {
            for (int dj=c; dj<c+3; ++dj)
            {
                if (distinct.find(grid[di][dj])!=distinct.end() || grid[di][dj]<1 || grid[di][dj]>9)
                    return 0;
                distinct.insert(grid[di][dj]);
            }
        }
        // cout << "passed distinct " << endl;

        if (grid[r+1][c+1]!=5)
            return 0;
        // cout << "passed 1 " << endl;
        // cout << grid[r][c]%2 << " " << grid[r][c+2]%2 << " " << grid[r+2][c]%2 << " " << grid[r+2][c+2]%2 << endl;
        if (grid[r][c]%2!=0 || grid[r][c+2]%2!=0 || grid[r+2][c]%2!=0 || grid[r+2][c+2]%2!=0)
            return 0;
        // cout << "passed 2 " << endl;
        if ((15-grid[r][c]-grid[r][c+2])!=grid[r][c+1])
            return 0;
        // cout << "passed 3 " << endl;
        if ((15-grid[r+2][c]-grid[r+2][c+2])!=grid[r+2][c+1])
            return 0;
        // cout << "passed 4 " << endl;
        if ((15-grid[r][c]-grid[r+2][c])!=grid[r+1][c])
            return 0;
        // cout << "passed 5 " << endl;
        if ((15-grid[r][c+2]-grid[r+2][c+2])!=grid[r+1][c+2])
            return 0;
        // cout << "passed 6 " << endl;

        return 1;
    }
};