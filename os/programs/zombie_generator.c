#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>

void handler(int sig)
{
  pid_t pid;

  pid = wait(NULL);

  printf("Pid %d exited.\n", pid);
}

int main() {
    pid_t pid;
    //signal(SIGCHLD, handler);

    pid = fork();
    if (pid > 0) {
        // parent
        //wait(NULL);
        sleep(60);
    }
    else {
        printf("child\n");
        printf("done");
    }
    return 0;
}
