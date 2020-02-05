#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool is_unique(const char *str)
{
    if (str == NULL) {
        return true;
    }

    unsigned int str_len = strlen(str);
    bool result = true;
    // assume the string consists of 256 ASCII chars
    char all[256] = { 0 };
    int i = 0;

    // convert each char to int, as index for the array all
    for (i = 0; i < str_len; i++)
    {
        int index = (int)str[i];
        if (all[index] == 0) {
            all[index] = 1;
        }
        else {
            result = false;
            break;
        }
    }

    return result;
}

int main()
{
    const char *s1 = "qwer";
    const char *s2 = "";
    const char *s3 = NULL;
    const char *s4 = "asdmaia=/la;";
    printf("%d\n", is_unique(s1));
    printf("%d\n", is_unique(s2));
    printf("%d\n", is_unique(s3));
    printf("%d\n", is_unique(s4));

    return 0;
}
