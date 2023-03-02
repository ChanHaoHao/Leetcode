class Solution {
    public int[] sortArray(int[] nums) {

        mergesort(nums, 0, nums.length-1);
        return nums;
    }

    private void mergesort(int[] nums, int left, int right) {
        if (left>=right) {
            return;
        }

        int mid=(left+right)/2;
        mergesort(nums, left, mid);
        mergesort(nums, mid+1, right);
        merge(nums, left, mid, right);
    }

    private void merge(int[] nums, int left, int mid, int right) {
        int len1=mid-left+1;
        int len2=right-mid;

        int[] leftSub=new int[len1], rightSub=new int[len2];

        for (int i=0; i<len1; i++) {
            leftSub[i]=nums[i+left];
        }
        for (int i=0; i<len2; i++) {
            rightSub[i]=nums[mid+1+i];
        }

        int i=0, j=0, k=left;
        while (i<len1 || j<len2) {
            if (j==len2 || i<len1 && leftSub[i]<=rightSub[j]) {
                nums[k++]=leftSub[i++];
            }
            else {
                nums[k++]=rightSub[j++];
            }
        }
    }

    
}