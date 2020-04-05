/**
 * http://www.mathcs.emory.edu/~cheung/Courses/255/Syllabus/1-C-intro/bit-array.html
 * 
 * Actually this is neither sorting nor searching. But this is useful when
 * we want to implement set-like data structure.
 * With bit array, if we want to have an array to store if ints exist or not,
 * by providing a 10-size int array, we can have 32 * 10 numbers to store.
 */

#include <stdio.h>
#include <stdbool.h>

#define ARR_SIZE 10

void set_bit(int *arr, int arr_size, int value) {
    int index = (int)value / arr_size;
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

void clear_bit(int *arr, int arr_size, int value) {
    int index = (int)value / arr_size;
    int bit_position = value % arr_size;
    int bit_repr = 1;
    bit_repr = ~(bit_repr << bit_position);
    arr[index] = arr[index] & bit_repr;
}

int main()
{
    int arr[ARR_SIZE]; // 32 (size of int) * ARR_SIZE number to store
    int i = 0;
    for (i = 0; i < 4; i++) {
        set_bit(arr, ARR_SIZE, i);
    }

    for (i = 0; i < 8; i++) {
        printf("%d: %d\n", i, check_bit(arr, ARR_SIZE, i));
    }

    return 0;
}