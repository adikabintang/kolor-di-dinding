Anatomy of a program in memory: https://manybutfinite.com/post/anatomy-of-a-program-in-memory/
what to know about cache: https://manybutfinite.com/post/intel-cpu-caches/

The anatomy of a memory:

![anatomy](http://static.duartes.org/img/blogPosts/linuxFlexibleAddressSpaceLayout.png)
Image source: https://manybutfinite.com/post/anatomy-of-a-program-in-memory/

Keys to grasp:

1. Virtual memory is mapped to the physical memory by a data structure called **page table**, the process is called **paging**. A Memory Management Unit (MMU) performs a translation of virtual memory addresses to physical addresses [[wiki](https://en.wikipedia.org/wiki/Memory_management_unit)].
2. See the white gap in the picture above, the "random" spaces. It is called **address space layout randomization**, a security technique to prevent an attacker from easily jumping to a certain memory area [[wiki](https://en.wikipedia.org/wiki/Address_space_layout_randomization)].
3. Stack:
   1. stores local variable and parameter of a function
   2. calling a function pushes a new **stack frame** to the stack. When the function returns, the frame is popped, called **stack unwinding**.
   3. Each thread has its own stack
   4. Stack overflow (when it reaches the full size of the stack) causes **segmentation fault**.
4. Heap:
   1. Stores dynamically allocated var. The language runtime requests for it to the kernel. In C, the interface for doing it is `malloc()`.
   2. Heap can be fragmented, which we don't want.

Continue to [linux_io_notes.md](linux_io_notes.md).

# Memory architecture

## Non-uniform memory access (NUMA)

In NUMA, memory access time depends on the memory location relative to the processor [[wiki](https://en.wikipedia.org/wiki/Non-uniform_memory_access)].

## Symmetric Multiprocessing (SMP)

In SMP, two or more cores are connected to a single shared memory [[wiki](https://en.wikipedia.org/wiki/Symmetric_multiprocessing)]

![smp_vs_numa](http://outofsync.net/wiki/images/d/d4/Smp_numa.png)

Image source: http://outofsync.net/wiki/index.php?title=Monitoring_linux_system_performance

# More about virtual memory

Sources:

- https://elinux.org/images/b/b0/Introduction_to_Memory_Management_in_Linux.pdf
- slides: https://www.youtube.com/watch?v=7aONIVSXiJ8

virtual memory: **mapping** virtual address to physical RAM; provides isolation, single address space

two address spaces:
1. physical addresses: used by hardware. example: DMA
2. virtual addresses: used by software. example: load/store instructions

mapping is done by hardware: MMU
- it sits between CPU and memory (part of CPU hardware, integrated).
- what it does:
  - maps accesses using virtual addresses to system RAM
  - maps accesses using virtual addresses to memory-mapped peripheral hardware
  - handle permission
  - generates page fault on an invalid address
- how MMU works:

![mmu_ops](https://upload.wikimedia.org/wikipedia/commons/d/dc/MMU_principle_updated.png)

Source: https://en.wikipedia.org/wiki/Memory_management_unit

Mapping/translation process:

![vmem_trans_process](https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Page_table_actions.svg/1280px-Page_table_actions.svg.png)

source: https://en.wikipedia.org/wiki/Page_table

![vmem_system](../images/virt_mem_system.png)

Source: https://www.youtube.com/watch?v=7aONIVSXiJ8

- MMU works with memory in a *unit* called **page**, which is usually 4Kb. The real frame that MMU is working on is called **page frame**.
- how shared memory works:
  - simply map the same **physical** frame into 2 different processes. The virtual addresses need not be the same. Syscall to request a specific virtual address to map the shared memory region: `mmap()`.
- Linux uses lazy (on-demand) allocation of physical pages. it defers the allocation. for the memory that gets allocated but does not get used, allocation never has to happen. it's a performance optimization. https://landley.net/writing/memory-faq.txt#:~:text=The%20Linux%20kernel%20uses%20lazy,with%20no%20physical%20pages%20attached.

how to make swap:

1. swap partition: a disk parition that is only for swap. 
2. swap file: make an empty file with `dd`, then make that file to a swap using `mkswap`

swap size: 

1. PC: twice the RAM size
2. server: half of RAM size

tweak swap:

swappiness
https://askubuntu.com/questions/157793/why-is-swap-being-used-even-though-i-have-plenty-of-free-ram

https://help.ubuntu.com/community/SwapFaq/#What_is_swappiness_and_how_do_I_change_it.3F

> What is swappiness and how do I change it?
The swappiness parameter controls the tendency of the kernel to move processes out of physical memory and onto the swap disk. Because disks are much slower than RAM, this can lead to slower response times for system and applications if processes are too aggressively moved out of memory.
>
> swappiness can have a value of between 0 and 100
>
> swappiness=0 tells the kernel to avoid swapping processes out of physical memory for as long as possible. For Kernel version 3.5 and newer it disables swapiness.
>
> swappiness=100 tells the kernel to aggressively swap processes out of physical memory and move them to swap cache

how to see swappiness: `cat /proc/sys/vm/swappiness`

how to set swappiness: `sudo sysctl vm.swappiness=my_val`

or put `vm.swappiness=my_val` in `/etc/sysctl.conf`.

# OOM Killer

sources:

- https://lwn.net/Articles/317814/
- https://www.oracle.com/technical-resources/articles/it-infrastructure/dev-oom-killer.html
- https://lwn.net/Articles/761118/
- https://www.kernel.org/doc/gorman/html/understand/understand016.html

1. Process are rated by *badness score*. how to see the score: `/proc/<pid>/oom_score`
2. How badness score is calculated:
   1. original memory size of the process
   2. CPU time (utime + stime)
   3. run time (now - start time)
   4. oom_adj value -> what's this?
      1. a value in `/proc/<pid>/oom_adj` **to control the behavior of OOM killer for a process**. The value is from -17 to +15. The higher it is, the higher the possibility to get killed. To avoid getting killed: set to -17.
   5. If a process forks a child, half of the child's process memory size is added to the parent's badness score. That's why a server that is forking for a new connection (like the older version of Apache web server) is very likely to get killed by OOM killer (it forks many child and the run time is high).
   6. "**sum up the amount of memory used by a process, then scale it by the process's oom_score_adj value**" [lwn](https://lwn.net/Articles/761118/)

`badness_for_task = total_vm_for_task / (sqrt(cpu_time_in_seconds) * sqrt(sqrt(cpu_time_in_minutes)))`

So, how to easily control the memory use of userspace apps? Use `cgroup` or `Docker` (by Docker I mean it will utilize cgroup for this purpose too)
