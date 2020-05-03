/*
learned from here: https://www.geeksforgeeks.org/c-program-demonstrate-fork-and-pipe/
The code is taken from geeksforgeeks, with some modification for learning purpose
notes on pipe: https://www.tldp.org/LDP/lpg/node11.html

Creates 2 processes: P1 and P2
P1 takes string, passes it to P2
P2 concatenates the received string
P2 sends the string back to P1
P1 prints it
*/
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <string.h>
#include <sys/wait.h>

int main()
{
    // 2 pipes:
    // 1st pipe: send input print from parent process
    // 2nd pipe: send concatenated string from child process
    
    int fd1[2]; // store two ends of first pipe: fd[0] is for reading, fd[1] is for writing
    int fd2[2]; // store two ends of second pipe
    /*
    notes on reading and writing to pipe:
    parents sends data to child:
    - parent closes fd[0]
    - child closes fd[1]
    - parent writes fd[1]
    - child reads fd[0]
    and so does the child to parent
    the point is, if a process wants to write (which means to fd[1]), close fd[0] beforehand.
    if a process wants to read (which means reading from fd[0]), close fd[1] beforehand.
    */

    char fixed_str[] = "a fixed string";
    char input_str[100];
    pid_t p;

    if (pipe(fd1) == -1 || pipe(fd2) == -1)
    {
        fprintf(stderr, "Pipe failed");
        return 1;
    }

    scanf("%s", input_str);
    p = fork();

    if (p < 0)
    {
        fprintf(stderr, "Fork failed");
        return 1;
    }
    else if (p > 0) // parent process
    {
        char concat_str[100];
        
        // close reading end of first pipe
        close(fd1[0]); 

        // write input string and close writing end of first pipe
        write(fd1[1], input_str, strlen(input_str) + 1);
        close(fd1[1]);

        // wait for child to send a string
        wait(NULL);

        // wait for child to send a string
        close(fd2[1]);

        // read string from child, print, close reading end
        read(fd2[0], concat_str, sizeof(concat_str)/sizeof(char));
        printf("Concatenated string: %s\n", concat_str);
        close(fd2[0]);
    }
    else // child process
    {
        char concat_str[100];
        
        // close writing end of first pipe
        close(fd1[1]);
        read(fd1[0], concat_str, sizeof(concat_str)/sizeof(char));
        
        // concatenate a fixed string with it
        int k = strlen(concat_str);
        int i;
        for (i = 0; i < strlen(fixed_str); i++) {
            concat_str[k++] = fixed_str[i];
        }
        concat_str[k] = '\0';

        // close both reading ends
        close(fd1[0]);
        close(fd2[0]);

        // write concatenated string and close writing end
        write(fd2[1], concat_str, strlen(concat_str)+1);
        close(fd2[1]);

        exit(0);
    }

    return 0;
}