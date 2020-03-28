#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <sys/time.h>

long get_micro_time(){
	struct timeval currentTime;
	gettimeofday(&currentTime, NULL);
	return currentTime.tv_sec * (int)1e6 + currentTime.tv_usec;
}

int compare(const void *c1, const void *c2)
{
    char *a = *(char *)c1, *b = *(char *)c2;
    if (a > b)
    {
        return 1;
    }
    else if (a < b)
    {
        return -1;
    }
    return 0;
}

int cmp_func(const void *s1, const void *s2) {
    const char *a = *(const char **)s1, *b = *(const char **)s2;
    char *l = malloc(strlen(a));
    char *r = malloc(strlen(b));
    strcpy(l, a);
    strcpy(r, b);
    qsort(l, strlen(l), sizeof(char), compare);
    qsort(r, strlen(r), sizeof(char), compare);
    int res = strcasecmp(l, r);
    free(r);
    free(l);
    return res;
}

int main()
{
    const char *arr_str[] = {
        "ot", "abc", "are", "bca", "era", "acb", "to" };

    int i = 0;
    printf("%d\n\n", strlen(arr_str[0]));
    for (i = 0; i < (int)sizeof(arr_str)/sizeof(*arr_str); i++) {
        printf("%s ", arr_str[i]);
    }
    printf("\n");

    long t0 = get_micro_time();
    qsort(arr_str, sizeof(arr_str)/sizeof(*arr_str), sizeof(*arr_str), cmp_func);
    long t1 = get_micro_time();
    for (i = 0; i < (int)sizeof(arr_str)/sizeof(*arr_str); i++) {
        printf("%s ", arr_str[i]);
    }
    printf("\ntakes: %d\n", t1-t0);

    return 0;
}