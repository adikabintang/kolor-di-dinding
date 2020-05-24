/**
 * https://leetcode.com/problems/remove-linked-list-elements
 * Runtime: 20 ms, faster than 13.48% of C online submissions 
 * Memory Usage: 7.8 MB, less than 100.00% of C online submissions
 */

struct ListNode* removeElements(struct ListNode* head, int val){
    struct ListNode *ptr = head, *prev = ptr;
    while (head && head->val == val) {
        head = head->next;
        free(ptr);
        ptr = head;
    }
    while (ptr) {
        if (ptr->val == val) {
            prev->next = ptr->next;
            free(ptr);
            ptr = prev->next;
        }
        else {
            prev = ptr;
            ptr = ptr->next;   
        }
    }
    return head;
}
