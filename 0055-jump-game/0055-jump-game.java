class Solution {
    public boolean canJump(int[] nums) {
        int index=0;

        for (int i=0; i<nums.length; i++) {
            if (index==i && nums[i]==0)
                break;
            index=Math.max(index, i+nums[i]);
        }

        if (index>=nums.length-1)
            return true;
        else
            return false;
    }
}