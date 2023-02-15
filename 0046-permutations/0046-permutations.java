class Solution {
    int len;
    List<List<Integer>> ans=new ArrayList<>();
    Deque<Integer> path=new ArrayDeque<>();
    boolean[] used;
    public List<List<Integer>> permute(int[] nums) {
        len=nums.length;

        if (len==0) {
            return ans;
        }

        used=new boolean[len];
        dfs(nums, 0);
        return ans;
    }

    private void dfs(int[] nums, int depth) {
        // if the permutation is made
        if (depth==len) {
            ans.add(new ArrayList<>(path));
            return;
        }

        for (int i=0; i<len; i++) {
            // if the value is used, go to the next value
            if (used[i]) {
                continue;
            }

            // if the value is not used
            path.addLast(nums[i]);
            used[i]=true;
            // go to the next level
            dfs(nums, depth+1);
            // return to the last level
            path.removeLast();
            used[i]=false;
        }
    }
}