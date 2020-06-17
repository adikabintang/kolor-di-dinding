# IP addressing

> how many address available for 192.168.0.0/24

Format: IP/subnet mask

```
all address for that subnet mask = 2 ^ (32 - subnet mask)

all usable address for that subnet mask = 2 ^ (32 - subnet mask) - 2
```

- The first address is the network address
- The last one is broadcast

So, for that question (192.168.0.0/24)

- All addresses = 2 ^ (32 - 24) = 256
- All usable address (excluding network address and broadcast) = 254
- Network address = 192.168.0.0
- Broadcast address = 192.168.0.255
- Usable = 192.168.0.1 - 192.168.0.254


## IPv4 vs IPv6

Advantage of IPv6 over IPv4:

1. IPv4 is 32 bit long, while IPv6 is 128 bit long. IPv6 is very far way from exhaustion
2. IPv4 requires manual or DHCP for addressing. IPv6 requires manual or autoconfiguration, which is less complex than DHCP.
3. IPv4 requires NAT to prevent exhaustion, IPv6 does not need it.

So why we don't use the IPv6 everywhere? It's because it's not backward compatible to IPv4. Therefore, upgrading requires upgrading all IP-based things in the network, which is too many and very hard.

TODO: learn IPv6 https://youtu.be/ck5bR1WlOo0?t=1454

# Routing

## OSPF

Sources:

- https://www.youtube.com/watch?v=kfvJ8QVJscc
- https://www.youtube.com/watch?v=QyymlFWDEgM
- https://www.networkworld.com/article/2348778/my-favorite-interview-question.html

### Concept of link state protocols

1. Every router floods info about itself, its links, its neighbors to all routers. Each router calculates shortest path independently.
   1. This prevents loop since it maps the whole network. RIP, which does not know the routers behind its direct neighbor, is vulnerable to loop
2. Because it maps the whole network, to make it scalable, the network is divided into areas
3. The inter-area network is like a distance vector.

### Link state protocol: OSPF

1. OSPF is a link state routing protocol: it calculates the "link state" os the metric for shortest path selection. RIP, on the other hand, is a distance-vector routing which calculates the number of hops as the metric.
2. OSPF operates by exchanging Link State Advertisement (LSA)
3. The LSA is kept in a Link State Database (LSDB). The LSDB is the same in all routers.

The main steps in OSPF:

1. Become neighbors
2. Exchange LSDB info
3. Calculate best path


**1. Become neighbors:**

- To become neighbors, routers send `hello` packets bringing the router ID. The router ID looks like IPv4 address, but it't not IPv4 address. It can be configured manually or it will take the loopback address as the ID or the higher UP IP address if no loopback set.
- Select Designated Router (DR) and Backup DR (BDR). If there is an event from any router, by default, every router that receives the advertisement will broadcast the received advertisement. If there is DR, only DR will re-advertise it, preventing flooding the network.

**2. Exhange LSDB info:**

- Router A and B exchange Database Description (DBD), containing what network it has on the LSDB. For example, Router B has info (link state/bandwith data) about network 192.168.1.0/24 that router A does not know. Then, the router A will send a Link State Request (LSR) to ask for the link info about that network.
- Router B will send the information in Link State Update (LSU)
- Router A will send an ack in a Link State Acknowledgement (LSAck)

**3. Calculate best path:**

```
cost = reference bandwidth / interface bandwidth

default reference bandwith = 10^5 Kbps
```

For example, the FastEthernet bw is 10^5 Kbps and the Ethernet is 10^4 Kbps. The cost of FastEthernet is 1 and the Ethernet's is 10. FastEthernet is smaller, meaning it's a more economical path (faster).

If the OSPF network is too large, it can cause problems:

1. Big LSDB, takes up space
2. Big routing table, slow
3. Too much LSA, flooding the network and too often re-calculating best path

**How to manage large OSPF network: Multi-area OSPF.**

Split OSPF into areas. There must be an area 0.

```
------------------            ---------------------
|  area 1        |            |     area 0        |
| 10.10.0.0/24   |----ABR_1---|   12.12.0.0/24  ASBR-----another AS
| 10.10.1.0/24   |            |   12.12.1.0/24    |
------------------            --------------------|
                                        |
                                      ABR_2
                                        |
                              ---------------------
                              |     area 2        |
                              |     13.13.0.0/24  |
                              |     13.13.1.0/24  |
                              ---------------------
```

The Area Border Router (ABR) aggregates the network within the area and advertises it to another area. SPF calculation is only done in the ABR. ABR is a member of 2 or more areas.

Since inter-area OSPF is like a distance vector, it is vulnerable to loop. To prevent loop, traffic from one area to another **must go through area 0**.

Autonomous System Border Router (ASBR) is the border router that is connected and make an eBGP peer session to another ASBR of different AS network.

## BGP

Sources:
- https://www.youtube.com/watch?v=_Z29ZzKeZHc
- https://en.wikipedia.org/wiki/Border_Gateway_Protocol
- Computer Networking: Principles, Protocols, and Practice (https://ufdc.ufl.edu/AA00011742/00001)
- https://networklessons.com/bgp/bgp-route-reflector

1. BGP is path vector protocol. What is path? it's the AS path. So it does something like "to go to 69.69.69.0/24 the path is ASN 65576, 64585, 65538".
2. 2 BGP routers that are connected and work together is called BGP peered routers.
   1. If they belong to the same AS, it's called iBGP peer
   2. If they belong to different ASes, it's called eBGP peer
3. iBGP peer does not forward the advertisement to another iBGP peeer. That's why iBGP routers must be connected in a fully meshed. If the number of iBGP routers are too many to be in fully mesh, we can use Route Reflector (RR) that forward the advertisement to another iBGP routers, see [here](https://networklessons.com/bgp/bgp-route-reflector)
4. To prevent loops, BGP router does not forward/save advertisement that contains its' own AS number in the path.
5. If there are 2 path to a certain subnetwork, BGP prefers the longest prefix match.
   1. For example:
      1. Path 1: AS 65534, 65535 for 1.1.1.0/24
      2. Path 2: AS 65576, 62345 for 1.1.0.0/16
   2. When there is a traffic for 1.1.1.64, it will choose path 1. Vulnerability: BGP hijacking, see [wiki](https://en.wikipedia.org/wiki/BGP_hijacking).
6. In order to be able to route traffics from inside AS to outside, the AS border router must be configured with `next-hop-self` to the interior AS.
7. The interior AS routing protocol can be any IGP such as OSPF, EIGRP, RIP, IS-IS, etc.

## Security: BGP hijacking

TODO
