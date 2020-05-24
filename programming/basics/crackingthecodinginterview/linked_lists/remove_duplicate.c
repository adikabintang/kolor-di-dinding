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
        counter = 0;    
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
        
        current = current->next;
    }
}

void print_ll(node *head)
{
    node *current = head;
    while (current != NULL) {
        printf("%d\n", current->val);
        current = current->next;
    }
}

node *reverse_ll(node *head)
{
    node *current = head;
    node *prev = NULL;
    node *next = current->next;

    while (next != NULL) {
        current->next = prev;
        prev = current;
        current = next;
        next = next->next;
    }

    current->next = prev;
    return current;
}

int main()
{
    node *head = (node *) malloc(sizeof(node));
    head->val = 1;
    head->next = NULL;

    node *a = (node *) malloc(sizeof(node));
    a->val = 2;
    a->next = NULL;

    node *b = (node *) malloc(sizeof(node));
    b->val = 3;
    b->next = NULL;

    node *c = (node *) malloc(sizeof(node));
    c->val = 4;
    c->next = NULL;

    head->next = a;
    a->next = b;
    b->next = c;

    print_ll(head);

    //remove_duplicate(head);
    node *new_head = reverse_ll(head);
    printf("---\n");

    print_ll(new_head);
    return 0;
}