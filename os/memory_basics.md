Anatomy of a program in memory: https://manybutfinite.com/post/anatomy-of-a-program-in-memory/
what to know about cache: https://manybutfinite.com/post/intel-cpu-caches/

The anatomy of a memory:

![anatomy](http://static.duartes.org/img/blogPosts/linuxFlexibleAddressSpaceLayout.png)
Image source: https://manybutfinite.com/post/anatomy-of-a-program-in-memory/

Keys to grasp:

1. Virtual memory is mapped to the physical memory by a data structure called **page table**, the process is called **paging**.
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
