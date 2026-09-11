class Solution {
public:
    int totalNumbers(vector<int>& digits) {
        int freq[10] = {0};

        for (int d: digits) {
            freq[d]++;
        }

        int ans = 0;
        for (int i=1; i<10; ++i) {
            freq[i]--;

            if (freq[i] >= 0) {
                for (int j=0; j<10; ++j) {
                    freq[j]--;

                    if (freq[j] >= 0) {
                        for (int k=0; k<10; k=k+2) {
                            freq[k]--;

                            if (freq[k] >= 0) {
                                ans++;
                            }
                            freq[k]++;
                        }
                    }
                    freq[j]++;
                }
            }
            freq[i]++;
        }

        return ans;
    }
};