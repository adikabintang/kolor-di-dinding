Reading materials:
https://medium.com/@oscar.eriks/case-study-network-bottlenecks-on-linux-part-1-the-nic-c24d62826a64
https://medium.com/@oscar.eriks/case-study-network-bottlenecks-on-a-linux-server-part-2-the-kernel-88cf614aae70
https://opensourceforu.com/2016/10/network-performance-monitoring/

# Introduction
Packets start to drop. What happens?

Problems could be in:
- NIC
- Soft interrupt issued by device driver
- Kernel
- Network/transport layer (IP, TCP, UDP, etc)

## SYN-RECV state
TCP connection handshake:
- Client sends SYN
- Server sends SYNACK
- Client sends ACK
Then, TCP connection is established.

SYN-RECV is a state when server does not receive ACK in TCP connection handshake.

In Linux, to know the number of SYN-RECV is to:
```bash
netstat -an | grep -c SYN_RECV
```
If the result is 0, then all good.

## NIC Ring Buffer
NIC Ring Buffer is the temporary storage to receive packets.

To check ring buffer size:
```bash
ethtool -g nameofdevicering
```

A very rough idea of how the system receive packets:
- Packets fill the NIC ring buffer
- NIC driver then give interrupts to the kernel
- After receiving the interrupt, the data from the ring buffer will be moved to RAM in socket receive buffer

## Socket Receive Buffer
### Collapsing
Collaping: when the kernel socket buffer is nearing its' max size, the kernel tries to identify segment in the buffer that has identical metadata, and tries to combin them, so as to not have identical metadata filling up the buffer.

### Pruning
Pruning: when no more collaping can happen, the kernel drops new packets since they cannot fit in the buffer.

To monitor collapsing and pruning:
```bash
netstat -s | grep -P "(collapse|prune)"

# example output:
# 26 packets pruned from receive queue because of socket buffer overrun
```

To check the size of read/write buffer:
```bash
sysctl -a | grep -P "tcp_(r|w)mem"
```