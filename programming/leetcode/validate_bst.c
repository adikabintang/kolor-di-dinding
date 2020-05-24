// https://leetcode.com/problems/validate-binary-search-tree/
// ugly but works
// Runtime: 8 ms, faster than 75.00% of C online submissions 
// Memory Usage: 8.3 MB, less than 100.00% of C online submissions
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int last_val = INT_MIN;
bool first = true;

bool helper(struct TreeNode *root) {
    if (!root)
        return true;
    
    if (!helper(root->left) || (!first && root->val <= last_val)) {
        return false;
    }
    last_val = root->val;
    first = false;
    return helper(root->right);
}

bool isValidBST(struct TreeNode* root){
    last_val = INT_MIN;
    first = true;
    return helper(root);
}

int main() {
    struct TreeNode *root;
    root = malloc(sizeof(struct TreeNode));
    root->val = 2;
    // root->left = malloc(sizeof(struct TreeNode));;
    // root->left->val = 1;
    // root->left->left = NULL;
    // root->left->right = NULL;
    // root->right = malloc(sizeof(struct TreeNode));
    // root->right->val = 3;
    // root->right->left = NULL;
    // root->right->right = NULL;
    
    printf("r = %d\n", isValidBST(root));

    return 0;
}
