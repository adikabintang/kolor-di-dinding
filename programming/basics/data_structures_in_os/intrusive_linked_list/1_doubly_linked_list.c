/**
 * 1. https://www.data-structures-in-practice.com/intrusive-linked-lists/
 * 2. https://www.cs.helsinki.fi/group/cpro/harj5_13.pdf
 */
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

typedef struct dlist
{
    struct dlist *next, *prev;
} dlist;

typedef struct item
{
    int val;
    dlist dlist_link;
} item;

item *create_item(int val)
{
    item *i = malloc(sizeof(item));
    if (i)
    {
        i->val = val;
    }
    return i;
}



int main()
{
    item *a = create_item(1);
    item *b = create_item(2);
    return 0;
}