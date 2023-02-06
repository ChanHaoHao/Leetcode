/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        Deque<TreeNode> deque=new ArrayDeque<>();
        List<Integer> ans=new ArrayList<>();
        
        if (root!=null) 
            deque.add(root);
        
        while (!deque.isEmpty()) {
            TreeNode tmp=deque.pollLast();
            ans.add(tmp.val);
            int size=deque.size();
            for (int i=0; i<size; i++) {
                TreeNode tmp2=deque.pollFirst();
                if (tmp2.left!=null)
                    deque.add(tmp2.left);
                if (tmp2.right!=null)
                    deque.add(tmp2.right);
            }
            if (tmp.left!=null)
                deque.add(tmp.left);
            if (tmp.right!=null)
                deque.add(tmp.right);
        }
        
        return ans;
    }
}