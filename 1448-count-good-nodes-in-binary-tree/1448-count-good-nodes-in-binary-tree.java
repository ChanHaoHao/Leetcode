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
    int ans=0;

    public int goodNodes(TreeNode root) {
        dfs(root, root.val);

        return ans;
    }

    private void dfs(TreeNode root, int curMax) {
        if (root==null)
            return;

        if (root.val>=curMax)
            ans+=1;
        curMax=Math.max(curMax, root.val);

        if (root.left!=null)
            dfs(root.left, curMax);
        if (root.right!=null)
            dfs(root.right, curMax);
    }
}