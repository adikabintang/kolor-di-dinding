#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

void bv_set_bit(uint8_t *bit_vector, int bit_vector_size, short val)
{
    int idx = (int)val / bit_vector_size;
    int bit_position = val % bit_vector_size;
    uint8_t bit_repr = 1 << bit_position;
    bit_vector[idx] = bit_vector[idx] | bit_repr;
}

bool bv_check_bit(uint8_t *bit_vector, int bit_vector_size, short val)
{
    int idx = (int)val / bit_vector_size;
    int bit_position = val % bit_vector_size;
    uint8_t bit_repr = 1 << bit_position;
    return (bit_vector[idx] & bit_repr);
}

int main()
{
    uint8_t bv[4000] = { 0 };
    short input[10] = {1, 1, 5, 4, 32000, 8, 1, 32000, 7, 3};
    int input_size = (int)sizeof(input) / sizeof(short);
    int i = 0;
    for (i = 0; i < input_size; i++) {
        if (bv_check_bit(bv, 4000, input[i])) {
            printf("%d, " , input[i]);
        } else {
            bv_set_bit(bv, 4000, input[i]);
        }
    }

    return 0;
}