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
    public int maxDepth(TreeNode root) {
        // recursive
        if (root==null)
            return 0;

        return 1+Math.max(maxDepth(root.left), maxDepth(root.right));

        // DFS 
        // Stack<TreeNode> stack=new Stack<>();
        // Stack<Integer> stack2=new Stack<>();
        // stack.add(root);
        // stack2.add(1);
        
        // int ans=0;
        // while (!stack.isEmpty()) {
        //     TreeNode node=stack.pop();
        //     int depth=stack2.pop();
            
        //     if (node!=null) {
        //         ans=Math.max(ans, depth);
        //         stack.add(node.left);
        //         stack2.add(depth+1);
        //         stack.add(node.right);
        //         stack2.add(depth+1);
        //     }
        // }
        
        // return ans;

        // BFS
        // Deque<TreeNode> deque=new LinkedList<>();
        // if (root!=null)
        //     deque.add(root);
        
        // int level=0;
        
        // while (!deque.isEmpty()) {
        //     for (int i=0; i<deque.size(); i++) {
        //         TreeNode node=deque.pollFirst();
        //         if (node.left!=null)
        //             deque.add(node.left);
        //         if (node.right!=null)
        //             deque.add(node.right);
        //     }
        //     level++;
        // }
        // return level;
    }
}