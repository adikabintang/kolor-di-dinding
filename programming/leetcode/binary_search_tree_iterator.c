// https://leetcode.com/problems/binary-search-tree-iterator/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct {
    struct TreeNode *ptr;
} BSTIterator;


BSTIterator* bSTIteratorCreate(struct TreeNode* root) {
    BSTIterator *iterator = malloc(sizeof(BSTIterator));
    if (!iterator) {
        perror("failed to malloc\n");
        exit(-1);
    }
    iterator->ptr = root;
    return iterator;
}

bool helper(struct TreeNode *root, int *val) {
    bool stop = false;
    if (root) {
        stop = helper(root->left, val);
        if (stop) {
            *val = root->val;
            return true;
        }
        return helper(root->right, val);
    }
    return true;
}

/** @return the next smallest number */
int bSTIteratorNext(BSTIterator* obj) {
    if (obj->ptr) {
        bSTIteratorNext(obj->ptr->left);
        int val = obj->ptr->val;
        return val;
    }
}

/** @return whether we have a next smallest number */
bool bSTIteratorHasNext(BSTIterator* obj) {
  
}

void bSTIteratorFree(BSTIterator* obj) {
    
}

struct TreeNode *create_bst();

int main() {
    BSTIterator* obj = bSTIteratorCreate(create_bst());
    int param_1 = bSTIteratorNext(obj);
 
    bool param_2 = bSTIteratorHasNext(obj);
 
    bSTIteratorFree(obj);
    return 0;
}

struct TreeNode *create_bst() {
    struct TreeNode *root;
    root = malloc(sizeof(struct TreeNode));
    root->val = 2;
    root->left = malloc(sizeof(struct TreeNode));;
    root->left->val = 1;
    root->left->left = NULL;
    root->left->right = NULL;
    root->right = malloc(sizeof(struct TreeNode));
    root->right->val = 3;
    root->right->left = NULL;
    root->right->right = NULL;
    return root;
}