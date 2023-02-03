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
    boolean indicator=true;
    public boolean isBalanced(TreeNode root) {
        dfs(root);
        return indicator;
    }

    private int dfs(TreeNode root) {
        if (root==null || !indicator)
            return 0;

        int left=dfs(root.left), right=dfs(root.right);
        if (Math.abs(left-right)>1)
            indicator=false;
        return 1+Math.max(left, right);
    }
}