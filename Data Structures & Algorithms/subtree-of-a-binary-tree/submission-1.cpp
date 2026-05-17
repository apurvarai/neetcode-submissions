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
bool sametree(TreeNode* root1,TreeNode* root2 ){

    if(!root1 && !root2) return true;

    if(root1 && root2 && root1->val==root2->val)
    return sametree(root1->left,root2->left) && sametree(root1->right,root2->right);
    
    return false;
    }
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(!subRoot) return true;

        if(!root && subRoot) return false;

        if(sametree(root,subRoot)) 
        return true;
        else 
        return isSubtree(root->left,subRoot)||isSubtree(root->right,subRoot);


        
    }
};
