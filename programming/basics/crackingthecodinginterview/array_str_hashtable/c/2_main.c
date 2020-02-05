#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool is_permutation(const char *s1, const char *s2)
{
    if (strlen(s1) != strlen(s2) || s1 == NULL && s2 == NULL) {
        return false;
    }

    // assuming string consists of ASCII
    char all[256] = { 0 };
    int i = 0;

    for (i = 0; i < strlen(s1); i++) {
        int index = (int)s1[i];
        all[index] += 1;
    }

    for (i = 0; i < strlen(s2); i++) {
        int index = (int)s2[i];
        all[index] -= 1;
        if (all[index] < 0) {
            return false;
        }
    }

    return true;
}

int main()
{
    printf("%d\n", is_permutation("123", "312"));
    printf("%d\n", is_permutation("1233", "312"));
    printf("%d\n", is_permutation("123", "3122"));
    printf("%d\n", is_permutation("123", "322"));
    printf("%d\n", is_permutation("", ""));
    return 0;
}