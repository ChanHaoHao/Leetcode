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

        std::vector<pair<int, int>> topK;
        while (!pq.empty()) {
            topK.push_back(pq.top());
            pq.pop();
        }

        std::sort(topK.begin(), topK.end(), [](const pair<int, int>& a, const pair<int, int>& b) { 
            return a.second < b.second;
        });
        std::vector<int> ans;
        for (const auto& k: topK) {
            ans.push_back(k.first);
        }

        return ans;
    }
};