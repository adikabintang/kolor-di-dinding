/**
 * http://www.mathcs.emory.edu/~cheung/Courses/255/Syllabus/1-C-intro/bit-array.html
 * 
 * Actually this is neither sorting nor searching. But this is useful when
 * we want to implement set-like data structure.
 * With bit array, if we want to have an array to store if ints exist or not,
 * by providing a 10-size int array, we can have 32 * 10 numbers to store.
 * 
 * One thing to note is with bit vector, we need to know the range of numbers we 
 * want to store. For example, if the numbers are 0-3200, instead of having 
 * int arr[3200], the size is 3200/32 (32 is the int size in bit): int arr[100]
 */

#include <stdio.h>
#include <stdbool.h>

#define ARR_SIZE 10

void set_bit(int *arr, int value) {
    int index = (int)value / 32; // (sizeof(int) * 8)
    int bit_position = value % 32;
    int bit_repr = 1;
    bit_repr = bit_repr << bit_position;
    arr[index] = arr[index] | bit_repr;
}

bool check_bit(int *arr, int value) {
    int index = (int)value / 32;
    int bit_position = value % 32;
    int bit_repr = 1;
    bit_repr = bit_repr << bit_position;
    return (arr[index] & bit_repr);
}

void clear_bit(int *arr, int value) {
    int index = (int)value / 32;
    int bit_position = value % 32;
    int bit_repr = 1;
    bit_repr = ~(bit_repr << bit_position);
    arr[index] = arr[index] & bit_repr;
}

int main()
{
    int arr[ARR_SIZE]; // 32 (size of int) * ARR_SIZE number to store
    int i = 0;
    for (i = 0; i < 4; i++) {
        set_bit(arr, i);
    }

    for (i = 0; i < 8; i++) {
        printf("%d: %d\n", i, check_bit(arr, ARR_SIZE, i));
    }

    return 0;
}