// https://www.hackerrank.com/challenges/alternating-characters/
// Complete the alternatingCharacters function below.
int alternatingCharacters(char* s) {
    int ctr = 0, i = 0, len = 0, j = 0;
    len = strlen(s);
    while (i < len) {
        j = i + 1;
        while (j < len && s[j] == s[i]) {
            ctr++;
            j++;
        }
        i = j;
    }
    return ctr;
}
