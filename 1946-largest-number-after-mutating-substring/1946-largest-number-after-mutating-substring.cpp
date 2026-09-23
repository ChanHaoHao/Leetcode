class Solution {
public:
    string maximumNumber(string num, vector<int>& change) {
        int n=num.length(), i=0;
        while (i < n && change[num[i]-'0'] <= num[i]-'0') {
            ++i;
        }

        while (i < n && change[num[i]-'0'] >= num[i]-'0') {
            num[i] = change[num[i]-'0']+'0';
            ++i;
        }

        return num;
    }
};