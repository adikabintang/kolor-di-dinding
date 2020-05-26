# The Linux Boot Process

Sources: 

- https://www.thegeekstuff.com/2011/02/linux-boot-process/
- https://wiki.debian.org/BootProcess
- https://en.wikipedia.org/wiki/Initial_ramdisk
- https://en.wikipedia.org/wiki/Linux_startup_process
- https://stackoverflow.com/questions/44274648/which-one-is-pid1-sbin-init-or-systemd
- https://www.tecmint.com/systemd-replaces-init-in-linux/
- https://en.wikipedia.org/wiki/Master_boot_record

# Some terms

1. BIOS: a *firmware* that initializes hardware during the booting
2. MBR: Master Boot Record - a special type of boot sector at the beginning of a disk partition

# Very high level overview

1. BIOS searches, loads, and executes Master Boot Record (MBR) bootloader. The boot loader can be in hard drive or USB stick. It also does some integrity check.
2. MBR contains a program named GRUB boot loader. It loads the GRUB boot loader and executes it.
3. GRUB (Grand Unified Bootloader) loads and executes kernel and initrd images.
4. Kernel mounts the root file system
5. Kernel executes `kernel_init()`, which mount the root file system `/` (on RAM or disk, depends on the configuration).
6. If a temporary `/` file system is needed on RAM, initrd (initial RAM disk) is used by the kernel as the temporary root file system until the kernel is booted and the real root filesystem is mounted.
7. executes /sbin/init (which has PID 1). In Fedora, /sbin/init is a symlink to systemd. It identifies the default init level and uses that to load all appropriate programs.
8.  `Runlevel` programs: programs that are run when the system is booting up (and also some when shutting down). The runlevel programs are in `/etc/rc.d/rc*.d/`.

# More complete of step 1 - 3 above

Source: https://medium.com/@cloudchef/linux-boot-process-part-1-e8fea015dd66

x86 has operational modes: **real mode** and (then) **protected mode**. Real mode happens when it starts, has access only to the first MB of memory, can access memory and IO unrestricted. Protected mode is when multitasking, paging, protection rings already formed.

Protection ring: privilege levels (rings). Ring 0-3. Ring 0 is the most privileged, ring 3 is the least. Linux only uses ring 0 and ring 3. Ring 0 is kernel mode, ring 3 is user mode.

Ring 3 (user mode) cannot access IO nor manage memory. To do so, it uses system call. For example, `malloc()` is the function that implements the system call `sbrk()`. A system call is initiated by generating a **software interrupt**. It switches the content to kernel mode and switches back to user mode afterwards.

When the computer is starting, BIOS performs **POST (power on self-test)** and **boot**. POST checks the connected hardware such as CPU, memory, GPU, disk controllers. Boot starts the boot process by loading the first sector of memory (master boot record (MBR)).

Because the execution context provided by BIOS is too restrictive, it uses boot loader (GRUB 2) to help load Linux kernel. GRUB 2 is too big to store in MBR, that's why it is divided into stages. The first stage is the bare minimal code to boot to the next stage (second stage). The second stage is the `/boot/grub` that loads the configuration file and drivers from the file system.

# More complete of step 4 - 8 above

Source: 

- https://medium.com/@cloudchef/linux-boot-process-part-2-bd7514913495
- https://en.wikipedia.org/wiki/Initial_ramdisk
- https://en.wikipedia.org/wiki/RAM_drive

Kernel boot process:

1. Check if the boot manager loaded the code following the layout required by the "kernel boot protocol"
2. Detect memory layout, validate CPU arch
3. Prepare the system to switch to protected mode:
   1. Initialize **Interrupt Handler Table**: a data structure that associates a list of interrupt handlers (ISR) with a list of interrupt requests (IRQ).
   2. Initialize **Global descriptor table**: a data structure that defines the characteristics of memory segments
4. Switch to protected mode: decompressing kernel
5. Kernel starts executing. Paging is enabled, interrupt handler table is initialized. `start_kernel()` is called, and the subsequent called functions have the PID 0. `start_kernel` initializes many kernel subsystems, one of them is the task scheduler.
6. after `start_kernel()` finishes, the first user space process to run is `kernel_init()` with PID 1. After doing a bunch of things, this function call the `init` process

Then, it runs **initial ram disk** scheme, which is loading a temporary root file system into memory. Two methods: initrd and initramfs. By the way, ram disk refers to a block of RAM that the computer treats as if it was a secondary storage.

Why do we need initial ram disk?

1. The real root file system may be on RAID (partitioned into several disk) or other complicated things. This makes booting from the disk is more complicated. That's why the initial ram disk mounts the temporary root file system on RAM, just for booting purpose.
2. Drivers in the kernel are in the form of module (that can be loaded by `modprobe`). Not all drivers are loaded in the first place, because it would be too large. When doing initial ram disk, initdr runs `/linuxrc` (initramfs runs `/init`) to find the needed module and load them. 

After the `kernel_init()` finishes, it enters **init process**, implemented by **systemd**. The systemd checks the root file system, checks and mounts additional file systems, initialize network cards, start many daemons, sets getty on the terminals for user to use the shell.

Very good diagram of the boot process:

![boot](https://miro.medium.com/max/700/1*_riwUOYCIRXdZVJHtODxoA.png)

Image source: https://medium.com/@cloudchef/linux-boot-process-part-2-bd7514913495