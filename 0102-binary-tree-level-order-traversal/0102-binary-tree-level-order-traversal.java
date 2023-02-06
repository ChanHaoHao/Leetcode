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
    public List<List<Integer>> levelOrder(TreeNode root) {
        Deque<TreeNode> deque=new ArrayDeque<>();
        List<List<Integer>> ans=new ArrayList<>();

        if (root!=null)
            deque.add(root);
        
        while (!deque.isEmpty()) {
            List<Integer> list=new ArrayList<>();
            TreeNode tmp;
            int size=deque.size();
            for (int i=0; i<size; i++) {
                tmp=deque.pollFirst();
                list.add(tmp.val);
                if (tmp.left!=null)
                    deque.add(tmp.left);
                if (tmp.right!=null)
                    deque.add(tmp.right);
            }

            if (!list.isEmpty())
                ans.add(list);
        }

        return ans;
    }
}