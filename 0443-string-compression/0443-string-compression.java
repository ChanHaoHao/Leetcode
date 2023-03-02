class Solution {
    public int compress(char[] chars) {
        int count=1, ans=0;
        for (int i=1; i<chars.length; i++) {
            if (chars[i]==chars[i-1]) {
                count++;
                continue;
            }
            else {
                chars[ans++]=chars[i-1];
                if (count>1) {
                    String tmp=Integer.toString(count);
                    for (int j=0; j<tmp.length(); j++) {
                        chars[ans++]=tmp.charAt(j);
                    }
                }
                count=1;
            }
        }

        chars[ans++]=chars[chars.length-1];
        if (count>1) {
            String tmp=Integer.toString(count);
            for (int j=0; j<tmp.length(); j++) {
                chars[ans++]=tmp.charAt(j);
            }
        }

        return ans;
    }
}