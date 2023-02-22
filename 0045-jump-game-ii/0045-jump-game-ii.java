class Solution {
    public int jump(int[] nums) {
        int ans=0, end=0, farthest=0;

        for (int i=0; i<nums.length-1; i++) {
            farthest=Math.max(farthest, i+nums[i]);
            if (farthest>=nums.length-1) {
                ans++;
                break;
            }
            if (i==end) {
                ans++;
                end=farthest;
            }
        }

        return ans;
    }
    
    // My thought, but TLE
    // int ans=0;
    // public int jump(int[] nums) {
    //     if (nums.length==0) {
    //         return 0;
    //     }

    //     bfs(0, 0, nums);
    //     return ans;
    // }

    // private void bfs(int curr, int jump, int[] nums) {
    //     if (curr>=nums.length-1) {
    //         if (jump<ans || ans==0) {
    //             ans=jump;
    //         }
    //         return;
    //     }

    //     if (jump>ans && ans!=0) {
    //         return;
    //     }

    //     int que;
    //     if (curr+nums[curr]<nums.length) {
    //         que=nums[curr];
    //     }
    //     else {
    //         que=nums.length-curr;
    //     }

    //     for (int i=que; i>0; i--) {
    //         bfs(curr+i, jump+1, nums);
    //     }
    // }
}