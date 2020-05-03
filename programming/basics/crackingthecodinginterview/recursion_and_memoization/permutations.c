#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_helper(int **arr, int row_size, int col_size)
{
    int i = 0;
    for (i = 0; i < row_size; i++)
    {
        int j = 0;
        for (j = 0; j < col_size; j++)
        {
            printf("%d, ", arr[i][j]);
        }
        printf("\n");
    }
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void print_arr(int *arr, int size)
{
    int i = 0;
    for (i = 0; i < size; i++)
    {
        printf("%d, ", arr[i]);
    }
    printf("\n");
}

void permute_helper(int *arr, int left, int right, int **holder, int *holder_i)
{
    if (left == right) 
    {
        holder[*holder_i] = malloc((right + 1) * sizeof(int));
        memcpy(holder[*holder_i], arr, sizeof(holder[*holder_i]) + 1);
        *holder_i = *holder_i + 1;
    }
    else
    {
        int i = 0;
        for (i = left; i <= right; i++)
        {
            swap(&arr[i], &arr[left]);
            permute_helper(arr, left+1, right, holder, holder_i);
            swap(&arr[i], &arr[left]);
        }
    }
}

int **permute(int *arr, int size, int *returned_size)
{
    int n_permut = 1, i = 0;
    for (i = 0; i < size; i++)
    {
        n_permut = n_permut * (size - i);
    }
    int **result = malloc((n_permut + 1) * sizeof(int));
    *returned_size = n_permut;
    int result_i = 0;
    permute_helper(arr, 0, size - 1, result, &result_i);
    return result;
}

int main()
{
    int arr[3] = {1, 2, 3};
    int **res;
    int ret_size = 0;
    res = permute(arr, 3, &ret_size);
    printf("retsize: %d\n", ret_size);
    print_helper(res, ret_size, 3);
    return 0;
}