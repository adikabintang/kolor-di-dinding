#include <stdio.h>

#define MAX_BUFF 10

typedef struct circular_buffer {
    int buff[MAX_BUFF];
    size_t top_idx;
    size_t size;
} circular_buffer;

void push(circular_buffer *cb, int value) {
    cb->buff[cb->top_idx] = value;
    cb->top_idx++;
    cb->top_idx = MAX_BUFF % cb->top_idx;
    cb->size++;
    if (cb->size > MAX_BUFF)
        cb->size = MAX_BUFF;
}

bool get(circular_buffer *cb, int *val) {
    if (cb->size <= 0) {
        return false;
    }

    *val = cb->buff[--cb->top_idx];
    cb->size--;
    return true;
}
