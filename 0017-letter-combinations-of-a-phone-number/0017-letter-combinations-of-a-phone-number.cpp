class Solution {
public:
    void backtracking(string digits, int digit, string combination, vector<string>& ans, unordered_map<char, vector<char>>& dict)
    {
        if (digit==digits.length())
        {
            ans.push_back(combination);
            return;
        }
        
        vector<char> candidates = dict[digits[digit]];
        for (auto i : candidates)
        {
            backtracking(digits, digit+1, combination+i, ans, dict);
        }

        return;
    }

    vector<string> letterCombinations(string digits) { 
        vector<string> ans;
        int n = digits.length();
        if (n==0)
            return ans;

        unordered_map<char, vector<char>> dict = {{'2', {'a', 'b', 'c'}}, {'3', {'d', 'e', 'f'}},
                                                {'4', {'g', 'h', 'i'}}, {'5', {'j', 'k', 'l'}},
                                                {'6', {'m', 'n', 'o'}}, {'7', {'p', 'q', 'r', 's'}},
                                                {'8', {'t', 'u', 'v'}}, {'9', {'w', 'x', 'y', 'z'}}};

        backtracking(digits, 0, "", ans, dict);

        return ans;
    }
};