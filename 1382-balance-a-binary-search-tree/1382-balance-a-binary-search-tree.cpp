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
    TreeNode* constructBST(vector<int>& vals, int left, int right) {
        if (left > right)
            return nullptr;
        
        int mid = (left + right) / 2;
        TreeNode* node = new TreeNode(vals[mid]);
        node->left = constructBST(vals, left, mid-1);
        node->right = constructBST(vals, mid+1, right);

        return node;
    }

    TreeNode* balanceBST(TreeNode* root) {
        vector<int> vals;
        stack<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* curr = q.top();
            q.pop();

            if (curr != nullptr) {
                vals.push_back(curr->val);
                q.push(curr->right);
                q.push(curr->left);
            }
        }

        sort(vals.begin(), vals.end());

        return constructBST(vals, 0, vals.size()-1);
    }
};