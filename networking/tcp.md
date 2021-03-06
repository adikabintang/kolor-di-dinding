Sources:

- https://www.youtube.com/watch?v=tyk2-0MY9p0
- https://packetbomb.com/understanding-throughput-and-tcp-windows/#:~:text=Bytes%20in%20flight%20is%20the,we%20can%20send%20more%20data.
- https://devcentral.f5.com/s/articles/tuning-the-tcp-profile-part-one 
- https://devcentral.f5.com/s/articles/the-send-buffer-in-depth-21845 
- https://paulgrevink.wordpress.com/2017/09/08/about-long-fat-networks-and-tcp-tuning/ 
- https://medium.com/@nic.kong/long-fat-network-lfn-and-tcp-7df4654b7c21 
- https://wwwx.cs.unc.edu/~sparkst/howto/network_tuning.php 

# Understanding TCP throughput

1. Bandwidth: total capacity that the channel can pass at a time
2. Throughput: the actual data transferred (really received) through a channel
3. Bandwidth delay product (BDP):
   1. "the amount of data TCP should have within the transmission path at any one time in order to fully utilize the available capacity".
   2. BDP = bandwidth * round-trip delay time
   3. BDP = bytes/sec * sec = **bytes**
   4. BDP: the maximum amount of data that has been transmitted but not yet acknowledged at any given time. This is also known as *in-flight bytes*.
   5. A network with a large BDP is known as a long fat network (LFN).
   6. How to measure BDP:
      1. know the bandwidth of the link
      2. get the RTT using iperf
      3. calculate BDP.
      4. If BDP > 12500 bytes, it's an LFN 
4. Amount of data the receiver *says* it can receive: **receive window** (RWND, the value is advertised to the sender periodically)
5. Amount of data the sender *thinks* it can send: **min(SNDBUF, CWND, RWND, BDP)**
6. Window size value and window scale (scaling factor) is in TCP header (sent when doing the TCP handshake).
7. Congestion window: **CWND**. 
   1. Maintained by the sender. 
   2. It's a sender side flow control based on network conditions and capacity.
   3. Not sent in TCP. It's a state variable.
   4. Defined as *multiples* of MSS (maximum segment size) (will exponentially grow)
   5. how this increases in TCP slow start for congestion control: 
      1. CUBIC: exponential growth of CWND. When it limits the slow-start threshold (ssthresh), it grows linearly. When there is a packet loss, the CWND drops down (like CWND = CWND / something, this is called back-off)
      2. BBR: like cubic, but instead of multiple of MSS, it's a multiple of BDP (https://blog.apnic.net/2020/01/10/when-to-use-and-not-use-bbr/)
   6. Sender is bound by CWND even if RWND is large
8. SNDBUF: send buffer
   1. SNDBUF: size of socket buffer application is writing to
   2. set by OS/application
   3. optimal size depends on BDP
   4. Send buffer limit determines how much data is kept outstanding in TCP for one blocking or non-blocking send request
   5. Read more here: https://devcentral.f5.com/s/articles/the-send-buffer-in-depth-21845
9. When the throughput is not optimal, do this checklist:
   1. Measure BDP
   2. What is the advertised RWND?
      1. Is the receiver application taking the data from the receive buffer?
   3. Are the bytes in flight (CWND) increasing and reaching BDP or RWND? If no:
      1. Does the sender stop and wait for ACKs after sending the same amount of data over and over? if yes, send buffer problem
      2. Is there any packet loss (=retransmissions, dup ACKs) that prevents CWND from growing? If yes, there is congestion
10. CWND is used for congestion control, RWND is used for flow control.

# Congestion control algorithms

Sources:

- https://www.net.t-labs.tu-berlin.de/teaching/computer_networking/03.07.htm
- https://book.systemsapproach.org/congestion/tcpcc.html#tcp-cubic
- https://en.wikipedia.org/wiki/CUBIC_TCP

## Intro: what is AIMD

AIMD = Additive-increase, multiplicative-decrease (AIMD)

To sum up:

- Initial CWND = usually 10 * MSS [[RFC6928](https://tools.ietf.org/html/rfc6928)]. The CWND grows exponentially everytime an ACK is received.
- When it hits the ssthreshold, it grows linearly. This phase is called congestion avoidance.
- When there is a packet loss (timeout/duplicate ACK*), the ssthreshold is set to the 3/4 of the prev value, and the CWND is multiplicatively decreased below the ssthreshold.

![aimd](https://www.net.t-labs.tu-berlin.de/teaching/computer_networking/03.07-Dateien/congwin.gif)

Image source: https://www.net.t-labs.tu-berlin.de/teaching/computer_networking/03.07.htm

*what is duplicate ACK?

Source: https://book.systemsapproach.org/congestion/tcpcc.html#fast-retransmit-and-fast-recovery and https://stackoverflow.com/questions/48148820/what-is-duplicate-ack-when-does-it-occur

A duplicate ACK is sent when the receiver gets the out of order packet. See this picture below:

![dupack](https://book.systemsapproach.org/_images/f06-12-9780123850591.png)

Image source: https://book.systemsapproach.org/congestion/tcpcc.html#fast-retransmit-and-fast-recovery

"TCP fast retransmit" refers the re-transmission of the packet that the sender assumes lost by infering from the duplicate ACK instead of waiting for ACK timeout for that packet.

## CUBIC

Like AIMD, but it models the CWND with a cubic function. See here: https://en.wikipedia.org/wiki/CUBIC_TCP

## BBR

Based on BDP. Might not be fair if, as it may take over the link if there is other connections with different congestion control algorithm too.

# Tuning TCP throughput

- https://paulgrevink.wordpress.com/2017/09/08/about-long-fat-networks-and-tcp-tuning/
- https://www.cyberciti.biz/faq/linux-tcp-tuning/
- https://en.wikipedia.org/wiki/Retransmission_(data_networks)

## Tuning window size

- `net.core.wmem_max` (write): max OS send buffer size for all types of connection
- `net.core.rmem_max` (read): max OS read buff size for all types of connections

```bash
echo 'net.core.wmem_max=12582912' >> /etc/sysctl.conf
echo 'net.core.rmem_max=12582912' >> /etc/sysctl.conf
```

minimum, initial, maximum. Higher: more memory used.

```bash
echo 'net.ipv4.tcp_rmem= 10240 87380 12582912' >> /etc/sysctl.conf
echo 'net.ipv4.tcp_wmem= 10240 87380 12582912' >> /etc/sysctl.conf
```

turn on window scaling:

```bash
echo 'net.ipv4.tcp_window_scaling = 1' >> /etc/sysctl.conf
echo 'net.ipv4.tcp_timestamps = 1' >> /etc/sysctl.conf
```

turn on Selective ACK (SACK), which explicitely lists packets that are acknowledged:

```bash
echo 'net.ipv4.tcp_sack = 1' >> /etc/sysctl.conf
```

## Tuning segmentation offloading

- https://en.wikipedia.org/wiki/Large_send_offload
- https://docs.vmware.com/en/VMware-vSphere/6.0/com.vmware.vsphere.networking.doc/GUID-FB4F8DB7-B4AC-4442-9B0B-B776F0C7BCCB.html

idea: reducing CPU overhead by passing a large multipacket buffer to NIC, and let the NIC splits the buffer into multiple packets.

```bash
ethtool -K $interface_name tso on    # turn on, we want this
ethtool -K $interface_name tso off   # turn off
```

# Problems

## Bufferbloat

Sources:

- https://en.wikipedia.org/wiki/Bufferbloat

When the buffer is too large, and there are a lot of packet loss, it takes longer to fill the receiver buffer. This uncertain time to fill the receive buffer can cause jitter (packet delay variation) and overall throughput. Interactive apps hate this.

How to solve? use TCP BBR congestion control. Why?

Other congestion control algorithm uses packet loss as the sign of congestion. When it detects packet loss (which the sender thinks it's congestion, although it's not necessarily a congestion. May be it's just pure packet loss), it will decrease the CWND multiple times (remember: AIMD). This makes the time to fill the receive buffer longer, even though there is no congestion.

If we use BBR, it scales the CWND with multiple of BDP, and see the BDP as the parameter of a congestion. BDP will not affect the calculation as much as the packet loss if the reason is the real packet loss, not the congestion.

## head of line (HoL) blocking

Sources:

- https://http3-explained.haxx.se/en/why-quic/why-tcphol
- https://stackoverflow.com/questions/45583861/how-does-http2-solve-head-of-line-blocking-hol-issue/45583977?stw=2#45583977

Let's start from the higher layer.

HTTP1.0 uses 1 HTTP request per TCP connection. If you have 6 TCP connections (like browsers), and 12 HTTP requests to fetch a website (html + css + js + pictures + etc), these 12 HTTP requests must be queued up in those 6 TCP connections.

let's focus on a single TCP connection. For the next HTTP1.0 request, the first one needs to complete first. If there are many packet loss, the first request blocks the request. This is HoL on the app layer. HTTP2 solves this.

In HTTP2, the second request can be made without waiting for the first one to complete (multiplexing HTTP2 connections on a single TCP connections). HTTP2 solves the HoL in app layer. But not in the transport layer. One lost packet in the TCP stream makes *all* streams wait until it is retransmited and received. QUIC solves this.

QUIC implements *streams*, and the QUIC streams can be made without waiting for the previous one to complete (multiplexing QUIC streams on a single UDP connections).

See the picture here, it's nice: https://http3-explained.haxx.se/en/why-quic/why-tcphol

## SYN flood attack

Attacker sends SYN, server replies with SYNACK, and the attacker flees. This condition is also known as TCP half open.

Upon receiving the SYN, the server saves the Transmission Control Block (TCB) in a struct, taking a few bytes. TCB keeps the state, such as information about IP address and port of that connection, and so on. If the attackers flood the server with SYN and does not reply with the ACK after server sends SYNACK, this can deplete the server's resource. When the server does not receive ACK, the server may re-transmit the SYNACK and also set the timeout until it purges that connection.

What to do: TCP SYN cookies (see page 58 of https://moodle.epfl.ch/pluginfile.php/2722993/mod_resource/content/0/transportSols.pdf and https://en.wikipedia.org/wiki/SYN_cookies)

The server sends a cookies (let's say `y`) to the client, then the server does not keep the state (not in memory, no timer for timeout). Client sends `y+1` with the ACK. Server subtract that, and check if it the cookie is valid, then it will construct the TCB.

The cookie depends on timestamp (for checking the timeout) and (src ip, src port, dest ip, dest port). All of them are hashed. The server, when receiving the cookie back from client with the ACK, check the validity of the hash value.

# misc

- For TCP, if the server is not listening, server machine will return TCP RST to the client. For UDP, it will be ICMP type 3 destination is unreachable.
- ..
