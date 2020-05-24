// idea: https://www.programiz.com/dsa/heap-data-structure
#include "heap.h"

#define GET_LEFT_CHILD_IDX(idx) 2 * idx + 1
#define GET_RIGHT_CHILD_IDX(idx) 2 * idx + 2
#define GET_PARENT_IDX(idx) (int) idx / 2

heap *heap_create(heap_type type) {
    heap *h = malloc(sizeof(heap));
    h->size = 0;
    h->type = type;
    return h;
}

static bool __max_heap_push(heap *h, int val) {
    size_t last_idx = h->size;
    int parent_idx = GET_PARENT_IDX(last_idx);
    int temp = 0;

    if (last_idx >= HEAP_MAX_SIZE)
        return false;

    h->arr[last_idx] = val;
    while (parent_idx >= 0 && h->arr[parent_idx] < h->arr[last_idx]) {
        temp = h->arr[parent_idx];
        h->arr[parent_idx] = h->arr[last_idx];
        h->arr[last_idx] = temp;
        last_idx = parent_idx;
        parent_idx = GET_PARENT_IDX(last_idx);
    }
    h->size++;
    return true;
}

static bool __min_heap_push(heap *h, int val) {
    size_t last_idx = h->size;
    int parent_idx = GET_PARENT_IDX(last_idx);
    int temp = 0;

    if (last_idx >= HEAP_MAX_SIZE)
        return false;

    h->arr[last_idx] = val;
    while (parent_idx >= 0 && h->arr[parent_idx] > h->arr[last_idx]) {
        temp = h->arr[parent_idx];
        h->arr[parent_idx] = h->arr[last_idx];
        h->arr[last_idx] = temp;
        last_idx = parent_idx;
        parent_idx = GET_PARENT_IDX(last_idx);
    }

    h->size++;
    return true;
}

static bool __max_heap_pop(heap *h, int *returned_val) {
    size_t i = 0; 
    int temp = 0;
    int left_child_idx = GET_LEFT_CHILD_IDX(0);
    int right_child_idx = GET_RIGHT_CHILD_IDX(0);
    int largest_child_idx = 0;

    if (h->size <= 0) 
        return false;

    *returned_val = h->arr[0];
    h->arr[i] = h->arr[h->size - 1];
    h->size--;
    while (left_child_idx < h->size || right_child_idx < h->size) {
        if (left_child_idx < h->size && right_child_idx < h->size) {
            largest_child_idx = (h->arr[left_child_idx] >= 
                h->arr[right_child_idx] ? left_child_idx : right_child_idx);
        }
        else if (left_child_idx < h->size) {
            largest_child_idx = left_child_idx;
        }
        else {
            largest_child_idx = right_child_idx;
        }

        if (h->arr[i] < h->arr[largest_child_idx]) {
            temp = h->arr[i];
            h->arr[i] = h->arr[largest_child_idx];
            h->arr[largest_child_idx] = temp;
            i = largest_child_idx;
            left_child_idx = GET_LEFT_CHILD_IDX(i);
            right_child_idx = GET_RIGHT_CHILD_IDX(i);
        }
        else {
            break;
        }
    }

    return true;
}

static bool __min_heap_pop(heap *h, int *returned_val) {
    size_t i = 0;
    int temp = 0;
    int left_child_idx = GET_LEFT_CHILD_IDX(0);
    int right_child_idx = GET_RIGHT_CHILD_IDX(0);
    int smallest_child_idx = 0;

    if (h->size <= 0) 
        return false;

    *returned_val = h->arr[0];
    h->arr[i] = h->arr[h->size - 1];
    h->size--;
    while (left_child_idx < h->size || right_child_idx < h->size) {
        if (left_child_idx < h->size && right_child_idx < h->size) {
            smallest_child_idx = (h->arr[left_child_idx] <= 
                h->arr[right_child_idx] ? left_child_idx : right_child_idx);
        }
        else if (left_child_idx < h->size) {
            smallest_child_idx = left_child_idx;
        }
        else {
            smallest_child_idx = right_child_idx;
        }

        if (h->arr[i] > h->arr[smallest_child_idx]) {
            temp = h->arr[i];
            h->arr[i] = h->arr[smallest_child_idx];
            h->arr[smallest_child_idx] = temp;
            i = smallest_child_idx;
            left_child_idx = GET_LEFT_CHILD_IDX(i);
            right_child_idx = GET_RIGHT_CHILD_IDX(i);
        }
        else {
            break;
        }
    }

    return true;
}

bool heap_push(heap *h, int val) {
    if (h->type == MAX_HEAP)
        return __max_heap_push(h, val);
    else
        return __min_heap_push(h, val);
}

bool heap_pop(heap *h, int *returned_val) {
    if (h->type == MAX_HEAP)
        return __max_heap_pop(h, returned_val);
    else
        return __min_heap_pop(h, returned_val);
}
