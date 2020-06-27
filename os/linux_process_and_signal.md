main tutorial: https://www.bogotobogo.com/Linux/linux_process_and_signals.php

# Process

## Process Table
Process table describes all the processes that are currently loaded. How to see: `ps`. See all processes: `ps aux`.

## Daemon Processes
A daemon a special-purpose process that is *long-lived* and *runs in background*.

## Managing daemons with systemd

Sources:

- https://www.youtube.com/watch?v=unIAGt5pB7A
- http://0pointer.de/blog/projects/resources.html

Example:

```bash
[Unit]
Description=a sample service

[Service]
Type=simple
ExecStart=/usr/lib/my_program.sh
MemoryLimit=1G
CPUShares=1000      # requested, in milli CPU
LimitCPU=2000       # limit, in milli CPU

[Install]
WantedBy=multi-user.target
```

Using systemd, if a program forks children and we stop with `systemctl stop my_service.service`, systemd also stops the children.

## Controlling resource usage with cgroup

One of the practical ways: Docker to use cgroup indirectly. See [Docker](docker_for_dummies.md).

Use systemd: see the above example. Each systemd's service is a cgroup. All processes that are started by that service use that cgroup.

## C Program: make a new process with system()

```c
int main()
{
    system("ps aux");
    printf("oi!");
}
```

A call to `system()` is not so flexible.

## C Program: make a new process with exec()
`exec` hands off execution of the running program to another. *The original program will no longer running after the new one is started*.
```c
int main()
{
    execlp("ps", "ps", 0);
    print("oi"); // this will never be called
}
```

## C Program: make a new process with fork and execv
```c
int main()
{
    pid_t pid = fork();
    int pid_child;
    int status;
    if (pid == 0)
    {
        printf("child\n");
        execv("ls");
    }
    else
    {
        printf("parent %d\n", pid);
    }
    printf("parent prints this line\n");
    pid_child = wait(&status); // it blocks the parent, wait for child process to finish
}
```

We can see the process tree (the parent to it's children by running `pstree -p -s $PID`. The parent includes `init`).

## Zombie Process

Read:

- https://stackoverflow.com/questions/16944886/how-to-kill-zombie-process
- https://askubuntu.com/questions/111422/how-to-find-zombie-process
- https://www.geeksforgeeks.org/zombie-and-orphan-processes-in-c/
- https://en.wikipedia.org/wiki/Child_process
- https://gist.github.com/leehambley/5589953

Zombie process happens when child has finished its execution, but the parent has not (because blocked) or does not call `wait()`.


As the child process has died, it does not consume much resource. However, it's still on the process table. How to see:

```bash
ps aux | grep Z
```

The number of PID is limited. If zombie process takes all of the available unique PID, the system cannot launch new process.

How to remove zombie process: the parent must call `wait()` or the parent process must be killed.

Example of how a zombie is created:

```c
int main() {
    pid_t pid = fork();
    if (pid > 0) {
        printf("parent");
        sleep(3600);
    }
    else {
        printf("I am a child. Finishing...");
    }
}
```

When a children exits, it sends a `SIGCHLD` signal to the parent. The parent can call wait inside the signal handler. Example of handler:

```c
void handler(int sig)
{
    pid_t pid;
    pid = wait(NULL);
    printf("Pid %d exited.\n", pid);
}

int main() {
    signal(SIGCHLD, handler);
}
```

## Orphan Process

Orphan process is a child process which is still running but the parent has died. When orphan process died, just ignore it since `init` process `wait` for it.

```c
int main() {
    pid_t pid = fork();
    if (pid > 0) {
        printf("parent, finishing...");
    }
    else {
        printf("I am a child");
        sleep(3600);
    }
}
```

## Limiting number of forks

sources:

- https://superuser.com/questions/559709/how-to-change-the-maximum-number-of-fork-process-by-user-in-linux
- https://unix.stackexchange.com/questions/118617/how-to-limit-the-number-of-process-that-a-user-can-create
- https://stackoverflow.com/questions/29605502/maximum-number-of-children-processes-on-linux

Unlimited number of forks can cause [*fork bomb*](https://en.wikipedia.org/wiki/Fork_bomb#:~:text=In%20computing%2C%20a%20fork%20bomb,system%20due%20to%20resource%20starvation.): a DoS attack that crashes apps due to resource starvation.

Limit to the current terminal session: `sudo ulimit -n THE_NUMBER`

Permanent: in `/etc/limits.conf`

# Signals

Signal is a notification sent from the kernel to a process, a process to another process, or a process to itself.

To stop a process, there are some signals that can be used. Reference: https://unix.stackexchange.com/questions/251195/difference-between-less-violent-kill-signal-hup-1-int-2-and-term-15

They are SIGKILL, SIGINT, SIGTERM, SIGQUIT, SIGHUP. SIGKILL never fails to kill a running process, it *cannot be ignored or handled*. The process killed by SIGKILL does not have chance to react or dodge. The other signal can be catch and the process can be written to do something upon receiving these signals. 

## SIGINT

`Ctrl + c` is one way to send this `kill -s SIGINT pid`. It says: "stop what this process is doing now and wait for further user input".

It's the weakest signal to kill a process.

## SIGTERM

It tells the application to exit cleanly. The application might take time to save its state, free resources such as temporary files, etc. SIGTERM might be ignored for a while.

It's the normal kill signal.

## SIGHUP

Hang up meaning: "end a telephone conversation by cutting the connection." (source: just google "hang up meaning")

SIGHUP is automatically sent to applications running in a terminal when the user disconnects from that terminal.

Example: run something foreground on terminal of a remote machine. We have disconnected to the network and thus so have the SSH. SIGHUP is sent.

Harshness level: like SIGTERM.

## SIGQUIT

Kill the process now and left a core dump. It is used when something is *seriously wrong*.

# Troubleshooting and debugging linux processes with strace

Source: https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/

`strace` captures and records all system calls made by a process and the signals received by the process.

For example, to see what system calls a program `df` calls, we can use `strace ls -h`
