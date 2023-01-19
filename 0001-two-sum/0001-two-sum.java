class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        HashMap<Integer, Integer> index = new HashMap<>();
        int i;
        for (i=0; i<nums.length; i++) {
            if (map.containsKey(target-nums[i])) {
                break;
            }
            map.put(nums[i], 1);
            index.put(nums[i], i);
        }
        return new int[]{index.get(target-nums[i]), i};
    }
}