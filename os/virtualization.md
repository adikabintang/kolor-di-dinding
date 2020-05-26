Sources:

- https://www.redhat.com/en/topics/virtualization/what-is-a-hypervisor
- https://www.redhat.com/en/topics/virtualization/what-is-KVM
- https://mkdev.me/en/posts/virtualization-basics-and-an-introduction-to-kvm
- https://www.linuxjournal.com/article/9764
- https://en.wikipedia.org/wiki/Hardware-assisted_virtualization
- https://en.wikipedia.org/wiki/X86#Extensions
- https://en.wikipedia.org/wiki/Popek_and_Goldberg_virtualization_requirements
- https://en.wikipedia.org/wiki/QEMU

# Virtualization basics

1. Hypervisor easy definition: software that creates and runs VM
   1. Hypervisor is also known as Virtual Machine Monitor (VMM)
2. Types:
   1. Type 1: for bare metal. Example: Xen, KVM
   2. Type 2: On top of host OS. example: virtualbox

Let's talk specifically about type 1 hypervisor.

Hypervisor needs some of the OS components to operate: process scheduler, memory manager, IO stack, device drivers, network stack and so on. Xen is virtually an OS. It has all of the components mentioned before. KVM turns Linux kernel to a hypervisor type 1, and those components needed are already present in the Linux kernel. So, the guest OS in KVM runs as a Linux process. KVM itself is a module in Linux (very good introduction on how to write and load a module: https://www.youtube.com/watch?v=juGNPLdjLH4).

## Virtualization approaches

1. Dynamic translation (full virtualization based on software)
   1. hypervisor catches all commands from guest OS and translate them. Used by VMware.
2. Paravirtualization
   1. Hypervisor provides an interface to the guest OS through a para-API. The guest OS code is modified so that it calls the para-API
3. Hardware-assisted virtualization (full virtualization assisted by CPU)
   1. CPU (intel VT-x, AMD-V) has extension that basically meets the requirements to perform virtualization (such as Privileged instructions, Control sensitive instructions) that can be leveraged by hypervisors. KVM uses this.

## More about KVM

KVM installation consists of the following:

1. Device driver for managing virtualization hardware
   1. The driver is exposed by a [character driver](https://askubuntu.com/questions/1021394/what-is-a-character-device) `/dev/kvm`
2. User-space component that emulates PC hardware
   1. By QEMU

QEMU is a user-space emulator that can emulate I/O hardware and processor. KVM uses QEMU for I/O emulation.
