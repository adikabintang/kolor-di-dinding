# OSPF

Sources:

- https://www.youtube.com/watch?v=kfvJ8QVJscc
- https://www.youtube.com/watch?v=QyymlFWDEgM
- https://www.networkworld.com/article/2348778/my-favorite-interview-question.html

## Concept of link state protocols

1. Every router floods info about itself, its links, its neighbors to all routers. Each router calculates shortest path independently.
   1. This prevents loop since it maps the whole network. RIP, which does not know the routers behind its direct neighbor, is vulnerable to loop
2. Because it maps the whole network, to make it scalable, the network is divided into areas
3. The inter-area network is like a distance vector.

## Link state protocol: OSPF

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
| 10.10.1.0/24   |            |     12.12.1.0/24  |
------------------            --------------------|
                                        |
                                      ABR_2
                                        |
                              ---------ABR_4-------
                              |     area 2        |
                              |     13.13.0.0/24  |
                              |     13.13.1.0/24  |
                              ---------------------
```

The Area Border Router (ABR) aggregates the network within the area and advertises it to another area. SPF calculation is only done in the ABR. ABR is a member of 2 or more areas.

Since inter-area OSPF is like a distance vector, it is vulnerable to loop. To prevent loop, traffic from one area to another **must go through area 0**.

Autonomous System Border Router (ASBR) is the border router that is connected and make an eBGP peer session to another ASBR of different AS network.

# BGP

TODO