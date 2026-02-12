class Solution {
public:
    int triangularSum(vector<int>& nums) {
        queue<int> q;

        for (int n: nums)
            q.push(n);
        
        while (q.size() > 1) {
            int n = q.size()-1;
            for (; n>0; --n) {
                int f = q.front();
                q.pop();
                q.push((f + q.front()) % 10);
            }
            q.pop();
        }

        return q.front();
    }
};