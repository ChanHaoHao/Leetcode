class Solution {
public:
    string reverseParentheses(string s) {
        stack<int> pos;
        string ans = "";
        
        for (int i=0; i<s.length(); i++)
        {
            if (s[i] == '(')
            {
                pos.push(ans.length());
            }
            else if (s[i] == ')')
            {
                int index = pos.top();
                pos.pop();
                reverse(ans.begin()+index, ans.end());
            }
            else
            {
                ans += s[i];   
            }
        }
        
        return ans;
    }
};