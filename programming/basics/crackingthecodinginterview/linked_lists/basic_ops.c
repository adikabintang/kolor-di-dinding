#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node {
    int val;
    struct node *next;
} node;

node *head = NULL;
node *current = NULL;

bool list_append(int val) {
    node *n = malloc(sizeof(node));
    if (n == NULL)
        return false;
    
    n->val = val;
    n->next = NULL;
    if (head == NULL) {
        head = n;
        current = head;
    }
    else {
        current->next = n;
        current = current->next;
    }
}

void list_iterate() {
    node *ptr = head;
    while (ptr != NULL) {
        printf("-> %d\n", ptr->val);
        ptr = ptr->next;
    }
}

node *find_node(int val) {
    node *ptr = head;
    while (ptr != NULL && ptr->val != val) {
        ptr = ptr->next;
    }
    return ptr;
}

void list_remove_node(node *n) {
    node *ptr = head;
    node *prev = NULL;
    while (ptr != n) {
        prev = ptr;
        ptr = ptr->next;
    }

    if (!ptr) {
        head = n->next;
    }
    else {
        prev->next = n->next;
    }
    free(n);
}

void list_remove_node_linus(node *n) {
    node **indirect = &head;
    while (*indirect != n) {
        indirect = &(*indirect)->next;
    }

    *indirect = n->next;
    free(n);
}

int main() {
    list_append(1);
    list_append(4);
    list_append(5);
    list_append(6);
    list_append(9);
    list_iterate();
    node *n = find_node(4);
    // list_remove_node(n);
    // printf("---\n");
    // list_iterate();
    n = find_node(6);
    list_remove_node_linus(n);
    printf("---\n");
    list_iterate();
    return 0;
}
