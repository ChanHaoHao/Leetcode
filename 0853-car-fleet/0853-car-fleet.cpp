class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        // store (pos, speed)
        vector<pair<int, int>> storage;
        for (int i=0; i<position.size(); ++i) {
            storage.push_back({position[i], speed[i]});
        }

        sort(storage.begin(), storage.end());
        stack<double> time;
        for (auto it = storage.begin(); it < storage.end(); ++it) {
            double t = (target - it->first) / double(it->second);
            while (!time.empty() && time.top() <= t) {
                time.pop();
            }
            time.push(t);
        }

        return time.size();
    }
};