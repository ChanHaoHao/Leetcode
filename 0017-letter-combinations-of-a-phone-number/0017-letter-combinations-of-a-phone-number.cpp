class Solution {
public:
    void backtrack(unordered_map<char, vector<char>>& mp, string& digits, int i, string substr, vector<string>& ans) {
        if (i == digits.length()) {
            ans.push_back(substr);
            return;
        }

        for (auto c: mp[digits[i]]) {
            string tmp = substr + c;
            backtrack(mp, digits, i+1, tmp, ans);
        }
    }

    vector<string> letterCombinations(string digits) {
        unordered_map<char, vector<char>> mp;
        mp['2'] = {'a', 'b', 'c'};
        mp['3'] = {'d', 'e', 'f'};
        mp['4'] = {'g', 'h', 'i'};
        mp['5'] = {'j', 'k', 'l'};
        mp['6'] = {'m', 'n', 'o'};
        mp['7'] = {'p', 'q', 'r', 's'};
        mp['8'] = {'t', 'u', 'v'};
        mp['9'] = {'w', 'x', 'y', 'z'};

        vector<string> ans;
        backtrack(mp, digits, 0, "", ans);

        return ans;
    }
};