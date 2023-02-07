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
    public boolean isValidBST(TreeNode root) {
        return valid(root, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);
    }

    private boolean valid(TreeNode node, double left, double right) {
        if (node==null) {
            return true;
        }

        if (!(node.val<right && node.val>left)) {
            return false;
        }

        return valid(node.left, left, (double)node.val) && valid(node.right, (double)node.val, right);
    }
}