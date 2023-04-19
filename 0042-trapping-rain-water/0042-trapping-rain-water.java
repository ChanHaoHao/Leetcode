class Solution {
    public int trap(int[] height) {
        int ans=0, i;
        ArrayList<Integer> traped = new ArrayList<>();

        for (i=0; i<height.length; i++) {
            if (height[i]!=0) {
                traped.add(height[i]);
                break;
            }
        }

        if (i==height.length)
            return 0;

        for (i=i; i<height.length; i++) {
            if (height[i]<traped.get(0)) {
                traped.add(height[i]);
            }
            else {
                if (traped.size()!=1) {
                    for (int j=1; j<traped.size(); j++) {
                        ans += Math.min(traped.get(0), height[i]) - traped.get(j);
                    }
                }
                traped.clear();
                traped.add(height[i]);
            }
        }

        if (traped.size()!=1) {
            ArrayList<Integer> tmp = new ArrayList<>();
            tmp.add(traped.get(traped.size()-1));
            for (i=traped.size()-2; i>-1; i--) {
                if (traped.get(i)<tmp.get(0)) {
                    tmp.add(traped.get(i));
                }
                else {
                    if (tmp.size()!=1) {
                        for (int j=1; j<tmp.size(); j++) {
                            ans += Math.min(tmp.get(0), traped.get(i))-tmp.get(j);
                        }
                    }
                    tmp.clear();
                    tmp.add(traped.get(i));
                }
            }
        }

        return ans;
    }
}