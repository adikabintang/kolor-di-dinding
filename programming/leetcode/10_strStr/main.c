/*
Runtime: 0 ms, faster than 100.00% of C online submissions
Memory Usage: 7.1 MB, less than 81.25% of C online submissions 
*/
#include <stdio.h>
#include <string.h>
#include <stdint.h>

int strStr(const char * haystack, const char * needle)
{
    char *r = strstr(haystack, needle);
    if (r == NULL)
        return -1;
    
    if ((intptr_t)r == 0)
        return 0;
    
    return (intptr_t)r - (intptr_t)haystack;
}

int main()
{
    const char *haystack = "aaaaa";
    const char *needle = "a";
    printf("resulttt: %d\n", strStr(haystack, needle));

    const char *h = "hello";
    const char *n = "ll";
    printf("resulttt: %d\n", strStr(h, n));

    const char *has = "hello";
    const char *nd = "";
    printf("resulttt: %d\n", strStr(has, nd));

    const char *hs = "hello";
    const char *ndo = "as";
    printf("resulttt: %d\n", strStr(hs, ndo));
    return 0;
}