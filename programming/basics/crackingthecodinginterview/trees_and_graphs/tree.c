#include <stdio.h>
#include <stdlib.h>

#define MAX_CHILDREN 4

typedef struct node {
    int val;
    struct node children[MAX_CHILDREN];
} node;

typedef struct tree
{
    node root;
} tree;
