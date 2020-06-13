# Docker basics

Sources:

- https://www.linuxjournal.com/content/everything-you-need-know-about-linux-containers-part-i-linux-control-groups-and-process
- https://events.static.linuxfound.org/sites/events/files/slides/An%20introduction%20to%20Control%20Groups%20(cgroups)%20(2).pdf
- https://stackoverflow.com/questions/46450341/chroot-vs-docker
- https://en.wikipedia.org/wiki/Linux_namespaces
- https://medium.com/@saschagrunert/demystifying-containers-part-i-kernel-space-2c53d6979504
- https://www.youtube.com/watch?v=sK5i-N34im8
- 
Just the oversimplified of how Docker works.

Docker mainly uses these two things to work:

- cgroup: for resource management and limiting
- namespace: for isolation

## Cgroup

- cgroup is for resource limiting such as memory and CPU (there are other things, but let's focus on this)
- systemd uses cgroup to organize processes
- each systemd's service is a cgroup. all processes that are started by that service use that cgroup
- you can access cgroup directly or indirectly (using docker)
  - directly with service example:

```
[Service]
ExecStart=/bin/foo
MemoryAccounting=true
MemoryLimit=400K
```

## Namespace

Docker shares the kernel with host OS. Then how docker can have its own root filesystem, network drivers, etc? It uses Linux Namespace for isolation.

Namespace kinds:

- mnt namespace: provides root filesystem (think of chroot)
- pid namespace: process within that cgroup only sees itself and the children
- network namespace: allows to have its own net stack
- user namespace: allows non-root on host OS to be mapped to the root within the container
- uts namespace: allows to have different host and domain names
- ipc: isolate ipc
