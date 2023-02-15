class Solution {
    List<List<Integer>> ans=new ArrayList<>();
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Deque<Integer> tmp=new ArrayDeque<>();
        Arrays.sort(nums);
        dfs(nums, tmp, 0);

        return ans;
    }

    private void dfs(int[] nums, Deque<Integer> tmp, int index) {
        if (index==nums.length) {
            ans.add(new ArrayList<>(tmp));
            return;
        }

        // All subsets that include nums[i]
        tmp.addLast(nums[index]);
        dfs(nums, tmp, index+1);
        tmp.removeLast();

        // All subsets that don't include nums[i]
        while (index+1<nums.length && nums[index]==nums[index+1]) {
            index++;
        }
        dfs(nums, tmp, index+1);
    }
}