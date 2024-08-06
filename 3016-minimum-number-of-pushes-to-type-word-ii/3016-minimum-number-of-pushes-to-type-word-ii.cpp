class Solution {
public:
    int minimumPushes(string word) {
        // the counting doesn't need to be stored in a map, because we don't care the mapping
        vector<int> counting(26);
        for (char &c:word)
        {
            counting[c-'a']++;
        }

        // sort it in reverse
        sort(counting.rbegin(), counting.rend());
        int ans = 0;
        for (int i=0; i<26; i++)
        {
            ans += (i/8+1)*counting[i];
        }

        return ans;
    }
};