Source: https://www.slashroot.in/linux-system-io-monitoring 


# How to monitor system I/O

## free

command: `free -mh`.

`free` is mainly used to check RAM usage. we can see the total used, buffer, and cache.

## /usr/bin/time -v program

Example: `/usr/bin/time -v code`

This will invoke the program and we can see many details including:
- Major page faults
- Minor page faults
- Page size
- Swaps
- File system inputs
- File system outputs

If we recently open a program, there is a chance that the data is cached by `buffer caching` to reduce the number of major page faults and increase minor page faults.

## vmstat

Sources: 

- https://medium.com/@damianmyerscough/vmstat-explained-83b3e87493b3
- https://access.redhat.com/solutions/1160343

**Wait on I/O** is a situation when there are a large number of applications waiting for their I/O operations to get completed.

When wait on i/o happens, the CPU becomes idle. Sometimes it is confusing to see the bottleneck when CPU is idle. This might be one of the problems.

How to use:
- `vmstat 2`: sample every 2 seconds
- `vmstat 2 4`: sample 4 times every 2 seconds

Sample output:
```
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0 377796 157908 164976 2116256    1    5    56    46   73  235  8 11 81  0  0
 0  0 377796 150344 164976 2124672    0    0     0     0 42460 7281  2  8 90  0  0
```

- `wa` under `cpu`: cpu wait on i/o. if it has high value, there is an i/o bottleneck
- `id` under `cpu`: cpu idle
- `bi` under `io`: blocks that are read into RAM from the disk. If `wa` and `bi` is high, there's i/o bottleneck
- if `swpd` > 0, swap is being used. if `so` > 0, it's even worse, there is a RAM bottleneck (happens when swapping: kernel selects memory segment that is less frequently used and swapped out to disk)

Here is a more detailed explanation:

**procs**

- `r`: number of processes in a running state, read from `/proc/[PID]/stat`
- `b`: number of processes in an uninterruptable sleep state (a process that does not handle signals right away), read from `/proc/[PID]/stat`

Example of uninterruptable sleep state process: device drivers when waiting for network/disk IO, it sleeps and accumulates received signals and reacts when the process resumes.

**memory**

- `swpd`: amount of swap memory used, the less the better, read from `/proc/[PID]/stat`
- `free`: free RAM
- `buff`: amount of memory used as buffers, read from `/proc/meminfo`
- `cache`: cache size used, read from `/proc/meminfo`

By the way, if we are running out of RAM + swap, OOM killer will save the day by killing process(es). It kills the process by badness score, which is rated by the process + children of the process (accumulated) takes the most RAM and the minimum number of process killed in order to free up memory to resolve the situation (kernel and root are less prioritized). Read more: https://docs.memset.com/other/linux-s-oom-process-killer#Linux'sOOMProcessKiller-HowdoesitselectaProcesstoKill?

**swap**

- `si`: amount of memory swapped in from disk per second
- `so`: amount of memory swapped out to disk per second

**IO**

- `bi`: number of blocks read from disk per second
- `bo`: number of blocks written disk per second

**system**

- `in`: number of interrupts per second, read from `/proc/stat` and `/proc/interrupts`
- `cs`: number of context switches per second, read from `/proc/stat`

**cpu**

All read from `/proc/stat`.

- `us`: time spent running non-kernel code, high when a user-space process messes up (like running a lame app that has `while(1)` without sleep)
- `sy`: time spent running kernel code, high when a kernal-space process messes up
- `id`: idle time
- `wa`: waiting I/O time
- `st`: time stolen from a virtual machine

## sar
`sar` can also be used to see wait on i/o.

In Fedora, install `sar` by `dnf install sysstat`.

Example:
- `sar 2`: sample every 2 seconds
- `sar 1 7`: sample 7 times every 1 second

Sample output:
```
Linux 4.20.10-200.fc29.x86_64 (localhost.localdomain) 	02/28/2019 	_x86_64_	(4 CPU)

06:42:20 PM     CPU     %user     %nice   %system   %iowait    %steal     %idle
06:42:21 PM     all      4.24      0.00      8.98      0.00      0.00     86.78
06:42:22 PM     all      0.50      0.00      6.78      0.00      0.00     92.71
```

# How to identify which process is taking heavy IO in linux

## top

Open `top` and press `F`. Select what we want to display, and sort. After pressing `F`, there is a guide at the top.

## iostat

`iostat` provides some detailed information about the io usage.

Example output of `iostat`:
```
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           7.74    0.04   10.82    0.26    0.00   81.14

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda              12.56       145.49       122.57    5569832    4692126
dm-0              6.23       108.17        28.44    4140873    1088664
dm-1              4.44         2.06        15.75      78912     602884
dm-2             10.49        34.87        79.65    1335009    3049116
loop0             0.00         0.03         0.00       1136          0
loop1             0.00         0.02         0.00        661          0
```

Example output of `iostat -xk`:
```
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           7.74    0.04   10.82    0.26    0.00   81.15

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
sda              7.10    5.46    145.46    122.54     0.49     8.12   6.45  59.80    2.09   23.67   0.14    20.48    22.46   1.32   1.66
dm-0             4.64    1.60    108.14     28.43     0.00     0.00   0.00   0.00    2.03   23.73   0.05    23.33    17.80   0.61   0.38
dm-1             0.50    3.94      2.06     15.74     0.00     0.00   0.00   0.00    1.70   17.37   0.07     4.10     4.00   0.10   0.05
dm-2             2.44    8.04     34.86     79.63     0.00     0.00   0.00   0.00    2.62   20.69   0.17    14.27     9.90   1.23   1.29
loop0            0.00    0.00      0.03      0.00     0.00     0.00   0.00   0.00    0.78    0.00   0.00    10.23     0.00   0.60   0.00
loop1            0.00    0.00      0.02      0.00     0.00     0.00   0.00   0.00    0.60    0.00   0.00    10.17     0.00   0.48   0.00
```

To get i/o performance of the device:
```
read performace of a device = (r/s value) / (rkB/s value)
write performace of a device = (w/s value) / (wkB/s value)
```
