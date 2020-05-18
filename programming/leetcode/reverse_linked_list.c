// https://leetcode.com/problems/reverse-linked-list/
// Runtime: 0 ms, faster than 100.00% of C online submissions
// Memory Usage: 6.2 MB, less than 100.00% of C online submissions
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *current = head;
    struct ListNode *result = NULL, *prev_res = NULL;
    
    while (current != NULL) {
        result = malloc(sizeof(struct ListNode));
        result->val = current->val;
        result->next = prev_res;
        prev_res = result;
        current = current->next;
    }
    
    return result;
}
