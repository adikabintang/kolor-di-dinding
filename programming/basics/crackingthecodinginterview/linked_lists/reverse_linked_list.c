#include <stdio.h>
#include <stdlib.h>

struct node
{
    int val;
    struct node *next;
};

typedef struct node node;

node *ll_init(int *arr, int arr_size)
{
    int i = 0;
    node *head;
    if (arr_size > 0) {
        head = malloc(sizeof(node));
    }
    node *ptr = head;
    for (i = 0; i < arr_size; i++)
    {
        ptr->val = arr[i];
        if (i < arr_size - 1)
        {
            ptr->next = malloc(sizeof(node));
        }
        ptr = ptr->next;
    }
    return head;
}

void ll_reverse(node **head)
{
    node *current = *head;
    node *prev = NULL;
    node *next = current->next;

    while (current != NULL)
    {
        current->next = prev;
        prev = current;
        current = next;
        if (next != NULL)
            next = next->next;
    }
    *head = prev;
}

void ll_print(node *head)
{
    node *ptr = head;
    while (ptr != NULL)
    {
        printf("%d, ", ptr->val);
        ptr = ptr->next;
    }
    printf("\n");
}

int main()
{
    int arr[3] = {1, 2, 3};
    node *head = ll_init(arr, 3);
    ll_print(head);
    ll_reverse(&head);
    ll_print(head);
    
    return 0;
}