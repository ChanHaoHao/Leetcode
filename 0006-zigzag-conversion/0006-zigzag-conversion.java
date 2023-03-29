class Solution {
    public String convert(String s, int numRows) {
        if (s.length()<=numRows || numRows==1) {
            return s;
        }

        String ans="";
        boolean frontDir=true;
        int row=0;
        ArrayList<String> trial=new ArrayList<>();
        for (int i=0; i<numRows; i++) {
            trial.add(new String());
        }

        for (int i=0; i<s.length(); i++) {
            String tmp=trial.get(row);
            tmp+=s.charAt(i);
            trial.set(row, tmp);
            if (frontDir) {
                row++;
            }
            else {
                row--;
            }

            if (row==numRows-1) {
                frontDir=false;
            }
            else if (row==0) {
                frontDir=true;
            }
        }

        for (int i=0; i<numRows; i++) {
            ans+=trial.get(i);
        }

        return ans;
    }
}