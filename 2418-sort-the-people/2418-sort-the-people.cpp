class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        // int n = names.size();

        // for (int i=0; i<n; i++)
        // {
        //     for (int j=i+1; j<n; j++)
        //     {
        //         if (heights[i]<heights[j])
        //         {
        //             int height = heights[i];
        //             heights[i] = heights[j];
        //             heights[j] = height;
        //             string name = names[i];
        //             names[i] = names[j];
        //             names[j] = name;
        //         }
        //     }
        // }

        // return names;
        vector<pair<int, string>> merged;
        for (int i=0; i<names.size(); i++)
            merged.push_back({heights[i], names[i]});
        sort(merged.rbegin(), merged.rend());

        vector<string> ans;
        for (auto &name: merged)
            ans.push_back(name.second);

        return ans;
    }
};