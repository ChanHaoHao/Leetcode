class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        // count how many students that can accept 0 and 1
        // O(n) = N
        int count0=0, count1=0;

        for (int i=0; i<students.size(); i++) {
            if (students[i])
                count1++;
            else
                count0++;
        }

        // go through all the sandwiches till there are no more students that can accept the current sandwich
        for (int i=0; i<students.size(); i++) {
            if (sandwiches[i]) {
                if (count1==0) {
                    return count0;
                }
                else
                    count1--;
            } 
            else {
                if (count0==0)
                    return count1;
                else
                    count0--;
            }
        }

        return 0;
    }
};