#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node {
    int val;
    struct node *next;
} node;

// remember, global variable is useful when doing multithreading
// otherwise the var will be copied the other threads' stacks
node *head = NULL;
node *current = NULL;

bool list_append(int val) {
    node *new_node = malloc(sizeof(node));
    if (new_node == NULL) {
        return false;
    }
    new_node->val = val;

    if (head == NULL) {
        head = new_node;
        current = head;
    }

    new_node->next = head;
    current->next = new_node;
    current = new_node;
    return true;
}

void list_iterate(node *head) {
    node *ptr = head;
    if (ptr == NULL)
        return;

    do {
        printf("%d\n", ptr->val);
        ptr = ptr->next;
    } while (ptr != head);
}

int main() {
    list_append(1);
    list_append(2);
    list_append(3);
    list_iterate(head);
    return 0;
}