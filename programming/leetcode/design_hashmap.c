/**
 * https://leetcode.com/problems/design-hashmap/
 * Runtime: 252 ms, faster than 6.25% of C online submissions
 * Memory Usage: 314.9 MB, less than 100.00% of C online submissions 
 */

#include <stdio.h>
#include <stdlib.h>

#define HASHMAP_SIZE 1000000

typedef struct {
    int key;
    int value;
} MyHashMap;

/** Initialize your data structure here. */

MyHashMap* myHashMapCreate() {
    MyHashMap *obj = malloc(sizeof(MyHashMap) * HASHMAP_SIZE);
    int i = 0;
    for (i = 0; i < HASHMAP_SIZE; i++) {
        (obj + i)->value = -1;
    }
    return obj;
}

/** value will always be non-negative. */
void myHashMapPut(MyHashMap* obj, int key, int value) {
    MyHashMap *p = obj + key;
    p->value = value;
}

/** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
int myHashMapGet(MyHashMap* obj, int key) {
    if (key < HASHMAP_SIZE && key >= 0) {
        return (obj + key)->value;
    }
    return -1;
}

/** Removes the mapping of the specified value key if this map contains a mapping for the key */
void myHashMapRemove(MyHashMap* obj, int key) {
    if (key < HASHMAP_SIZE && key >= 0) {
        (obj + key)->value = -1;
    }
}

void myHashMapFree(MyHashMap* obj) {
    free(obj);
}

int main() {
    MyHashMap* obj = myHashMapCreate();
    myHashMapPut(obj, 1, 2);
 
    int param_2 = myHashMapGet(obj, 1);
    printf("param_2: %d\n", param_2);
 
    myHashMapRemove(obj, 1);
 
    myHashMapFree(obj);
}
