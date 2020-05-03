source: https://www.thegeekstuff.com/2011/02/linux-boot-process/

1. BIOS searches, loads, and executes Master Boot Record (MBR) bootloader. The boot loader can be in hard drive of USB stick. It also does some integrity check.
2. MBR contains GRUB boot loader. It loads the GRUB boot loader and executes it.
3. GRUB (Grand Unified Bootloader) loads and executes kernel and initrd images.
4. Kernel mounts the root file system
5. Kernel executes /sbin/init (which has PID 1)
6. initrd (initial RAM disk) is used by the kernel as the temporary root file system until the kernel is booted and the real root filesystem is mounted.
7. `init` identifies the default init level and uses that to load all appropriate programs.
8. `Runlevel` programs: programs that are run when the system is booting up (and also some when shutting down). The runlevel programs are in `/etc/rc.d/rc*.d/`.
