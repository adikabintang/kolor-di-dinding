#include "hash_table.h"
#include <assert.h>

size_t __get_idx(int key) {
    return key % HT_CAPACITY;
}

// how Java implements collision avoidance: 
// https://stackoverflow.com/questions/4980757/how-do-hashtables-deal-with-collisions
void ht_insert(hash_table *h, int key, int value) {
    size_t idx = __get_idx(key);
    ll_node *n = NULL;

    n = h->table[idx];
    while (n) {
        if (n->key == key) {
            n->value = value;
            return;
        }
        n = n->next;
    }
    
    // prepend at the head of linked list
    n = malloc(sizeof(ll_node));
    assert(n);
    n->key = key;
    n->value = value;
    n->next = h->table[idx]; // note for me: it's NULL for the first time, don't be stupidly confused
    h->table[idx] = n;
    
    h->size++;
}

hash_table *ht_create() {
    size_t i = 0;
    hash_table *h = NULL;

    h = malloc(sizeof(hash_table));
    assert(h);
    h->size = 0;
    // why llnode * ? table is actually multidimensional array **table
    // if int *a = malloc(sizeof(int)), then to do the same, int **a = malloc(sizeof(int*))
    h->table = malloc(HT_CAPACITY * sizeof(ll_node *));
    assert(h->table);

    for (i = 0; i < HT_CAPACITY; i++) {
        h->table[i] = NULL;
    }
    return h;
}

bool ht_get(hash_table *h, int key, int *value) {
    size_t idx = __get_idx(key);
    ll_node *node = h->table[idx];

    while (node) {
        if (node->key == key) {
            *value = node->value;
            return true;
        }
        node = node->next;
    }

    return false;
}

void ht_delete(hash_table *h, int key) {
    size_t idx = __get_idx(key);
    ll_node *n = NULL, *prev = NULL;

    n = h->table[idx];

    // heh this is not "tasteful" according to Torvalds
    if (n->key == key) {
        h->table[idx] = n->next;
        free(n);
        n = NULL;
        h->size--;
        return;
    }

    prev = n;
    while (n) {
        if (n->key == key) {
            prev->next = n->next;
            free(n);
            h->size--;
            return;
        }
        prev = n;
        n = n->next;
    }
}

void ht_free(hash_table *h) {
    int i = 0;
    ll_node *ptr = NULL, *head = NULL;

    if (h == NULL) return;

    for (i = 0; i < HT_CAPACITY; i++) {
        head = h->table[i];
        ptr = head;
        while (ptr) {
            head = head->next;
            free(ptr);
            ptr = NULL;
            ptr = head;
            h->size--;
        }  
    } 
}
