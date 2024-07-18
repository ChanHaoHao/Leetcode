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
    int countPairs(TreeNode* root, int distance) {
        traverseTree(root, graph, leafs);
        int ans = 0;

        for (auto node : leafs)
        {
            unordered_set<TreeNode*> passed;
            passed.insert(node);
            queue<TreeNode*> node_queue;
            node_queue.push(node);
    
            // using the idea from editorial, do the bfs in a for-loop instead of a while-loop
            for (int dist=0; dist<distance+1; dist++)
            {
                int n = node_queue.size();
                for (int i=0; i<n; i++)
                {
                    TreeNode* curr = node_queue.front();
                    node_queue.pop();
                    passed.insert(curr);

                    if (leafs.contains(curr) && curr!=node)
                        ans += 1;
                    else
                    {
                        for (auto next : graph[curr])
                        {
                            if (!passed.contains(next))
                                node_queue.push(next);
                        }
                    }
                }
            }
        }

        return ans/2;
    }

private:
    unordered_map<TreeNode*, vector<TreeNode*>> graph;
    unordered_set<TreeNode*> leafs;

    void traverseTree(TreeNode* node, unordered_map<TreeNode*, vector<TreeNode*>>& graph, unordered_set<TreeNode*>& leafs)
    {
        if (!node->left && !node->right) 
        {
            leafs.insert(node);
            return;
        }

        if (node->left)
        {
            graph[node->left].push_back(node);
            graph[node].push_back(node->left);
            traverseTree(node->left, graph, leafs);
        }

        if (node->right)
        {
            graph[node->right].push_back(node);
            graph[node].push_back(node->right);
            traverseTree(node->right, graph, leafs);
        }

        return;
    }
};