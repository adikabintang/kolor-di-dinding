/**
 * 1. https://www.data-structures-in-practice.com/intrusive-linked-lists/
 * 2. https://www.cs.helsinki.fi/group/cpro/harj5_13.pdf
 * 3. https://0xax.gitbooks.io/linux-insides/content/DataStructures/
 * 4. https://github.com/robbiev/coh-linkedlist
 */
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

typedef struct list
{
    struct list *next;
} list;

typedef struct item
{
    int val;
    list list_items;
} item;

void print_all(item *head)
{
    list *current = &head->list_items;
    while (current != NULL)
    {
        // what is this: see the above link (1) and (2) question 7
        // the point is: we can get the address of the struct by finding the
        // offset of the member from the object
        item *n = (void *)(current)-offsetof(item, list_items);
        printf("-> %d\n", n->val);
        current = current->next;
    }
}

int main()
{
    item *a = malloc(sizeof(item));
    item *b = malloc(sizeof(item));

    a->val = 1;
    b->val = 2;
    a->list_items.next = &(b->list_items);
    b->list_items.next = NULL;

    print_all(a);

    return 0;
}
