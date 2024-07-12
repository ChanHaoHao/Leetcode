#include <string.h>

class Solution {
public:
    int maximumGain(string s, int x, int y) {
        int ans = 0;
        string high_prior, low_prior;
        int score[2];

        if (x > y)
        {
            high_prior = "ab";
            low_prior = "ba";
            score[0] = x;
            score[1] = y;
        }
        else
        {
            high_prior = "ba";
            low_prior = "ab";
            score[0] = y;
            score[1] = x;
        }

        deque<char> first;
        for (int i=0; i<s.length(); i++)
        {
            if (first.empty())
            {
                first.push_back(s[i]);
            }
            else
            {
                if (first.back()==high_prior[0] && s[i]==high_prior[1])
                {
                    first.pop_back();
                }
                else
                {
                    first.push_back(s[i]);
                }
            }
        }

        ans = (s.length()-first.size())*score[0]/2;

        stack<char> second;
        int first_size = first.size();
        for (int i=0; i<first_size; i++)
        {
            char tmp = first.front();
            first.pop_front();
            if (second.empty())
            {
                second.push(tmp);
            }
            else
            {
                if (second.top()==low_prior[0] && tmp==low_prior[1])
                {
                    second.pop();
                }
                else
                {
                    second.push(tmp);
                }
            }
        }

        ans += (first_size-second.size())*score[1]/2;
        return ans;
    }
};