// URLify
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void urlify(char *input, unsigned int input_len)
{
    unsigned int counter = 0;
    int i = 0;
    for (i = 0; i < input_len; i++)
    {
        if (input[i] == ' ') {
            counter++;
        }
    }
    
    for (i = input_len-1; i >= 0; i--) {
        int index = i + counter * 2;
        if (counter == 0) {
            break;
        }
        
        if (input[i] != ' ') {
            input[index] = input[i];
        } 
        else {
            input[index] = '0';
            input[index - 1] = '2';
            input[index - 2] = '%';
            counter--;    
        }
    }
}

int main()
{
    char *s = "mr john smith    ";
    char in[18];
    int i = 0;

    for (i = 0; i < strlen(s); i++) {
        in[i] = s[i];
    }
    in[17] = '\0';
    printf("%s\n", in);
    urlify(in, 13);
    printf("%s\n", in);
    return 0;
}
