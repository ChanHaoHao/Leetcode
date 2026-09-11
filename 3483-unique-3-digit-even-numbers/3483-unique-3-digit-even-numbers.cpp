class Solution {
public:
    bool check(int req[], int freq[]) {
        for (int i=0; i<10; ++i) {
            if (req[i] > freq[i])
                return false;
        }
        return true;
    }

    int totalNumbers(vector<int>& digits) {
        int freq[10] = {0};

        for (int d: digits) {
            freq[d]++;
        }

        int ans = 0;
        for (int i=100; i<999; i=i+2) {
            int req[10] = {0};
            int tmp=i;
            while (tmp > 0) {
                req[tmp%10]++;
                tmp = tmp / 10;
            }

            if (check(req, freq)) ans++;
        }

        return ans;
    }
};