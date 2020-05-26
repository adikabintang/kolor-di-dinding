// https://leetcode.com/problems/invert-binary-tree/
// Runtime: 0 ms, faster than 100.00% of C online submissions
// Memory Usage: 5.6 MB, less than 100.00% of C online submissions 
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* invertTree(struct TreeNode* root){
    struct TreeNode *left = NULL, *right = NULL;
    if (root == NULL) {
        return NULL;
    }
    
    right = invertTree(root->right);
    left = invertTree(root->left);
    root->left = right;
    root->right = left;
    
    return root;
}