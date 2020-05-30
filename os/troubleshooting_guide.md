# High Load

Source: https://www.linuxjournal.com/article/10688

Three issues to see in order:

1. CPU
2. RAM
3. I/O

**Steps:**

1. Run `top`

Example output:

```bash
top - 23:49:21 up  2:16,  1 user,  load average: 0.78, 0.55, 0.45
Tasks: 269 total,   1 running, 268 sleeping,   0 stopped,   0 zombie
%Cpu(s):  5.0 us,  2.3 sy,  0.0 ni, 90.7 id,  0.8 wa,  0.7 hi,  0.4 si,  0.0 st
MiB Mem :   7681.2 total,   1972.0 free,   2678.5 used,   3030.7 buff/cache
MiB Swap:   7832.0 total,   7827.2 free,      4.8 used.   4253.6 avail Mem
```

What to see:

- `load average: 0.78, 0.55, 0.45`

Load average is the average number of processes that waits for CPU time. The less the better. Those three numbers are the load average for the last 1, 5, 10 minutes. If it is sth like `big, less, least` than we are experiencing increasing load since the last 10 minutes.

- `n zombie`

Number of zombie process. Kill zombie process with `kill -s SIGCHLD pid`. They actually do not slow things down, but they can take the available PID number available.

- `%Cpu(s):  5.0 us,  2.3 sy,  0.0 ni, 90.7 id,  0.8 wa,  0.7 hi,  0.4 si,  0.0 st`

  - `us` user space usage, the less the better
  - `sy` kernel space usage, the less the better
  - `id` CPU idle, the higher the better. If the system is slow but CPU idle is high, most probably it's not because of the CPU bound processes.
  - `wa` IO wait, the less the better. If IO wait is high, probably the system is slow because of IO wait or maybe RAM issues (if swap is on).

2. See the `top` with CPU usage sorted: `top -o %CPU`
3. See the `top` with memory usage sorted: `top -o %MEM`

So far, `top` is OK for examining CPU and RAM issues. What about I/O?

1. In addition to top, you can see memory, swap, io, system, cpu with `vmstat`, read [here](linux_io_notes.md#vmstat)

```
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0 377796 157908 164976 2116256    1    5    56    46   73  235  8 11 81  0  0
 0  0 377796 150344 164976 2124672    0    0     0     0 42460 7281  2  8 90  0  0
```

`wa` under `cpu` is IO wait. `io` (`bi` for block in or read, `bo` for block out or write). If these 2 are high, chance is you have an I/O problem.

2. To see which disk parition does the IO a lot, use `iostat`

```
Linux 5.6.13-200.fc31.x86_64 (localhost.localdomain) 	05/31/2020 	_x86_64_	(4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          12.35    0.24    4.53    0.43    0.00   82.45

Device             tps    kB_read/s    kB_wrtn/s    kB_dscd/s    kB_read    kB_wrtn    kB_dscd
dm-0             13.00       203.77        39.87         0.00    1998145     390996          0
dm-1              0.11         0.24         0.40         0.00       2316       3936          0
dm-2             29.37        70.96       233.53         0.00     695868    2289920          0
sda              21.78       276.71       271.19         0.00    2713320    2659233          0
```

3. To see which process does the IO, use `iotop`

```
Total DISK READ :	0.00 B/s | Total DISK WRITE :       0.00 B/s
Actual DISK READ:	0.00 B/s | Actual DISK WRITE:       0.00 B/s
    TID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND                                            
      1 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % systemd --switched-root --system --deserialize 28
      2 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [kthreadd]
      3 be/0 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [rcu_gp]
```

# Local network

Source: https://www.linuxjournal.com/article/10712

A client (C) and a HTTP server (S) who is listeing to port 80 run in the same network. Client cannot connect to the server. What to do?

1. Check using another client (A) machine in the same network. If it works, that client C is the culprit. If it does not work, follow the next step.
2. Make sure the server is connected to the network.
   1. Use `ethtool` (e.g. `sudo ethtool eth0`) and check if `Link detected: yes`
3. Check if they are in the same network.
   1. Use `ip a` to see their network address AND subnet
4. Check our gateway using `sudo route -n`

```
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.0.1     0.0.0.0         UG    600    0        0 wlp58s0
192.168.0.0     0.0.0.0         255.255.255.0   U     600    0        0 wlp58s0
```

5. `ping` the destination
6. Check if the server runs (using `ps`)
7. Check if the server listens to the correct port (e.g. 80)
   1. From the server: `netstat -tulpn`
   2. From the client: 
      1. `telnet SERVER_IP SERVER_PORT`
      2. `nmap -p SERVER_PORT SERVER_IP`

Deeper see [linux_networking_analysis.md](linux_networking_analysis.md)

# Remote Network

Source: https://www.linuxjournal.com/article/10738

A client C cannot open example.com. What to do?

1. Check if we can connect to the gateway
   1. Run `sudo route -n`
   2. `ping` the gateway IP address
2. Check if the DNS returns an IP:
   1. `nslookup example.com` or use `dig`
3. Use `traceroute` to see latency to each hop (let's hop this is not blocked by the firewall: traceroute uses ICMP (in windows) or UDP (linux))

Deeper see [linux_networking_analysis.md](linux_networking_analysis.md)