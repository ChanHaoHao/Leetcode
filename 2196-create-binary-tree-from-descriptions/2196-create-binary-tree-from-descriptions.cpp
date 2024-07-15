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
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        // use set to store distinct values
        unordered_set<int> childs, parents;
        // store the parent, child relation in the map
        unordered_map<int, vector<pair<int, int>>> map;

        int n_descriptions = descriptions.size();
        for (int i=0; i<n_descriptions; i++)
        {
            int parent = descriptions[i][0], child = descriptions[i][1], left = descriptions[i][2];
            parents.insert(parent);
            childs.insert(child);
            map[parent].push_back(make_pair(child, left));
        }

        // check all the values in parents and remove the ones in child to find the root
        for (auto curr = parents.begin(); curr != parents.end();)
        {
            if (childs.find(*curr)!=childs.end())
            {
                // move to the next element in parents
                curr = parents.erase(curr);
            }
            else
            {
                curr++;
            }
        }

        // initialize the root
        TreeNode * root = new TreeNode(*parents.begin());
        queue<TreeNode *> queue;
        queue.push(root);

        // use bfs to construct the tree
        while (!queue.empty())
        {
            TreeNode * parent = queue.front();
            queue.pop();

            // find all the existing child for the parents
            for (auto& childInfo : map[parent->val])
            {
                int childValue = childInfo.first, left = childInfo.second;
                TreeNode * node = new TreeNode(childValue);
                queue.push(node);

                if (left==1)
                {
                    parent->left = node;
                }
                else
                {
                    parent->right = node;
                }
            }
        }

        return root;
    }
};