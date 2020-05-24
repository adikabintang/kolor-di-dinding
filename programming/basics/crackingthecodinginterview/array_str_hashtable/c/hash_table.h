#ifndef HASH_TABLE_H_
#define HASH_TABLE_H_

#include <stdlib.h>
#include <stdbool.h>

// the capacity should be prime
// https://stackoverflow.com/questions/3980117/hash-table-why-size-should-be-prime
// http://srinvis.blogspot.com/2006/07/hash-table-lengths-and-prime-numbers.html
#define HT_CAPACITY 17

typedef struct ll_node {
    int key;
    int value;
    struct ll_node *next; // for storing collision
} ll_node;

typedef struct hash_table {
    ll_node **table;
} hash_table;

// by the way, why do we like to use heap in C to do OOP style:
// https://stackoverflow.com/questions/31673065/creating-classes-in-c-on-the-stack-vs-the-heap
extern hash_table *ht_create();
extern void ht_insert(hash_table *h, int key, int value);
extern bool ht_get(hash_table *h, int key, int *value);
extern void ht_delete(hash_table *h, int key);
extern void ht_free(hash_table *h);

#endif