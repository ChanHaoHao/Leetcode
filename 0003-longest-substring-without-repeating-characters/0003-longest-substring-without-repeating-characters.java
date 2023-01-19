class Solution {
    public int lengthOfLongestSubstring(String s) {
        ArrayList<Character> list=new ArrayList<>();
        int ans=0;

        for (int i=0; i<s.length(); i++) {
            while (list.contains(s.charAt(i))) {
                list.remove(0);
            }
            list.add(s.charAt(i));
            ans=Math.max(ans, list.size());
        }

        return ans;
    }
}