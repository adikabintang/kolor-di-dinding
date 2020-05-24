#include <stdio.h>
#include "heap.h"

int main() {
    int arr[5] = {2, 4, 1, 5, 0};
    int i = 0;
    int val = 0;
    heap *max_heap = heap_create(MAX_HEAP);
    
    printf("pushing...\n");
    for (i = 0; i < 5; i++) {
        if (!heap_push(max_heap, arr[i])) {
            perror("failed to push to the heap");
        }
    }
    printf("popping...\n");
    for (i = 0; i < 5; i++) {
        if (!heap_pop(max_heap, &val)) {
            perror("failed to pop from the heap");
        }
        else {
            printf("%d, ", val);
        }
    }
    printf("\n");

    heap *min_heap = heap_create(MIN_HEAP);
    
    printf("pushing...\n");
    for (i = 0; i < 5; i++) {
        if (!heap_push(min_heap, arr[i])) {
            perror("failed to push to the heap");
        }
    }
    printf("popping...\n");
    for (i = 0; i < 5; i++) {
        if (!heap_pop(min_heap, &val)) {
            perror("failed to pop from the heap");
        }
        else {
            printf("%d, ", val);
        }
    }
    printf("\n");
    return 0;
}
