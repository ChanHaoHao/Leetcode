class Solution {
public:
    int maximumAmount(vector<vector<int>>& coins) {
        int ROW = coins.size(), COL = coins[0].size();
        vector<vector<vector<long long>>> dp(ROW, vector<vector<long long>>(COL, vector<long long>(3, LLONG_MIN)));

        // Initialize starting cell
        dp[0][0][0] = coins[0][0] >= 0 ? coins[0][0] : coins[0][0];
        if (coins[0][0] < 0) {
            dp[0][0][1] = 0; // neutralize the starting cell
        }

        // Initialize first column
        for (int r = 1; r < ROW; ++r) {
            for (int k = 0; k < 3; ++k) {
                if (dp[r-1][0][k] == LLONG_MIN) continue;
                if (coins[r][0] >= 0) {
                    dp[r][0][k] = max(dp[r][0][k], dp[r-1][0][k] + coins[r][0]);
                } else {
                    // don't neutralize
                    dp[r][0][k] = max(dp[r][0][k], dp[r-1][0][k] + coins[r][0]);
                    // neutralize
                    if (k + 1 <= 2) {
                        dp[r][0][k+1] = max(dp[r][0][k+1], dp[r-1][0][k]);
                    }
                }
            }
        }

        // Initialize first row
        for (int c = 1; c < COL; ++c) {
            for (int k = 0; k < 3; ++k) {
                if (dp[0][c-1][k] == LLONG_MIN) continue;
                if (coins[0][c] >= 0) {
                    dp[0][c][k] = max(dp[0][c][k], dp[0][c-1][k] + coins[0][c]);
                } else {
                    // don't neutralize
                    dp[0][c][k] = max(dp[0][c][k], dp[0][c-1][k] + coins[0][c]);
                    // neutralize
                    if (k + 1 <= 2) {
                        dp[0][c][k+1] = max(dp[0][c][k+1], dp[0][c-1][k]);
                    }
                }
            }
        }

        // Fill the rest of the dp
        for (int r = 1; r < ROW; ++r) {
            for (int c = 1; c < COL; ++c) {
                for (int k = 0; k < 3; ++k) {
                    long long best = LLONG_MIN;
                    if (dp[r-1][c][k] != LLONG_MIN) best = max(best, dp[r-1][c][k]);
                    if (dp[r][c-1][k] != LLONG_MIN) best = max(best, dp[r][c-1][k]);
                    if (best == LLONG_MIN) continue;
                    if (coins[r][c] >= 0) {
                        dp[r][c][k] = max(dp[r][c][k], best + coins[r][c]);
                    } else {
                        // don't neutralize
                        dp[r][c][k] = max(dp[r][c][k], best + coins[r][c]);
                        // neutralize
                        if (k + 1 <= 2) {
                            dp[r][c][k+1] = max(dp[r][c][k+1], best);
                        }
                    }
                }
            }
        }

        // Answer is the max across all k at bottom-right
        return max({dp[ROW-1][COL-1][0], dp[ROW-1][COL-1][1], dp[ROW-1][COL-1][2]});
    }
};

