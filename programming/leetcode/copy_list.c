#include <stdio.h>
#include <stdlib.h>

struct Node {
    int val;
    struct TreeNode *next;
    struct TreeNode *random;
};

struct Node* copyRandomList(struct Node* head) {
    struct Node *res;
    struct Node *pr;
    struct Node *ph = head;

    if (head != NULL)
    {
        res = malloc(sizeof(struct Node));
        pr = res;
    }

    while (ph != NULL)
    {
        pr->val = ph->val;
        ph = ph->next;
        if (ph != NULL)
        {
            pr->next = malloc(sizeof(struct Node));
            pr = pr->next;
        }
    }

    ph = head;
    pr = res;
    while (ph != NULL)
    {
        if (ph->random == NULL)
        {
            pr->random = NULL;
        }
        else
        {
            
        }
        ph = ph->next;
        pr = pr->next;
    }
}

int main()
{
    return 0;
}