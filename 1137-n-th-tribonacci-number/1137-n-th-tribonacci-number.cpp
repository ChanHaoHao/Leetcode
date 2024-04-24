class Solution {
public:
    int tribonacci(int n) {
        int tri_array[] = {0, 1, 1};
        if (n<2)
        {
            return tri_array[n];
        }
        n = n-2;

        for (n; n>0; n--)
        {
            int tmp = tri_array[0]+tri_array[1]+tri_array[2];
            tri_array[0] = tri_array[1];
            tri_array[1] = tri_array[2];
            tri_array[2] = tmp;
        }
        return tri_array[2];
    }
};