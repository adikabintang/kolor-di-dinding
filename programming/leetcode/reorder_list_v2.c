/**
 * https://leetcode.com/problems/reorder-list/
 * Runtime: 24 ms, faster than 31.18% of C online submissions
 * Memory Usage: 8.7 MB, less than 100.00% of C online submissions
 * 
 * 1. split into two: half-half (or first half = end half + 1)
 * 2. reverse the last half
 * 3. merge
 */
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

int getLength(struct ListNode *head) {
    int l = 0;
    struct ListNode *ptr = head;
    while (ptr) {
        l++;
        ptr = ptr->next;
    }
    return l;
}

struct ListNode *reverse_list(struct ListNode *head) {
    struct ListNode *prev = NULL, *curr = head, *next;
    
    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
        
    }
    
    return prev;
}

void merge(struct ListNode *a, struct ListNode *b) {
    struct ListNode *pa = a, *pb = b, *temp_a, *temp_b;
    
    while (pa && pb) {
        temp_a = pa->next;
        temp_b = pb->next;
        pa->next = pb;
        pb->next = temp_a;
        pa = temp_a;
        pb = temp_b;
    }
}

void reorderList(struct ListNode* head){
    struct ListNode *ptr = head, *mid_ptr = head, *prev;
    int middle = 0, i = 0;
    
    if (!head)
        return;
    
    middle = (int)ceil((double)getLength(head) / (double)2);
    for (i = 0; i < middle; i++) {
        prev = mid_ptr;
        mid_ptr = mid_ptr->next;
    }
        
    mid_ptr = reverse_list(mid_ptr);
    prev->next = NULL;
    merge(ptr, mid_ptr);
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
    head->next->next->next = NULL;
    reorderList(head);
    iterate(head);
    return 0;
}