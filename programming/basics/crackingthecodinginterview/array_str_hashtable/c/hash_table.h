// http://www.cs.yale.edu/homes/aspnes/pinewiki/C(2f)HashTables.html
#ifndef HASH_TABLE_H_
#define HASH_TABLE_H_

#include <stdlib.h>
#include <stdbool.h>

// the capacity should be prime
// https://stackoverflow.com/questions/3980117/hash-table-why-size-should-be-prime
// http://srinvis.blogspot.com/2006/07/hash-table-lengths-and-prime-numbers.html
#define HT_CAPACITY 17

// sizeof any type must be divisible by sizeof(pointer), or 8 in x64 (4 in x86)
// why? because that depends on how much the CPU can access the memory (suhu pernah bilang ini dulu, all hail suhuu)
// that's why this size is 24 bytes
// for storing collision using linked list chaining
typedef struct ll_node {
    int key;
    int value;
    struct ll_node *next;
} ll_node;

typedef struct hash_table {
    size_t size;

    // clearing up confusion
    // if int *a, what *a dereferenced to? int (size 4 bytes). that's why int *a = malloc(sizeof(int))
    // if int **a, what **a dereferenced to? int * (size 8 bytes on x64). that's why int **a = malloc(sizeof(int *))
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