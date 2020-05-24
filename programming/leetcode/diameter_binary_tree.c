// https://leetcode.com/problems/diameter-of-binary-tree/
#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
     int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int global_max = 1;

int get_depth(struct TreeNode *root) {
    if (!root)
        return 0;
    
    int left_depth = get_depth(root->left);
    int right_depth = get_depth(root->right);
    
    // see here, and the difference between this function and get_max_depth()
    if (left_depth + right_depth + 1 > global_max) {
        global_max = left_depth + right_depth + 1;
    }
    
    if (left_depth > right_depth) {
        return left_depth + 1;
    }
    else {
        return right_depth + 1;
    }
}

int diameterOfBinaryTree(struct TreeNode* root){
    global_max = 1;
    get_depth(root);
    return global_max - 1;
}

// https://www.educative.io/edpresso/finding-the-maximum-depth-of-a-binary-tree
int get_max_depth(struct TreeNode *root) {
    if (!root)
        return 0;
    
    int left_depth = get_depth(root->left);
    int right_depth = get_depth(root->right);
    if (left_depth > right_depth) {
        return left_depth + 1;
    }
    else {
        return right_depth + 1;
    }
}

int main() {
    return 0;
}
