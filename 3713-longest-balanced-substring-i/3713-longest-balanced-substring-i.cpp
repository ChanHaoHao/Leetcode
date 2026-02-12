class Solution {
public:
    int isBalanced(unordered_map<char,int> &mp){
        int mini = INT_MAX, maxi = 0;
        for (auto p : mp) {
            mini = min(mini, p.second);
            maxi = max(maxi, p.second);
        }
        return mini == maxi;
    }

    int longestBalanced(string s) {
        int n = s.size();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            unordered_map<char,int> mp;  
            for (int j = i; j < n; j++) {
                mp[s[j]]++;
                if (isBalanced(mp)) {
                    ans = max(ans, j - i + 1);
                }
            }
        }
        return ans;
    }
};