// https://leetcode.com/problems/subtree-of-another-tree/
// Runtime: 8 ms, faster than 100.00% of C online submissions
// Memory Usage: 11 MB, less than 100.00% of C online submissions 
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool is_subtree_helper(struct TreeNode *s, struct TreeNode *t);

bool isSubtree(struct TreeNode* s, struct TreeNode* t){
    bool res = false;
    if (s != NULL && t != NULL) {
        if (s->val == t->val) {
            if (is_subtree_helper(s, t))
                return true;
        }
        if (isSubtree(s->left, t) || isSubtree(s->right, t)) {
            return true;
        }
    } else if (s == NULL && t != NULL || s != NULL || t == NULL)
        return false;
    else
        return true;
    
    return res;
}

bool is_subtree_helper(struct TreeNode *s, struct TreeNode *t)
{
    bool same = false;
    if (t == NULL && s == NULL)
        same = true;
    
    if (t != NULL && s != NULL) {
        if (t->val == s->val) {
            same = is_subtree_helper(s->left, t->left) && \
                is_subtree_helper(s->right, t->right);
        }
    }
    if (t == NULL && s != NULL || t != NULL && s == NULL)
        same = false;
    return same;
}

int main()
{
    struct TreeNode t;
    struct TreeNode s;
    s.val = 9;
    s.left = NULL;
    s.right = NULL;
    t.val = 4;
    t.left = NULL;
    t.right = NULL;
    printf("%d\n", isSubtree(&s, &t));
    return 0;
}