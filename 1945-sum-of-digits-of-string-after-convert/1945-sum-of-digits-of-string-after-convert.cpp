class Solution {
public:
    int getLucky(string s, int k) {
        int ans=0;
        for (auto x: s)
        {
            int num = x-96;
            while (num>0)
            {
                ans += num%10;
                num /= 10;
            }
        }

        for (int i=1; i<k; i++)
        {
            int tmp=0;
            while (ans>0)
            {
                tmp += ans%10;
                ans /= 10;
            }
            ans = tmp;
        }

        return ans;
    }
};