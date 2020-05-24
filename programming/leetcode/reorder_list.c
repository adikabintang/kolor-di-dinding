/**
 * https://leetcode.com/problems/reorder-list/
 * Runtime: 856 ms, faster than 8.60% of C online submissions
 * Memory Usage: 8.7 MB, less than 100.00% of C online submissions
 */
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

void reorderList(struct ListNode* head){
    struct ListNode *ptr = head, *prev_last, *last;
    
    if (!head)
        return;
    
    while (ptr->next) {
        last = ptr;
        while (last->next) {
            prev_last = last;
            last = last->next;
        }
        if (ptr == prev_last || ptr == last)
            break;
        last->next = ptr->next;
        ptr->next = last;
        ptr = last->next;
        prev_last->next = NULL;
    }    
}

void iterate(struct ListNode *head) {
    struct ListNode *ptr = head;
    while (ptr) {
        printf("%d, ", ptr->val);
        ptr = ptr->next;
    }
    printf("\n");
}

int main() {
    struct ListNode *head;
    head = malloc(sizeof(struct ListNode));
    head->val = 1;
    head->next = malloc(sizeof(struct ListNode));
    head->next->val = 2;
    head->next->next = malloc(sizeof(struct ListNode));
    head->next->next->val = 3;
    head->next->next->next = malloc(sizeof(struct ListNode));
    head->next->next->next->val = 4;
    head->next->next->next->next = NULL;
    reorderList(head);
    iterate(head);
    return 0;
}