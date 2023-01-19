class Solution {
    public List<List<Integer>> threeSum(int[] nums) {TreeMap<Integer, Integer> map = new TreeMap<>();
        ArrayList<ArrayList<Integer>> tmpAns = new ArrayList<>();

        for (int i:nums) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry:map.entrySet()) {
//            System.out.println("Keys: "+entry.getKey());

            if (entry.getKey()==0 && entry.getValue()>=3)
                tmpAns.add(new ArrayList<Integer>(Arrays.asList(0,0,0)));

            int j=Math.min(entry.getValue(), 2);
            if (j==2) {
                if (map.containsKey(-entry.getKey()*2) && entry.getKey()!=0) {
//                    System.out.println(1);
                    if (entry.getKey()<0)
                        tmpAns.add(new ArrayList<Integer>(Arrays.asList(entry.getKey(), entry.getKey(), -entry.getKey()*2)));
                    else
                        tmpAns.add(new ArrayList<Integer>(Arrays.asList(-entry.getKey()*2, entry.getKey(), entry.getKey())));
//                    System.out.println(Arrays.asList(-entry.getKey()*2, entry.getKey(), entry.getKey()));
                }
            }

            boolean thres=false;
//            System.out.println("    Keys: "+entry.getKey()+" Values: "+entry.getValue());
            for (Map.Entry<Integer, Integer> entry2: map.entrySet()) {
                if (thres) {
                    if (map.containsKey(-entry.getKey() - entry2.getKey()) && -entry.getKey() - entry2.getKey() > entry2.getKey()) {
//                        System.out.println(2);
//                        System.out.println(Arrays.asList(entry.getKey(), entry2.getKey(), -entry.getKey() - entry2.getKey()));
                        tmpAns.add(new ArrayList<Integer>(Arrays.asList(entry.getKey(), entry2.getKey(), -entry.getKey() - entry2.getKey())));
                    }
                }

                if (!thres && entry2.getKey().equals(entry.getKey())) {
                    thres = true;
                }
            }
        }

        List<List<Integer>> ans=new ArrayList<List<Integer>>();
        for (int i=0; i<tmpAns.size(); i++) {
            ArrayList<Integer> tmp=tmpAns.get(i);
            ans.add(Arrays.asList(tmp.get(0), tmp.get(1), tmp.get(2)));
        }
        return ans;
    }
}