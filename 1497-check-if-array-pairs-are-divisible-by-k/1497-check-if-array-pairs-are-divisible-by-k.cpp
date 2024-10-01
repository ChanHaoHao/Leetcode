class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int> freq;
        for (int i=0; i<k; ++i)
        {
            freq.push_back(0);
        }

        // count the freq of each remaining
        for (int x: arr)
        {
            // ((x%k)+k)%k is used to prevent negative numbers
            freq[((x%k)+k)%k]++;
        }

        // if k is even
        if (k%2==0)
        {
            // We have to consider the middle number and 0
            if (freq[0]%2!=0 || freq[k/2]%2!=0)
            {
                return false;
            }
            for (int i=1; i<k/2; ++i)
            {
                if (freq[i]!=freq[k-i])
                {
                    cout << i;
                    return false;
                }
            }
        }
        else
        {
            if (freq[0]%2!=0)
            {
                return false;
            }
            for (int i=1; i<k/2+1; ++i)
            {
                if (freq[i]!=freq[k-i])
                {
                    return false;
                }
            }
        }

        return true;
    }
};