#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include "queue_array.h"

int main() {
    int val = 0;
    queue *q = q_create();

    printf("empty: %d\n", q_is_empty(q));
    q_enqueue(q, 1);
    q_enqueue(q, 2);
    printf("empty: %d\n", q_is_empty(q));
    q_dequeue(q, &val);
    printf("val: %d\n", val);
    q_dequeue(q, &val);
    printf("val: %d\n", val);
    printf("empty: %d\n", q_is_empty(q));
    q_enqueue(q, 6);
    q_enqueue(q, 7);
    printf("empty: %d\n", q_is_empty(q));
    q_dequeue(q, &val);
    printf("val: %d\n", val);
    q_dequeue(q, &val);
    printf("val: %d\n", val);
    printf("empty: %d\n", q_is_empty(q));
    return 0;
}
