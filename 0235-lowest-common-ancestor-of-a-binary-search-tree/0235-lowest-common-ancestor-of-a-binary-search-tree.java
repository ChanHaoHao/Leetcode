/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // while (root.val!=p.val && root.val!=q.val && ((root.val-p.val)/Math.abs(root.val-p.val))*((root.val-q.val)/Math.abs(root.val-q.val))>0) {
        //     if (root.val>p.val) {
        //         root=root.left;
        //     }
        //     else
        //         root=root.right;
        // }
        while (root!=null) {
            if (root.val>p.val && root.val>q.val)
            root=root.left;
        else if (root.val<p.val && root.val<q.val)
            root=root.right;
        else
            break;
        }
        
        return root;
    }
}