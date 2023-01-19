class Solution {
    public int[] productExceptSelf(int[] nums) {
        ArrayList<Integer> indexZero = new ArrayList<>();
        int[] ans=new int[nums.length];

        int product=1;
        for (int i=0; i<nums.length; i++) {
            if (nums[i]==0)
                indexZero.add(i);
            else
                product*=nums[i];
        }

        if (indexZero.size()==0) {
            for (int i=0; i<nums.length; i++) {
                ans[i]=product/nums[i];
            }
        }
        else if (indexZero.size()>1){
            for (int i=0; i<nums.length; i++)
                ans[i]=0;
        }
        else {
            for (int i=0; i<nums.length; i++) {
                if (i==indexZero.get(0)) {
                    ans[i]=product;
                }
                else
                    ans[i]=0;
            }
        }
        return ans;
    }
}