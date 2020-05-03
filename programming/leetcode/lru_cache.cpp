#include <iostream>
#include <memory>
#include <unordered_map>

class DLNode {
public:
    int key;
    int val;
    DLNode *prev;
    DLNode *next;
    
    DLNode() {
        prev = NULL;
        next = NULL;
    }

    DLNode(int key, int val) {
        this->key = key;
        this->val = val;
        DLNode();
    }
};

class LRUCache {
public:
    int capacity;
    std::unordered_map<int, DLNode*> cache;
    DLNode *head = NULL;
    DLNode *tail = NULL;
    
    LRUCache(int capacity) {
        this->capacity = capacity;
        head = new DLNode();
        tail = new DLNode();
        head->next = tail;
        tail->prev = head;
    }

    void append_on_head(DLNode *node) {
        node->prev = head;
        node->next = head->next;
        head->next->prev = node;
        head->next = node;
    }

    void move_to_newest(DLNode *node)
    {
        node->prev->next = node->next;
        node->next->prev = node->prev;
        append_on_head(node);
    }

    DLNode *remove_tail()
    {
        DLNode *n = tail->prev;
        tail->prev = tail->prev->prev;
        n->prev->next = tail;
        return n;
    }
    
    int get(int key) {
        if (cache.find(key) == cache.end())
            return -1;
        
        DLNode *n = cache[key];
        move_to_newest(n);
        
        return n->val;
    }
    
    void put(int key, int value) {
        if (cache.find(key) != cache.end())
        {
            DLNode *n = cache[key];
            n->val = value;
            move_to_newest(n);
            return;
        }

        if (cache.size() >= capacity) {
            // delete the oldest one from queue
            DLNode *t = remove_tail();
            // delele the oldest one from cache
            cache.erase(t->key);
            delete(t);
            t = NULL;
        }
        DLNode *n = new DLNode(key, value);
        append_on_head(n);
        cache.insert(std::make_pair(key, n));
    }

};

int main()
{
    LRUCache* obj = new LRUCache(2);
    //int param_1 = obj->get(1);
    obj->put(1,1);
    obj->put(2,2);
    obj->put(1,10);
    obj->put(3,3);
    std::cout << obj->get(1) << std::endl;
    std::cout << obj->get(2) << std::endl;
    std::cout << obj->get(3) << std::endl;
    
    return 0;
}
