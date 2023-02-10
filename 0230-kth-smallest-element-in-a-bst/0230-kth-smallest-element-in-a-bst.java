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
    // TreeSet<Integer> tree=new TreeSet<>();
    public int kthSmallest(TreeNode root, int k) {
        // dfs(root);

        // int index=1, ans=0;
        // for (int value:tree) {
        //     if (index!=k) {
        //         index++;
        //         continue;
        //     }
        //     else {
        //         ans=value;
        //         break;
        //     }
        // }

        // return ans;

        // contains the node we have to pop back
        Stack<TreeNode> stack=new Stack<>();
        TreeNode curr=root;

        while (!stack.isEmpty() || curr!=null) {
            while (curr!=null) {
                stack.add(curr);
                curr=curr.left;
            }
            // go back to the last node that is not null
            curr=stack.pop();
            k--;
            if (k==0) {
                return curr.val;
            }
            // and go to the right of the last node
            curr=curr.right;
        }

        return curr.val;
    }

    // private void dfs(TreeNode root) {
    //     if (root==null)
    //         return;

    //     tree.add(root.val);
    //     if (root.left!=null)
    //         dfs(root.left);
    //     if (root.right!=null)
    //         dfs(root.right);
    // }
}