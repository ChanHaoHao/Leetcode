class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        std::priority_queue<pair<int, int>, std::vector<pair<int, int>>, greater<pair<int, int>>> pq;

        for (int i=0; i<nums.size(); ++i) {
            pq.push({nums[i], i});

            if (pq.size() > k) {
                pq.pop();
            }
        }

        std::vector<int> ans;
        while (!pq.empty()) {
            ans.push_back(pq.top().second);
            pq.pop();
        }

        std::sort(ans.begin(), ans.end());
        for (int i=0; i<ans.size(); ++i) {
            ans[i] = nums[ans[i]];
        }
        return ans;
    }
};