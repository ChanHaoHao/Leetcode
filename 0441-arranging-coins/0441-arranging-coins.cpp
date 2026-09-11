class Solution {
public:
    int arrangeCoins(int n) {
        int l=0, r=n;

        while (l < r) {
            int mid = (l + r) / 2;
            long long coins = ((long long) mid * (mid + 1) / 2);
            if (coins > n) {
                r = mid;
            }
            else {
                l = mid + 1;
            }
        }

        if (((long long) r * (r+1) / 2) > n) {
            return r - 1;
        }
        return r;
    }
};