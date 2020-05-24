/**
 * https://leetcode.com/problems/palindrome-linked-list
 * Runtime: 16 ms, faster than 20.91% of C online submissions
 * Memory Usage: 11.1 MB, less than 16.67% of C online submissions
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


bool isPalindrome(struct ListNode* head){
    struct ListNode *ptr = head, *rev_ptr = NULL, *n = NULL;
    
    while (ptr) {
        n = malloc(sizeof(struct ListNode));
        n->val = ptr->val;
        n->next = rev_ptr;
        rev_ptr = n;
        ptr = ptr->next;
    }
    
    ptr = head;
    while (ptr) {
        if (ptr->val != rev_ptr->val) {
            return false;
        }
        ptr = ptr->next;
        rev_ptr = rev_ptr->next;
    }

    // duh ommit the free()
    
    return true;
}
