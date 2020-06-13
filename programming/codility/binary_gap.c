#include <stdbool.h>
int solution(int N) {
    // write your code in C99 (gcc 6.2.0)
    int mask = 1, ctr = 0, max = 0;
    bool start = false;
    size_t length = sizeof(int) * 8, i = 0;
    
    while (i < length) {
        if ((mask & N)) {
            start = true;
            if (ctr > max) {
                max = ctr;
            }
            ctr = 0;
        }
        else {
            if (start)
                ctr++;
        }
        mask <<= 1;
        i++;
    }
    return max;
}
