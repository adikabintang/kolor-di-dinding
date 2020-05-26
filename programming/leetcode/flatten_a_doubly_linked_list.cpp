// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list
// Runtime: 0 ms, faster than 100.00% of C++ online submissions 
// Memory Usage: 7.4 MB, less than 100.00% of C++ online submissions 
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flatten(Node* head) {
        Node *ptr = head, *next = NULL;
        while (ptr) {
            if (ptr->child) {
                next = ptr->next;
                ptr->next = flatten(ptr->child);
                ptr->next->prev = ptr;
                ptr->child = NULL;
                while (ptr->next) {
                    ptr = ptr->next;
                }
                if (next) {
                    ptr->next = next;
                    next->prev = ptr;   
                }
            }
            ptr = ptr->next;
        }
        return head;
    }
};