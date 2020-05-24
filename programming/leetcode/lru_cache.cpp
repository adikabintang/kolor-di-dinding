/**
 * https://leetcode.com/problems/lru-cache/submissions/
 * Runtime: 184 ms, faster than 46.97% of C++ online submissions
 * Memory Usage: 40.8 MB, less than 6.10% of C++ online submissions
 */
#include <iostream>
#include <memory>
#include <unordered_map>

// TODO: make this as template class
class DoublyLinkedListNode
{
public:
    int key, value;
    std::shared_ptr<DoublyLinkedListNode> next, prev;
    DoublyLinkedListNode()
    {
    }

    DoublyLinkedListNode(int key, int value) {
        this->key = key;
        this->value = value;
    }
};

class LRUCache
{
private:
    std::unordered_map<int, std::shared_ptr<DoublyLinkedListNode>> cache;
    int capacity, counter;

    // headered doubly linked list
    // oldest->data1->data2->data3->latest
    std::shared_ptr<DoublyLinkedListNode> latest, oldest;

    // https://herbsutter.com/2013/06/05/gotw-91-solution-smart-pointer-parameters/
    void addToLatest(std::shared_ptr<DoublyLinkedListNode> &n) {
        auto current_latest = latest->prev;
        n->prev = current_latest;
        n->next = latest;
        latest->prev = n;
        current_latest->next = n;
    }

    void moveToLatest(std::shared_ptr<DoublyLinkedListNode> &n) {
        auto prev = n->prev;
        auto next = n->next;
        prev->next = next;
        next->prev = prev;
        addToLatest(n);
    }

    int removeTheOldest() {
        auto n = oldest->next;
        auto next = n->next;
        int key = n->key;
        // reference counter -= 1
        oldest->next = next;
        next->prev = oldest;
        return key;
    }

public:
    LRUCache(int capacity) : latest(new DoublyLinkedListNode()),
                             oldest(new DoublyLinkedListNode())
    {
        this->capacity = capacity;
        this->counter = 0;
        oldest->next = latest;
        oldest->prev = nullptr;
        latest->prev = oldest;
        latest->next = nullptr;
    }

    int get(int key)
    {
        if (cache.find(key) == cache.end())
            return -1;

        auto n = cache[key];
        moveToLatest(n);
        return n->value;
    }

    void put(int key, int value)
    {
        std::shared_ptr<DoublyLinkedListNode> n;
        if (cache.find(key) != cache.end()) {
            n = cache[key];
            n->value = value;
            moveToLatest(n);
            return;
        }

        n = std::make_shared<DoublyLinkedListNode>(key, value);
        cache.insert(std::make_pair(key, n));
        if (counter < capacity) {
            counter++;
        }
        else {
            // get the oldest, remove
            int key = removeTheOldest();
            // reference counter -= 1
            cache.erase(key);
        }

        addToLatest(n);
    }
};

int main()
{
    LRUCache *obj = new LRUCache(2);
    //int param_1 = obj->get(1);
    obj->put(1, 1);
    obj->put(2, 2);
    obj->put(1, 10);
    obj->put(3, 3);
    std::cout << obj->get(1) << std::endl;
    std::cout << obj->get(2) << std::endl;
    std::cout << obj->get(3) << std::endl;

    return 0;
}
