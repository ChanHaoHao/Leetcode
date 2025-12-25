class Solution {
public:
    // A custom comparison function
    static bool compare(const std::vector<int>& v1, const std::vector<int>& v2) {
        if (v1[0]==v2[0])
            return v1[1]<v2[1];
        return v1[0]<v2[0];
    }

    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), compare);
        int ans=1, n=points.size(), start=points[0][0], end=points[0][1];

        for (int i=1; i<n; i++)
        {
            if (points[i][0]>end)
            {
                ans += 1;
                end = points[i][1];
            }
            else
            {
                end = min(end, points[i][1]);
            }
        }

        return ans;
    }
};