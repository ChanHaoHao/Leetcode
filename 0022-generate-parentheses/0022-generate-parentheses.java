class Solution {
    List<String> ans=new ArrayList<>();
    Stack<String> stack=new Stack<>();

    public List<String> generateParenthesis(int n) {
        backtrack(0, 0, n);
        return ans;
    }

    public void backtrack(int openedN, int closedN, int n) {
        if (openedN==n && closedN==n) {
            String tmp="";
            for (String element:stack)
                tmp+=element;
            ans.add(tmp);
            return;
        }

        if (openedN<n) {
            stack.add("(");
            backtrack(openedN+1, closedN, n);
            stack.pop();
        }

        if (closedN<n && openedN>closedN) {
            stack.add(")");
            backtrack(openedN, closedN+1, n);
            stack.pop();
        }
    }
}