class Solution {
public:
    bool isValid(string s) {
        stack<char> storage;

        for (int i=0; i<s.length(); i++)
        {
            if (s[i]=='(' || s[i]=='{' || s[i]=='[')
                storage.push(s[i]);
            else
            {
                if (storage.empty())
                    return false;
                char tmp = storage.top();
                if (s[i]==')' && tmp!='(')
                    return false;
                else if (s[i]=='}' && tmp!='{')
                    return false;
                else if (s[i]==']' && tmp!='[')
                    return false;
                storage.pop();
            }
        }

        if (storage.empty())
            return true;
        return false;
    }
};