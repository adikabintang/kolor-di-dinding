#include <stdio.h>
#include <limits.h>

int insert(int m, int n, int i, int j)
{
    n = n & (INT_MAX << j);
    m = m << i;
    return n | m;
}

int main()
{
    int n = 0b10000000000;
    int m = 0b10011;
    int i = 2;
    int j = 6;

    printf("%x\n", (0b111 << 1));
    printf("%x\n", insert(m, n, i, j));
    return 0;
}