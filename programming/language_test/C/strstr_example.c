/**
 * strstr()
 * Returns a pointer to the first occurrence of str2 in str1, or a null pointer 
 * if str2 is not part of str1.
 */ 
#include <stdio.h>
#include <string.h>

int main()
{
    const char *name = "derek trucks";
    const char *find = "tr";

    char *ret = strstr(name, find);
    printf("ret: %s\n", ret); // ret: trucks

    return 0;
}