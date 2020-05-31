# NAT

Sources: 

- https://www.youtube.com/watch?v=qij5qpHcbBk
- https://computer.howstuffworks.com/nat1.htm

NAT operates with a NAT table. The basic idea is it masquerades private IP with a public IP.

3 types of NAT:

**1. Port Address Translation (PAT)**

```
---------------|
home           |
               |
client --> router -------> server
---------------|
```

Client (src ip: 192.168.1.2, src port: 8897) sends a HTTP request to a server (dst ip: 87.63.11.56, dst port: 80).

The router performs PAT by masquerading the private client IP address to the public IP address. The port stays the same. Typically used in home setting.

**2. Dynamic NAT**

Like PAT, but the public IP used for masquerading is taken from a pool of public IP addresses. After use, the public IP address is released to the pool again.

**3. Static NAT**

Like dynamic NAT, but it is static: the mapping is fixed and the public IP is not released after use.

TODO: 

- NAT traversal, useful for VoIP or peer-to-peer

# Firewall

Source: https://www.booleanworld.com/depth-guide-iptables-linux-firewall/

Firewall in linux: iptables. `iptables` is the command line interface to configure `netfilter`, a packet filtering framework in linux.

## Tables

Packet that arrive go through some tables:

1. filter table: for filtering packet, decides whether it should be allowed to reach the destination
2. mangle table: change the IP header such as TTL
3. NAT table: for storing NAT table
4. raw table: this table allows to work with packet before the kernel starts tracking state (NEW/ESTABLISHED)

## Chains

Chains: PREROUTING, INPUT, FORWARD, OUTPUT, POSTROUTING

![chains](https://www.booleanworld.com/wp-content/webp-express/webp-images/doc-root/wp-content/uploads/2017/06/Untitled-Diagram.png.webp)

Image source: https://www.booleanworld.com/depth-guide-iptables-linux-firewall/

## Target

After the firewall matches the packet in the table, it does one of these

- ACCEPT
- DROP: silent drop
- REJECT: client receives ICMP "connection refused" for TCP or "destination host unreachable" for UDP

Drop vs reject: drop is more secure (think about attacker does not know if it is rejected since it just feels the destination does not exist)

