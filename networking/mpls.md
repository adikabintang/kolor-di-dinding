# MPLS

Sources:

- https://en.wikipedia.org/wiki/Multiprotocol_Label_Switching
- the main video: https://www.youtube.com/watch?v=JHEE6QU3J6M&ab_channel=TeamNANOG
- https://www.youtube.com/watch?v=MEWIdO40U54
- https://www.youtube.com/watch?v=U1w-b9GIt0k
- http://www.gompls.net/2009/08/understanding-mpls-header.html
- https://en.wikipedia.org/wiki/Ethernet_frame#Types
- https://en.wikipedia.org/wiki/EtherType
- http://docs.frrouting.org/en/latest/ldpd.html
- https://networklessons.com/mpls
- https://archive.nanog.org/sites/default/files/tuesday_tutorial_steenbergen_mpls_46.pdf
- https://networkengineering.stackexchange.com/questions/47425/why-does-mpls-need-an-igp-like-ospf-in-order-to-work
- https://en.wikipedia.org/wiki/Label_Distribution_Protocol

Multiprotocol label switching (MPLS) is a routing technique that is based on short path labels, not the network addresses. It does not involve complex lookups in a routing table. But this also means that traceroute cannot know the router in the path, because traceroutes depends on L3 (ICMP error message).

Why MPLS is used/advantages of MPLS:

- This can be used as the tunnel between two sites. We can also say that the path between these sites is isolated from the other path in the network.
- We can influence the packet to chooose a certain path (with traffic engineering), **independent of IP routing protocol's best path**.
- Increase resiliency in case of failure (with Fast Reroute (FRR))
- Build a MPLS core network with cheaper switches. Looking up labels in the FIB is cheaper than looking up IP in FIB. So, less sophisticated ASIC = cheaper.

MPLS operates at the layer between L2 and L3, and often referred to as the L2.5. This is also known as shim header.

How routers know that this packet is MPLS or not? Routers look at the Ethertype field in the Ethernet header. The Ethertypefield defines what protocol it brings. For MPLS, the value for Ethertype field is 0x8847 (and for IPv4 it's 0x0800, and 0x0806 for ARP, etc. See [wiki](https://en.wikipedia.org/wiki/EtherType)). (Not related, just for info: in the IP header, there is a field in the IP header that serves the same purpose: protocol header. That's why introducing a new protocol on top of other protocol might get cumbersome because this the routers might need to recognize this field)

## MPLS operation

```
                            (MPLS domain)
(office, city A) --- ([LER] --- [LSR] --- [LER]) --- (office, city B)
   1.1.1.0/24                                          2.2.2.0/24
```

- Label Edge Router (LER) or Provider Edge (PE): Located at the edge of an MPLS network. Assigned label to the packet for the first time (ingress LER) and remove it (egress LER). Customer networks are connected to LERs.
- Label Switch Router (LSR) or Provider (P): located in the middle of an MPLS network. LSR sees the label on the packet and use it to forward the packet.

Take a look at this example:

A packet from the office in city A wants go to the office in city B (src: 1.1.1.6, dst: 2.2.2.6). The LER will inspect this packet and match the dest IP to the label in the table of Forwarding Equivalence Classes (FEC). Example of the FEC table:

```
| IP addr    | label |
|------------|-------|
| 2.2.2.0/24 | 17    |
| 6.6.6.0/24 | 18    |
```

The label 17 is pushed to the shim header (MPLS PUSH operation).

The LSR, when receiving the packet, will lookup to the Label Information Base (LIB) table and swaps the label for a label (MPLS SWAP operation). Example of the LIB table:

```
| Old label | New label |
|-----------|-----------|
| 17        | 69        |
| 18        | 70        |
```

When the egress LER table receives the packet, it pops the label (MPLS POP operation) and forward it to the office in city B using a normal IP packet.

The path that the MPLS packet goes through is called the **Label Switched Path (LSP)**. This path is established by Label Distribution Protocol (LDP, a manual and simple version) or RSVP-TE (traffic engineering, a more sophisticated approach). LSP is unidirectional (one way). That means the paths for the packet in and out may be different.

### MPLS LDP

Sources:

- https://networklessons.com/mpls/mpls-ldp-label-distribution-protocol
- https://networkengineering.stackexchange.com/questions/38588/rib-vs-fib-differences
- http://resources.intenseschool.com/mpls-ldp-lib-and-lfib/

LDP is a protocol for generating and exchanging MPLS labels. LDP is used to build and maintain LSP database, LDP relies on L3 routing protocol (IGP or BGP) to distribute the labels to neighboring MPLS routers. Why? Because each switches must be fully meshed to distribute the labels.

As an analogy, MPLS LDP builds the forwarding table like other routing protocols (OSPF, BGP, RIP, etc) do.

Routing protocols, like OSPF, BGP, and so on, is used to exchange prefix and other metrics. These are then calculated for the best path and then the routing table is saved into Routing Information Base (RIB). Use `show ip route` to see RIB. RIB is part of the *control plane*. The information from RIB is used to build the Forwarding Information Base (FIB), which is the table that says "the traffic egress towards IP address X should go through interface ethX". Router forwards packet using FIB. FIB is part of the *forwarding plane*.

MPLS LDP generates and exhanges MPLS labels. The MPLS enabled nodes must be peered. We may need to use IGP so that the MPLS nodes can connect to each other (like iBGP that relies on IGP). The label routing information is collected and saved into Label Information Base (LIB). LIB is part of the *control plane*. LIB is used to build the Label Forwarding Information Base (LFIB). LFIB is part of the *forwarding plane*. MPLS forwards packets using LFIB.

![mpls_ldp_lib](https://cdn.networklessons.com/wp-content/uploads/2015/08/xfib-lfib-cisco.png.pagespeed.ic.ceKHN1yir8.webp)

Image source: https://networklessons.com/mpls/mpls-ldp-label-distribution-protocol

### RSVP-TE

Traffic Engineering (TE): the ability to control where and how traffic is routed, independent of best path calculation of routing protocol.
Reason: prevent congestion, manage capacity, prioritize different services

Two mpls routing protocols: LDP, RVSP-TE

A network can use both: LDP for MPLS VPN, RSVP-TE for traffic engineering feature

![mpls_rsvp_te_ldp](../images/mpls_ldp_rsvp_te.png)

Image source: https://archive.nanog.org/sites/default/files/tuesday_tutorial_steenbergen_mpls_46.pdf

How roughly RSVP-TE works:

- Each LSP is assigned a bandwidth value
- Using [constrained routing](https://en.wikipedia.org/wiki/Constrained_Shortest_Path_First) (routing that excludes path that fails to meet the constraints), RSVP-TE takes the shortest path with enough bandwidth
- LSB may be deined if there is no enough bandwidth

Wait, how to determine the LSB bandwidth?

- Offline calculation
- Auto-bandwidth: calculated on the router by periodically measuring the traffic crossing the LSP

How MPLS auto-bandwith works:

- every x second, measure bandwidth over an LSP
- after several sample, measure the statistics
- if the change is greater than the threshold, the new bandwidth value is re-signaled across RSVP

# MPLS data transport services: MPLS VPN

Sources:

- https://en.wikipedia.org/wiki/MPLS_VPN
- https://en.wikipedia.org/wiki/Layer_2_MPLS_VPN
- https://en.wikipedia.org/wiki/Virtual_routing_and_forwarding
- https://www.rogerperkin.co.uk/ccie/mpls/cisco-mpls-tutorial/
- https://networklessons.com/mpls/mpls-layer-3-vpn-explained
- https://en.wikipedia.org/wiki/Multiprotocol_BGP
- https://ccieblog.co.uk/mpls/difference-between-the-rd-and-rt

MPLS VPN is VPN that uses MPLS to operate (not IPSec). 3 types of MPLS VPN: Point to point (pseudowire), L2 MPLS VPN (VPLS), L3 MPLS VPN (VPRN)

1. Pseudowire (point-to-point)

Emulated _L2 point-to-point_ circuit delivered over MPLS. Used by SCADA master controller related stuffs.

2. L2 MPLS VPN (VPLS)

- Builds an _L2 multipoint_ switching service over MPLS.
- Can handle [BUM traffic](https://en.wikipedia.org/wiki/Broadcast,_unknown-unicast_and_multicast_traffic#:~:text=BUM%20traffic%20refers%20to%20that,to%20the%20intended%20destination%20only.)
- Typically used to route traffic between > 2 data center locations. It's like building L2 VLANs between sites.
- The purpose of VPLS is like EVPN, but EVPN is newer and better

1. L3 MPLS VPN (VPRN)

An IP based VPN. L3 MPLS VPN uses Virtual Routing & Forwarding (VRF) to segment routing tables for each customer utilizing the service. The VRF is only on the PE router, not on the P. With VRF, the router has multiple instance of routing tables. It's the L3 equivalent to the L2 VLAN (see previous explanation about L2 MPLS VPN).

Since two customers of the L3 MPLS VPN may have the same IP address spaces the PE router may get confused when routing the packet. Example:

![conflict_ip](https://cdn.networklessons.com/wp-content/uploads/2015/08/xmpls-vpn-bgp-without-route-distinguisher-1024x375.png.pagespeed.ic.9bqhWkLymz.webp)

Image source: https://networklessons.com/mpls/mpls-layer-3-vpn-explained

To make it unique, we prepend a **Route Distinguisher (RD)** to the IP prefix of each customer. RD is 64 bit long, with a format of ASN:NN. ASN is the ISP ASN and NN is the unique number for each customer. The RD just makes sure that the route is unique in the VPNv4 BGP table.

```
  [RD]  | IPv4 prefix
 64 bit     32 bit
```

The combination of RD and the IP prefix is called VPNv4 route. VPNv4 is an address family of MP-BGP. The VPNv4 route will be advertised by **Multiprotocol BGP (MP-BGP)**. MP-BGP is an extension of BGP that allows different types of address to be distributed. The UPDATE of MP-BGP has a new Network Layer Reachability Information (NLRI) format that has these attributes: RD, IPv4 prefix, next hop, VPN label.

The RD is just to make sure the route is unique on the table. **Route Target (RT)** is like a tag that defines which prefixes get imported and exported on the PE routers. In other words, RT imports and exports routes. RT is put on the BGP *extended community attribute*.

When a packet from a customer enters the PE router, the ingress PE imports the RT. The egress PE router exports the RT to associate the tag with the customer VRF. Example:

```
vrf definition cust_x
 rd 1:1
 route-target import 100:100
 route-target export 100:100

int fa0/0
 description connection to Customer A Birmingham Site
 ip vrf forwarding cust_x
```

Read more about RD and RT here: https://ccieblog.co.uk/mpls/difference-between-the-rd-and-rt

# MPLS Fast Reroute (FRR)

- Improves convergence during a failure by pre-calculating backup paths for potential link/node failures
- So, the next best path is calculated and stored in the router's FIB
- Link and node failures can be protedted
- 2 ways to provide LSP protection:
  - One-to-one protecion (detour)
  - Many-to-one protection (facility)

# Appendix

## Leaking route with MP-BGP

Source: https://networkdirection.net/articles/routingandswitching/mp-bgp/leakingrouteswithmp-bgp/
