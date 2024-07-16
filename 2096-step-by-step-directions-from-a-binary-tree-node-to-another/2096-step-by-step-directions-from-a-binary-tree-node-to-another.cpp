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
    vector<char> * path1;
    vector<char> * path2;

    bool dfs(TreeNode* root, vector<char>* path, int value)
    {
        if (root->val==value)
        {
            return true;
        }

        if (root->left!=NULL)
        {
            path->push_back('L');
            if (dfs(root->left, path, value))
            {
                return true;
            }
            path->pop_back();
        }
        if (root->right!=NULL)
        {
            path->push_back('R');
            if (dfs(root->right, path, value))
            {
                return true;
            }
            path->pop_back();
        }

        return false;
    }

    string getDirections(TreeNode* root, int startValue, int destValue) {
        path1 = new vector<char> {};
        path2 = new vector<char> {};

        dfs(root, path1, startValue);
        dfs(root, path2, destValue);

        vector<char> new_path1 = *path1;
        vector<char> new_path2 = *path2;

        int i=0;
        while (i<new_path1.size() && i<new_path2.size())
        {
            if (new_path1[i]==new_path2[i])
            {
                i++;
            }
            else
            {
                break;
            }
        }
        
        string ans="";
        for (int tmp=i; tmp<path1->size(); tmp++)
        {
            ans += "U";
        }
        for (int tmp=i; tmp<new_path2.size(); tmp++)
        {
            ans+=new_path2[tmp];
        }

        return ans;
    }
};