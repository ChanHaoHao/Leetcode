/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        unordered_set<int> to_delete_set(to_delete.begin(), to_delete.end());
        vector<TreeNode*> ans;

        root = process_node(root, ans, to_delete_set);
        if (root!=NULL)
            ans.push_back(root);
        
        return ans;
    }

    TreeNode* process_node(TreeNode* node, vector<TreeNode*>& ans, unordered_set<int>& to_delete_set)
    {
        if (node==NULL)
            return NULL;

        // This allows us to check the node from the bottom
        node->left = process_node(node->left, ans, to_delete_set);
        node->right = process_node(node->right, ans, to_delete_set);

        if (to_delete_set.contains(node->val))
        {
            if (node->left!=NULL)
                ans.push_back(node->left);
            if (node->right!=NULL)
                ans.push_back(node->right);
            return NULL;
        }

        return node;
    }
};