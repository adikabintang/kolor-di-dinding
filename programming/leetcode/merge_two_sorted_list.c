#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *ptr_1 = l1;
    struct ListNode *ptr_2 = l2;
    struct ListNode *new_node;
    struct ListNode *ptr_new;

    if (l1 != NULL || l2 != NULL)
    {
        new_node = malloc(sizeof(struct ListNode));
        ptr_new = new_node;
    }

    while (ptr_1 != NULL && ptr_2 != NULL)
    {
        if (ptr_1->val < ptr_2->val)
        {
            ptr_new->val = ptr_1->val;
            ptr_1 = ptr_1->next;
        }
        else if (ptr_1->val > ptr_2->val)
        {
            ptr_new->val = ptr_2->val;
            ptr_2 = ptr_2->next;
        }
        else
        {
            ptr_new->val = ptr_1->val;
            ptr_new->next = malloc(sizeof(struct ListNode));
            ptr_new = ptr_new->next;
            ptr_new->val = ptr_2->val;
            ptr_1 = ptr_1->next;
            ptr_2 = ptr_2->next;
        }
        if (ptr_1 != NULL && ptr_2 != NULL)
        {
            ptr_new->next = malloc(sizeof(struct ListNode));
            ptr_new = ptr_new->next;
        }        
    }

    if (ptr_1 != NULL || ptr_2 != NULL)
    {
        struct ListNode *p = ptr_1 == NULL ? ptr_2 : ptr_1;    
        ptr_new->next = malloc(sizeof(struct ListNode));
        ptr_new = ptr_new->next;
        while (p != NULL)
        {
            ptr_new->val = p->val;
            p = p->next;
            if (p != NULL)
            {
                ptr_new->next = malloc(sizeof(struct ListNode));
                ptr_new = ptr_new->next;
            }
        }
    }

    ptr_new = NULL;
    
    return new_node;
}

struct ListNode *ll_init(int *arr, int arr_size)
{
    int i = 0;
    struct ListNode *head;
    if (arr_size > 0) {
        head = malloc(sizeof(struct ListNode));
    }
    struct ListNode *ptr = head;
    for (i = 0; i < arr_size; i++)
    {
        ptr->val = arr[i];
        if (i < arr_size - 1)
        {
            ptr->next = malloc(sizeof(struct ListNode));
        }
        ptr = ptr->next;
    }
    return head;
}

void ll_print(struct ListNode *head)
{
    struct ListNode *ptr = head;
    while (ptr != NULL)
    {
        printf("%d, ", ptr->val);
        ptr = ptr->next;
    }
    printf("\n");
}

int main()
{
    int arr_1[3] = {1, 2, 4};
    int arr_2[3] = {1, 3, 4};
    struct ListNode *l1 = ll_init(arr_1, 3);
    struct ListNode *l2 = ll_init(arr_2, 3);
    struct ListNode *n = mergeTwoLists(l1, l2);
    ll_print(n);
    return 0;
}