class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        // Calculate the number of
        unordered_map<string, int> counter;
        for (auto &x: arr)
        {
            counter[x]++;
        }

        for (auto &n: arr)
        {
            // If n is distinct
            if (counter[n]==1)
            {
                k-=1;
            }
            if (k==0)
            {
                return n;
            }
        }
        return "";
    }
};