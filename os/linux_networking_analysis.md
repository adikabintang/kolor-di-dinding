Sources:

- https://medium.com/@oscar.eriks/case-study-network-bottlenecks-on-linux-part-1-the-nic-c24d62826a64
- https://medium.com/@oscar.eriks/case-study-network-bottlenecks-on-a-linux-server-part-2-the-kernel-88cf614aae70
- https://opensourceforu.com/2016/10/network-performance-monitoring/
- https://access.redhat.com/sites/default/files/attachments/20150325_network_performance_tuning.pdf
- https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/performance_tuning_guide/s-network-packet-reception
- https://www.fir3net.com/UNIX/Linux/the-journey-of-a-frame-through-a-linux-based-system.html
- http://outofsync.net/wiki/index.php?title=Monitoring_linux_system_performance

# Intro: overview of packet reception

![net_reiceve](https://access.redhat.com/webassets/avalon/d/Red_Hat_Enterprise_Linux-6-Performance_Tuning_Guide-en-US/images/99794752f8e1ae820b246ae92227b430/packet-reception.png)

Image source: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/performance_tuning_guide/s-network-packet-reception

![net_receive_2](https://www.fir3net.com/images/articles/Linux_Network_Stack_1.png)

Image source: https://www.fir3net.com/UNIX/Linux/the-journey-of-a-frame-through-a-linux-based-system.html

1. NIC receives the frame
2. The frame is moved to the RAM with DMA
3. NIC raises hardware interrupt to the CPU
4. The hardware interrupt handler runs device driver and triggers a software interrupt
5. The software interrupt handler places the frame to a kernel data structure `sk_buff` (socket buffer)
6. The packet is passed to the receive socket buffer
7. Application calls a syscal such as `read()` or `recv()` or `recvfrom()` to read the data in the socket.

# Troubleshooting

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

SYN-RECV is a state when server does not receive ACK in TCP connection handshake (possible cause: TCP SYN flood attack DoS).

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
- NIC driver then give interrupts to the CPU
- After receiving the interrupt, the data from the ring buffer will be moved to RAM in socket receive buffer

Socket receive buffer size is in `net.ipv4.tcp_rmem`, and the write buffer is in `net.ipv4.tcp_wmem`. Both can be seen by:

```bash
sysctl -a | egrep "tcp_(r|w)mem"
```

## Socket Receive Buffer

### Collapsing

Collapsing: when the kernel socket buffer is nearing its' max size, the kernel tries to identify segment in the buffer that has identical metadata, and tries to combine them, so as to not have identical metadata filling up the buffer.

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

# Misc

1. How to see open ports: `netstat -l`, more complete with the process name: `netstat -tulpn`
2. ...
