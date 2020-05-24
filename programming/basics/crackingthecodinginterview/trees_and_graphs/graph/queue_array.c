#include "queue_array.h"

queue *q_create() {
    queue *q = malloc(sizeof(queue));
    q->back = -1;
    q->front = 0;
}

bool q_enqueue(queue *q, int val) {
    if (q->front >= QUEUE_MAX_SIZE)
        return false;

    q->value[++q->back] = val;
    return true;    
}

bool q_dequeue(queue *q, int *val) {
    if (q_is_empty(q)) {
        return false;
    }
    *val = q->value[q->front++];
    // reset
    if (q->front > q->back) {
        q->front = 0;
        q->back = -1;
    }
    return true;
}

bool q_is_empty(queue *q) {
    return (q->back < q->front);
}