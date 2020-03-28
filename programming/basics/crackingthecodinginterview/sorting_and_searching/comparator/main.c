#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>

/*
strcasecmp(s1, s2):
we can think of strcasecmp returns s1-s2.
example:
"aa"-"ab" = -1
"ab"-"aa" = 1
"aa"-"aa" = 0

when we use comparator(a, b) for sorting,
ascending (behaves like strcasecmp):
a < b -> return -1
a == b -> return 0
a > b -> return 1

descending:
a < b -> return 1
a == b -> return 0
a > b -> return -1 
*/

// this function is needed because qsort requires this type of arguments
int cmp_func(const void *s1, const void *s2)
{
    const char *l = *(const char **)s1;
    const char *r = *(const char **)s2;

    return strcasecmp(l, r);
}

int main()
{
    char *s1 = "aa";
    char *s2 = "ab";
    printf("%d\n", strcasecmp(s1, s2));

    const char *arr_str[] = {
        "Here", "are", "some", "sample", "strings", "to", "be", "sorted" };
    
    int i = 0;
    for (i = 0; i < (int)sizeof(arr_str)/sizeof(*arr_str); i++) {
        printf("%s ", arr_str[i]);
    }
    printf("\n");

    qsort(arr_str, sizeof(arr_str)/sizeof(*arr_str), sizeof(*arr_str), cmp_func);
    for (i = 0; i < (int)sizeof(arr_str)/sizeof(*arr_str); i++) {
        printf("%s ", arr_str[i]);
    }
    return 0;
}
