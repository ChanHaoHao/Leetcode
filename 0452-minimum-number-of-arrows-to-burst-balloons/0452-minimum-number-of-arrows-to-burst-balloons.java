class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points.length==1){
            return 1;
        }
        
        Arrays.sort(points, new Comparator<int[]>() {
            @Override
            public int compare (int[] o1, int[] o2) {
                if (o1[0]>o2[0]) 
                    return 1;
                else if (o1[0]<o2[0])
                    return -1;
                else {
                    if (o1[1]>o2[1])
                        return 1;
                    else if (o1[1]<o2[1])
                        return -1;
                    else
                        return 0;
                }
            }
        });

        int ans=1;
        int end=points[0][1];

        for (int i=1; i<points.length; i++) {
            if (points[i][0]<=end) {
                end = Math.min(end, points[i][1]);
            }
            else {
                ans++;
                end = points[i][1];
            }
        }
        return ans;
    }
}