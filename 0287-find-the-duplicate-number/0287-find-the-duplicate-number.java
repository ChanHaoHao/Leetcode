class Solution {
    public int findDuplicate(int[] nums) {
        // HashSet<Integer> set=new HashSet<>();
        // int ans=0;
        // for (int i:nums) {
        //     if (set.contains(i)) {
        //         ans=i;
        //         break;
        //     }
                
        //     set.add(i);
        // }

        // return ans;

        int slow=0, fast=0;
        while (true) {
            slow=nums[slow];
            fast=nums[nums[fast]];
            if (slow==fast)
                break;
        }
        
        int slow2=0;
        while (true) {
            slow=nums[slow];
            slow2=nums[slow2];
            if (slow2==slow)
                break;
        }
        
        return slow;
    }
}