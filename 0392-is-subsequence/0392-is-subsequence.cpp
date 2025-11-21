class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s.length()==0)
            return true;
        int i=0;
        for (auto x: t)
        {
            if (x==s[i])
            {
                i++;
                if (i==s.length())
                {
                    return true;
                }
            }
        }
        return false;
    }
};