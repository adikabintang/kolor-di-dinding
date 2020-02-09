// delete middle node
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

typedef struct Node Node;

void remove_middle(Node *n)
{
    n->data = n->next->data;
    n->next = n->next->next;
    free(n->next);
}

void print_ll(Node *head) {
    Node *current = head;
    while (current != NULL) {
        printf("%d\n", current->data);
        current = current->next;
    }
}

int main()
{
    Node *head = (Node *)malloc(sizeof(Node));
    head->data = 1;
    head->next = (Node *)malloc(sizeof(Node));

    head->next->data = 2;
    head->next->next = (Node *)malloc(sizeof(Node));

    head->next->next->data = 3;
    head->next->next->next = NULL;

    print_ll(head);
    printf("---\n");
    remove_middle(head->next);
    print_ll(head);

    return 0;
}
