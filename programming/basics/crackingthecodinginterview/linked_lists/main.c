#include <stdio.h>
#include <stdlib.h>

struct node
{
    int val;
    struct node *next;
};

typedef struct node node;

void remove_duplicate(node *head)
{
    node *current = head;
    int counter = 0;
    node *before;
    node *iterator = head;
    
    while (current != NULL) {
        iterator = head;
            
        while (iterator != NULL) {
            if (iterator->val == current->val) {
                counter++;
            }

            if (counter == 2) {
                before->next = iterator->next;
                free(iterator);
                break;
            }

            before = iterator;
            iterator = iterator->next;
        }
        counter = 0;
        current = current->next;
    }
}

int main()
{
    node *head = (node *) malloc(sizeof(node));
    head->val = 9;
    head->next = NULL;

    node *a = (node *) malloc(sizeof(node));
    a->val = 9;
    a->next = NULL;

    node *b = (node *) malloc(sizeof(node));
    b->val = 9;
    b->next = NULL;

    head->next = a;
    a->next = b;

    node *current = head;
    while (current != NULL) {
        printf("%d\n", current->val);
        current = current->next;
    }

    remove_duplicate(head);
    printf("---\n");

    current = head;
    while (current != NULL) {
        printf("%d\n", current->val);
        current = current->next;
    }

    return 0;
}