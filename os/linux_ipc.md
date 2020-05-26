Sources:

- https://tldp.org/LDP/lpg/node7.html
- https://www.tldp.org/LDP/tlk/ipc/ipc.html
- https://opensource.com/sites/default/files/gated-content/inter-process_communication_in_linux.pdf
- http://www.qnx.com/developers/docs/qnx_4.25_docs/tcpip50/prog_guide/sock_ipc_tut.html

Used for communicating between multiple processes.

# Pipe: half-duplex

1. Pipe is half-duplex.
   1. A pipe `[in]=====[out]` is written from the left ([in]) and read from the right ([out])
2. The function `pipe(int fd*)` takes an array as the input with size 2:
   1. First element `fd[0]` is for reading
   2. Second element `fd[1]` is for writing
3. The process that make use of one end of the pipe **must** close the other end. For example, if a parent is using `[out]` or `fd[0]` for reading from a child process, it must close `fd[1]`, and vice versa. If it fails to do so, no `EOF` at the end of the data sent.
4. Pipe is actually a file. When forking a process, parent and child shares the file descriptor. All data pass through the pipe passes through the kernel.

Example: a parent is forking a process. The child does something

```C
pid_t pid = fork();
const char *i_am_child = "i am the child";
size_t n_bytes;
char read_buff[100];

if (pid == 0) { // child process
    // see note 3:
    // child is writing, it uses fd[1] to write, and it must close fd[0]
    close(fd[0]);

    // send this to the pipe
    write(fd[1], i_am_child, strlen(i_am_child) + 1); // + 1 for \0
    // close after write
    close(fd[1]);
    exit(0)
}
else {          // parent process
    // see note 3:
    // parent is reading, it uses fd[0] to read, and it must close fd[1]
    close(fd[1]);

    // read from the pipe
    n_bytes = read(fd[0], read_buff, sizeof(readbuff));
    // close after read
    close(fd[0]);
    printf("received string: %s\n", read_buff);
}
```

# Shared memory, assisted by a binary semaphore

There is a shared memory segment that multiple processes share, they can access this segment.

We need a *counting semaphore* to avoid race condition when accessing the segment.

Example:

- Process A can read only if the semaphore value is 1. After it reads, it sets the semaphore to 0.
- Prcess B can write only if the semaphore value is 0. After it writes, it sets the semaphore to 1.