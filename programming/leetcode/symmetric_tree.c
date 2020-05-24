/**
 * https://leetcode.com/problems/symmetric-tree/
 */

bool is_mirror(struct TreeNode *left, struct TreeNode *right) {
    if (!left && !right)
        return true;
    if (!left || !right)
        return false;
    return (left->val == right->val) && is_mirror(left->left, right->right) && 
        is_mirror(left->right, right->left);
}

bool isSymmetric(struct TreeNode* root){
    return is_mirror(root, root);
}
