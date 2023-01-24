class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length()>s2.length())
            return false;

        HashMap<Character, Integer> map1 = new HashMap<>();
        HashMap<Character, Integer> map2 = new HashMap<>();
        for (int i=97; i<123; i++) {
            map1.put((char) i, 0);
            map2.put((char) i, 0);
        }
        for (int i=0; i<s1.length(); i++) {
            map1.put(s1.charAt(i), map1.get(s1.charAt(i)) + 1);
            map2.put(s2.charAt(i), map2.get(s2.charAt(i)) + 1);
        }
        int matches=26;
        for (int i=97; i<123; i++) {
            if (!map1.get((char) i).equals(map2.get((char) i)))
                matches--;
        }
//        System.out.println(matches);

        if (matches==26)
            return true;

        for (int i=s1.length(); i<s2.length(); i++) {
            Character o1=s2.charAt(i-s1.length());
            Character o2=s2.charAt(i);
//            System.out.print(o1);
//            System.out.println(o2);
            if (!map1.get(o1).equals(map2.get(o1))) {
                if (map1.get(o1).equals(map2.get(o1)-1))
                    matches++;
            }
            else
                matches--;
            map2.replace(o1, map2.get(o1)-1);

            if (!map1.get(o2).equals(map2.get(o2))) {
                if (map1.get(o2).equals(map2.get(o2)+1))
                    matches++;
            }
            else
                matches--;
            map2.replace(o2, map2.get(o2)+1);
//            System.out.println(matches);
            if (matches==26)
                return true;
        }

        return false;
        
    }
}