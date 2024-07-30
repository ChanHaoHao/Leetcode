class Solution {
public:
    int minimumDeletions(string s) {
        int ans=0, count=0;

        for (int i=0; i<s.length(); i++)
        {
            // temporalily count the B's
            if (s[i]=='b')
                count +=1;
            // if the current char is an A, and there are Bs in front
            // remove one count and add one to the ans
            // This will allow us to remove the less character in the mixed string
            // if As are greater than Bs, it will remove the Bs, vice versa.
            else if (count!=0)
            {
                count -= 1;
                ans += 1;
            }
        }

        return ans;
    }
};