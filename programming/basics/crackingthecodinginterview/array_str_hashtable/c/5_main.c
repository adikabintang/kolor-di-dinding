#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

bool is_one_away(const char *s1, const char *s2)
{
    int s1_len = strlen(s1);
    int s2_len = strlen(s2);
    int min_len = (s1_len > s2_len ? s1_len : s2_len);
    int diff_len = abs(s1_len - s2_len);
    int m = 0, n = 0, i = 0, counter = 0;

    if (diff_len > 1) {
        return false;
    }

    for (i = 0; i < min_len; i++) {
        if (s1[m] != s2[n]) {
            counter++;
            if (counter > 1) {
                return false;
            }

            if (s1_len > s2_len) {
                m++;
            }
            else if (s2_len > s1_len) {
                n++;
            }
        }
        m++;
        n++;
    }

    return counter <= 1;
}

int main()
{
    printf("%d\n", is_one_away("pale", "ple"));
    printf("%d\n", is_one_away("pales", "pale"));
    printf("%d\n", is_one_away("pale", "bale"));
    printf("%d\n", is_one_away("pale", "bake"));
    printf("%d\n", is_one_away("able", "bale"));
    return 0;
}