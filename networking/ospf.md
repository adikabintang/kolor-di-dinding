# OSPF

Sources:

- https://www.youtube.com/watch?v=kfvJ8QVJscc
- https://www.youtube.com/watch?v=QyymlFWDEgM
- https://www.networkworld.com/article/2348778/my-favorite-interview-question.html
- https://www.geeksforgeeks.org/route-poisoning-and-count-to-infinity-problem-in-routing/#:~:text=The%20main%20issue%20with%20Distance,updates%20at%20the%20same%20time.
- https://moodle.epfl.ch/pluginfile.php/2736146/mod_resource/content/0/lsSols.pdf

## Concept of link state protocols

1. Every router floods info about itself, its links, its neighbors to all routers. Each router calculates shortest path independently.
   1. This prevents loop since it maps the whole network. RIP, which does not know the routers behind its direct neighbor, is vulnerable to loop
2. Because it maps the whole network, to make it scalable, the network is divided into areas
3. The inter-area network is like a distance vector.

## Link state protocol: OSPF

1. OSPF is a link state routing protocol: it calculates the "link state" os the metric for shortest path selection. RIP, on the other hand, is a distance-vector routing which calculates the number of hops as the metric.
2. OSPF operates by exchanging Link State Advertisement (LSA)
3. The LSA is kept in a Link State Database (LSDB). The LSDB is the same in all routers.
4. All routers have a full picture of the topology. Therefore, it does not scale for a large network.

The main steps in OSPF:

1. Become neighbors
2. Exchange LSDB info
3. Calculate best path

**1. Become neighbors:**

- To become neighbors, routers send `hello` packets bringing the router ID. The router ID looks like an IPv4 address, but it't not IPv4 address. It can be configured manually or it will take the loopback address as the ID or the higher UP IP address if no loopback set.
  - `hello` message is used to discover neighboring routers and detecting failures.
- Select Designated Router (DR) and Backup DR (BDR). If there is an event from any router, by default, every router that receives the advertisement will broadcast the received advertisement. If there is DR, only DR will re-advertise it, preventing from flooding the network.
- When two routers become neighbhors, they *synchronize* their LSDB.

**2. Exhange LSDB info:**

- Router A and B exchange Database Description (DBD), containing what network it has on the LSDB. For example, Router B has info (link state/bandwith data) about network 192.168.1.0/24 that router A does not know. Then, the router A will send a Link State Request (LSR) to ask for the link info about that network.
- Router B will send the information in Link State Update (LSU)
- Router A will send an ack in a Link State Acknowledgement (LSAck)

**LSDB and LSA**

- After synchoronized, routers send and receive LSA.
- LSA describes the states of the routers: their attached networks and neighboring routers
- LSAs are flooded inside IP packets (unlike BGP which uses TCP)
- LSA contains a sequence number (only new seq number is accepted to prevent loop) and age.

**3. Calculate best path:**

Performed on routers independently, based on the same LSDB among all routers. OSPF uses Dijkstra algorithm to calculate the best path.

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

Inside an area, it's a link state routing. Inter-area is a distance vector. It's analoguous to IGP-EGP. Since inter-area OSPF is like a distance vector, it is vulnerable to loop. To prevent loop, traffic from one area to another **must go through area 0**. This is called **split horizon**.

Autonomous System Border Router (ASBR) is the border router that is connected and make an eBGP peer session to another ASBR of different AS network.

# A little bit about distance vector routing (like RIP)

- RIP uses bellman-ford algorithm to compute the shortest path.
- Unlike OSPF, it does not map the whole network

## Routing loop and count-to-infinity problem in distance vector

Sources:

- https://en.wikipedia.org/wiki/Route_poisoning#:~:text=Route%20poisoning%20is%20a%20method,become%20invalid%20within%20computer%20networks.&text=In%20the%20case%20of%20RIP,a%20routing%20update%20is%20sent.
- https://www.geeksforgeeks.org/route-poisoning-and-count-to-infinity-problem-in-routing/
- https://en.wikipedia.org/wiki/Split_horizon_route_advertisement

```
R1 ----- R2 --x--R3
```

Before R2-R3 is broken, R2 knows it can go to R3 with cost of 1 and R1 to R3 with cost of 2. Then, R2-R3 is down. Before R2 advertises this, R2 receives an advertisement from R1 saying that R1 knows how to get to R3 with cost of 2. Since R2-R1's cost is 1, R2 will think that it can go to R3 with cost of 3 via R1. Then, R2 advertises R2-R3 cost is 3 to R1. And it continues to infinity.

### Mitigation

1. Route poisoning: telling all nodes *immediately* when a link is down that the link is down. How to tell? In RIP, the max hop count is 15, so just tell that the failed link hop count to 16.
2. **Split horizon**: prevents loop by prohibiting a router from advertising a route back onto the interface from which the route was learned. S on the example above, R1 does not advertise the route to R3 to R2.

RIP combines route poisonong, split horizon, and holddown timer. Holddown timer starts when the link is down. When the timer is still running, all advertisement about the link to the router is ignored, unless if it comes from the router that used to be down.
