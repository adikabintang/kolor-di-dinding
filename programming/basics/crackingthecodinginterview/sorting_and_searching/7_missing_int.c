#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

#define ARR_SIZE 10

void set_bit(unsigned int *arr, unsigned int arr_size, unsigned int value) {
    unsigned int index = (unsigned int)value / arr_size;
    int bit_position = value % arr_size;
    int bit_repr = 1;
    bit_repr = bit_repr << bit_position;
    arr[index] = arr[index] | bit_repr;
}

bool check_bit(int *arr, int arr_size, int value) {
    int index = (int)value / arr_size;
    int bit_position = value % arr_size;
    int bit_repr = 1;
    bit_repr = bit_repr << bit_position;
    return (arr[index] & bit_repr);
}

int reveal_zero(int *arr, unsigned int arr_size, int index) {
    int res = -1;
    int j = 0;
    int start = index * (int)sizeof(unsigned int);
    int end = start + (int)sizeof(unsigned int); 
    for (j = start; j < end; j++) {
        if (!check_bit(arr, arr_size, j)) {
            res = j;
            break;
        }
    }

    return res;
}

unsigned int get_missing_array(unsigned int *input, unsigned int input_arr_size, int *err) {
    unsigned int arr[45] = { 0 };
    unsigned int i = 0;
    unsigned int n = 0;
    err = 0;
    for (i = 0; i < input_arr_size; i++) {
        set_bit(arr, 45, input[i]);
    }

    for (i = 0; i < 45; i++) {
        if (arr[i] != UINT_MAX) {
            break;
        }
    }

    if (i < UINT_MAX) {
        n = reveal_zero(arr, 45, i);
    }

    return n;
} 

int main()
{
    unsigned int input[10] = {0, 1, 1, 3, 4, 5, 6, 7, 8, 9};
    int err = 0;
    unsigned int missing = get_missing_array(input, 10, &err);
    printf("%d, %d\n", missing, err);

    return 0;
}