/*
Runtime: 0 ms, faster than 100.00% of C online submissions 
Memory Usage: 7 MB, less than 66.67% of C online submissions
*/
#include <stdio.h>
#include <string.h>

int lengthOfLastWord(char * s) {
    int result = 0;
    char *splitted = strtok(s, " ");
    while (splitted != NULL) {
        result = strlen(splitted);
        splitted = strtok(NULL, " ");
    }
    
    return result;
}

int main()
{
    char str[] = "hello world";
    printf("%d\n", lengthOfLastWord(str));
    char s[] = "helloworld";
    printf("%d\n", lengthOfLastWord(s));
    char st[] = "";
    printf("%d\n", lengthOfLastWord(st));
    // printf("%d\n", lengthOfLastWord("helloworld"));
    // printf("%d\n", lengthOfLastWord(""));
    return 0;
}