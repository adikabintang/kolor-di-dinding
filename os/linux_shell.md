What happens when we run a command in the shell?

Sources:

- https://medium.com/meatandmachines/what-really-happens-when-you-type-ls-l-in-the-shell-a8914950fd73
- https://brennan.io/2015/01/16/write-a-shell-in-c/
- https://github.com/adikabintang/emposh

1. The shell (`/bin/sh`) reads the STDIN. For example, we type `ls -l`, the shell reads the string and tokenize the string.

How to read STDIN: https://github.com/adikabintang/emposh/blob/master/src/util.c#L10

```C
char *line;
size_t buffer_size = 0;
getline(&line, &buffer_size, stdin);
```

Tokenizing: user `strtok()`: https://github.com/adikabintang/kolor-di-dinding/blob/master/programming/swiss_army_knife_and_cheatsheet.md#c-8


2. Check if the command is a built-in. A built-in is the command that is built within the shell itself, not provided by the OS. For example, `help`, `cd`. If it's built-in, run the built-in function. Otherwise, fork.
3. Fork example: https://github.com/adikabintang/emposh/blob/master/src/util.c#L45

```C
pid_t pid, wait_pid;
int status;

pid = fork();
if (pid == 0) {
    // this is the child process
    if (execvp("ls", "-l") == -1) {
        perror("cannot execute");
    }
    exit(EXIT_FAILURE);
}
else if (pid < 0) {
    perror("error forking");
}
else {
    // this is the parent
    do {
        wait_pid = waitpid(pid, &status, WUNTRACED);
    } while (!WIFEXITED(status) && !WIFSIGNALED(status));
}
```

The `execvp()` replaces defining parts of the current memory stack with the stuffs loaded from the "ls -l" executable file (look at the example above).
