#include <stdio.h>
#include "hash_table.h"

int main() {
    int v = 0;
    hash_table *h = ht_create();
    ht_insert(h, 1, 10);
    if (ht_get(h, 1, &v)) {
        printf("val: %d\n", v);
    }
    else
    {
        printf("not found\n");
    }
    
    return 0;
}
