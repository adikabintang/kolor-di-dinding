// http://www.mathcs.emory.edu/~cheung/Courses/255/Syllabus/1-C-intro/bit-array.html
// with this arr[10], normally we can store "like a set" of 10 numbers
// with bit array, each int is 32 bit, we can store 320 numbers
// arr[0]: 0-31, arr[1]: 32-63, etc
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define BIT_ARR_MAX 10

void bit_arr_set(int *arr, int val) {
    int idx = (int)val / (sizeof(int) * 8); // val / 32
    int bit_pos = val % (sizeof(int) * 8);
    int bit_repr = 1 << bit_pos;
    arr[idx] |= bit_repr;
}

bool bit_arr_check(int *arr, int val) {
    int idx = (int)val / (sizeof(int) * 8); // val / 32
    int bit_pos = val % (sizeof(int) * 8);
    int bit_repr = 1 << bit_pos;
    return arr[idx] & bit_repr;
}

void bit_arr_clear(int *arr, int val) {
    int idx = (int)val / (sizeof(int) * 8); // val / 32
    int bit_pos = val % (sizeof(int) * 8);
    int bit_repr_reversed = ~(1 << bit_pos);
    arr[idx] &= bit_repr_reversed;
}

int main() {
    int i = 0, arr[BIT_ARR_MAX] = { 0 };
    bit_arr_set(arr, 100);
    if (bit_arr_check(arr, 100)) {
        printf("100 exists\n");
    }
    bit_arr_clear(arr, 100);
    if (bit_arr_check(arr, 100)) {
        printf("100 exists\n");
    }
    else {
        printf("100 does not exist\n");
    }
    return 0;
}
