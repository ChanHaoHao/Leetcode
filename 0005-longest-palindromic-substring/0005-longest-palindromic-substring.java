class Solution {
    public String longestPalindrome(String s) {
        String ans="";
        // check the palidrome from the middle
        for (int i=0; i<s.length(); i++) {
            int left=i, right=i;

            // if the length of palidrome is odd
            while (left>=0 && right<s.length() && s.charAt(left)==s.charAt(right)) {
                left--;
                right++;
            }
            if ((right-left-2+1)>ans.length()) {
                ans=s.substring(left+1, right);
            }

            // if the length of the palidrome is even
            left=i;
            right=i+1;
            while (left>=0 && right<s.length() && s.charAt(left)==s.charAt(right)) {
                left--;
                right++;
            }
            if ((right-left-2+1)>ans.length()) {
                ans=s.substring(left+1, right);
            }
        }

        return ans;
    }
}