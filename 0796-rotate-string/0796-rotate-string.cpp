class Solution {
public:
    bool rotateString(string s, string goal) {
        if (s.length() != goal.length()) {
            return false;
        }
        
        int n = s.length();
        string s2 = s + s;
        for (int i=0; i<s2.length()-1; ++i) {
            if (s2.substr(i, n) == goal) {
                return true;
            }
        }

        return false;
    }
};