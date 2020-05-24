/**
 * https://leetcode.com/problems/copy-list-with-random-pointer
 * Runtime: 8 ms, faster than 90.38% of C online submissions 
 * Memory Usage: 8 MB, less than 100.00% of C online submissions
 */
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int val;
    struct Node *next;
    struct Node *random;
};

void iterate(struct Node *head) {
    struct Node *p = head;
    while (p) {
        printf("[n: %d, rand: %d], ", p->val, (p->random ? p->random->val : -69));
        p = p->next;
    }
    printf("\n---\n");
}

struct Node* copyRandomList(struct Node* head) {
	struct Node *ptr = head, *n = NULL;
    struct Node *p_res = NULL, *result = NULL;
    
    if (!head)
        return result;
    
    while (ptr) {
        n = malloc(sizeof(struct Node));
        n->val = ptr->val;
        n->next = ptr->next;
        ptr->next = n;
        ptr = n->next;
    }
    
    ptr = head;
    while (ptr) {
        if (ptr->random) {
            ptr->next->random = ptr->random->next;    
        }
        else {
            ptr->next->random = NULL;
        }
        
        ptr = ptr->next->next;
    }
    
    ptr = head;
    p_res = ptr->next;
    result = p_res;
    while (ptr) {
        
        ptr->next = p_res->next;
        ptr = ptr->next;
        p_res->next = ptr ? ptr->next : NULL;
        p_res = p_res->next;
    }
    
    return result;
}

int main() {
    struct Node *head = malloc(sizeof(struct Node));
    head->val = 1;
    head->next = malloc(sizeof(struct Node));
    head->next->val = 2;
    head->next->next = malloc(sizeof(struct Node));
    head->next->next->val = 3;
    head->next->next->next = NULL;
    head->random = head->next->next;
    head->next->random = NULL;
    head->next->next->random = head->next;
    printf("original: \n");
    iterate(head);
    struct Node *p = copyRandomList(head);
    //iterate(p);
    return 0;
}