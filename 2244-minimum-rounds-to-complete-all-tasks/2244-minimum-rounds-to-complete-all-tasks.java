import java.util.Arrays;

class Solution {
    public int minimumRounds(int[] tasks) {
        if (tasks.length==1) {
            return -1;
        }
        Arrays.sort(tasks);
        Stack<Integer> st = new Stack<Integer>();
        for (int i : tasks) {
            st.push(i);
        }
        int prev=st.pop();
        int count=1;
        int ans=0;
        while(!st.isEmpty()) {
            if (prev==st.peek()) {
                st.pop();
                count++;
            }
            else {
                if (count==1) {
                    return -1;
                }
                prev=st.pop();
                ans+=count/3;
                if (count%3>0) {
                    ans++;
                }
                count=1;
            }
        }
        if (count==1) {
            return -1;
        }
        ans+=count/3;
        if (count%3!=0) {
            ans++;
        }
        return ans;
    }
}