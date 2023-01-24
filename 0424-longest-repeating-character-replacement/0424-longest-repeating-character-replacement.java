class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character, Integer> map=new HashMap<>();
        int ans=0;

        int left=0;
        for (int right=0; right<s.length(); right++) {
            map.put(s.charAt(right), map.getOrDefault(s.charAt(right), 0)+1);
            int max=0;
            for (Map.Entry<Character, Integer> entry:map.entrySet())
                max=Math.max(max, entry.getValue());

            while ((right-left+1-max)>k) {
                map.replace(s.charAt(left), map.get(s.charAt(left))-1);
                left++;
            }

            ans=Math.max(ans, right-left+1);
        }

        return ans;
    }
}