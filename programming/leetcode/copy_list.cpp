#include <iostream>
#include <unordered_map>

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};


class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node *res;
        Node *pr;
        Node *ph = head;
        std::unordered_map<Node *, Node *> old_new;

        if (head != NULL)
        {
            res = new Node(head->val);
            old_new.insert(std::make_pair(ph, res));
            pr = res;
            ph = ph->next;
        }

        while (ph != NULL)
        {
            pr->next = new Node(ph->val);
            old_new.insert(std::make_pair(ph, pr->next));
            pr = pr->next;
            ph = ph->next;
        }

        pr = res;
        ph = head;
        while (ph != NULL)
        {
            if (ph->random == NULL)
                pr->random = NULL;
            else
            {
                pr->random = old_new[ph->random];
            }
            pr = pr->next;
            ph = ph->next;
        }

        return res;
    }
};

int main()
{

}