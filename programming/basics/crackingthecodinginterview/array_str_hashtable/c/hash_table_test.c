#include <stdio.h>
#include "hash_table.h"

int main() {
    int v = 0;
    size_t i = 0;
    hash_table *h = ht_create();
    for (i = 1; i <= 3; i++) {
        if (ht_get(h, i, &v)) {
            printf("val: %d\n", v);
        }
        else
        {
            printf("not found\n");
        }
    }
    printf("!!!\n");
    ht_insert(h, 1, 10);
    ht_insert(h, 2, 20);
    ht_insert(h, 3, 30);

    for (i = 1; i <= 3; i++) {
        if (ht_get(h, i, &v)) {
            printf("val: %d\n", v);
        }
        else
        {
            printf("not found\n");
        }
    }

    ht_delete(h, 1);

    for (i = 1; i <= 3; i++) {
        if (ht_get(h, i, &v)) {
            printf("val: %d\n", v);
        }
        else
        {
            printf("not found\n");
        }
    }

    ht_free(h);
    printf("---\n");
    for (i = 1; i <= 3; i++) {
        if (ht_get(h, i, &v)) {
            printf("val: %d\n", v);
        }
        else
        {
            printf("not found\n");
        }
    }
    printf("size: %d\n", h->size);

    return 0;
}
