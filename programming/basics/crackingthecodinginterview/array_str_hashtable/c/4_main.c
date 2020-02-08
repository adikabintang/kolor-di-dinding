// palindrome permutation
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

bool is_palindrome_permutation(const char *str)
{
    int s_len = strlen(str);
    int all_chars[256] = { 0 };

    if (s_len <= 1) {
        return true;
    }

    int char_count = 0;
    int str_len_wo_space = 0;
    int i = 0;
    for (i = 0; i < s_len; i++) {
        if (str[i] != ' ') {
            int index = (int)tolower(str[i]);
            if (all_chars[index] == 0) {
                char_count += 1;
            }
            all_chars[index] += 1;
            str_len_wo_space += 1;
        }
    }

    if (char_count == str_len_wo_space) {
        return false;
    }

    int odd_count = 0;
    for (i = 0; i < 256; i++) {
        if (all_chars[i] % 2 != 0) {
            odd_count += 1;
            if (odd_count > 1) {
                return false;
            }
        }
    }

    return true;
}

int main()
{
    printf("%d\n", is_palindrome_permutation("tact coa"));
    printf("%d\n", is_palindrome_permutation("Tact Coa"));
    printf("%d\n", is_palindrome_permutation("tacccoa"));
    printf("%d\n", is_palindrome_permutation("a"));
    printf("%d\n", is_palindrome_permutation("aa"));
    printf("%d\n", is_palindrome_permutation("oa"));
    printf("%d\n", is_palindrome_permutation("aaa"));
    printf("%d\n", is_palindrome_permutation(""));
    return 0;
}
