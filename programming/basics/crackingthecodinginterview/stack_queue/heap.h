#ifndef HEAP_H_
#define HEAP_H_

#include <stdlib.h>
#include <stdbool.h>

#define HEAP_MAX_SIZE 10

typedef enum heap_type {
    MAX_HEAP,
    MIN_HEAP
} heap_type;

typedef struct heap {
    int arr[HEAP_MAX_SIZE];
    size_t size;
    heap_type type;
} heap;

extern heap *heap_create(heap_type type);
extern bool heap_push(heap *h, int val);
extern bool heap_pop(heap *h, int *returned_val);

#endif
