#ifndef QUEUE_ARRAY_H_
#define QUEUE_ARRAY_H_

#include <stdlib.h>
#include <stdbool.h>

#define QUEUE_MAX_SIZE 20

typedef struct queue {
    int value[QUEUE_MAX_SIZE];
    int front, back;
} queue;

queue *q_create();
bool q_enqueue(queue *q, int val);
bool q_dequeue(queue *q, int *val);
bool q_is_empty(queue *q);

#endif