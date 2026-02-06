class Solution {
struct Compare {
    bool operator()(const pair<int, int> a, const pair<int, int> b) {
        return a.first > b.first;
    }
};

public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        // sort the trips by from first, then to
        sort(trips.begin(), trips.end(), [](const vector<int> a, const vector<int> b) {
            if (a[1] == b[1])
                return a[2] < b[2];
            return a[1] < b[1];
        });

        // the priority_queue stores to, passenger
        priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> pq;
        for (auto t: trips) {
            while (!pq.empty() && pq.top().first <= t[1]) {
                capacity += pq.top().second;
                pq.pop();
            }
            capacity -= t[0];
            if (capacity < 0)
                return false;
            pq.push({t[2], t[0]});
        }

        return true;
    }
};