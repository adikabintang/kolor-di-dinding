#include "hash_table.h"

int __get_idx(int key) {
    return key % HT_CAPACITY;
}

// how Java implements collision avoidance: 
// https://stackoverflow.com/questions/4980757/how-do-hashtables-deal-with-collisions
void ht_insert(hash_table *h, int key, int value) {
    size_t idx = __get_idx(key);
    ll_node **ptr = &(h->table[idx]), **prev = NULL;
    while (*ptr) {
        if ((*ptr)->key == key) {
            (*ptr)->value = value;
            return;
        }
        prev = ptr;
        *ptr = (*ptr)->next;
    }
    *ptr = malloc(sizeof(ll_node));
    (*ptr)->key = key;
    (*ptr)->value = value;
    (*ptr)->next = NULL;
    if (*prev) {
        (*prev)->next = *ptr;
    }
}

hash_table *ht_create() {
    size_t i = 0;
    hash_table *h = malloc(sizeof(hash_table));

    // https://softwareengineering.stackexchange.com/questions/201104/sizeof-style-sizeoftype-or-sizeof-variable
    // sizeof pointer: trying to access a variable that doesn't exist, yet
    h->table = malloc(HT_CAPACITY * sizeof(ll_node *)); 
    
    for (i = 0; i < HT_CAPACITY; i++) {
        h->table[i] = NULL;
    }

    return h;
}

bool ht_get(hash_table *h, int key, int *value) {
    size_t idx = __get_idx(key);
    ll_node *ptr = h->table[idx];
    while (ptr) {
        if (ptr->key == key) {
            *value = ptr->value;
            return true;
        }
        ptr = ptr->next;
    }
    return false;
}

void ht_delete(hash_table *h, int key) {
    size_t idx = __get_idx(key);
    ll_node **ptr = &(h->table[idx]), **prev = ptr, *next;
    ll_node **head = &(h->table[idx]);
    if ((*head)->key == key) {
        *head = (*head)->next;
        free(*ptr);
        return;
    }
    while (*ptr) {
        if ((*ptr)->key == key) {
            next = (*ptr)->next;
            free(*ptr);
            *ptr = next;
            (*prev)->next = *ptr;
            return;
        }
        prev = ptr;
        *ptr = (*ptr)->next;
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
        }  
    } 
}
