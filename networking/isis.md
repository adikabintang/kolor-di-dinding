# Intermediate System to Intermediate System (IS-IS)

Sources:

- https://en.wikipedia.org/wiki/IS-IS
- https://www.youtube.com/watch?v=o1k1TlxL5Dk
- https://forum.huawei.com/enterprise/en/why-do-many-isps-still-use-the-is-is-protocol-instead-of-the-ospf-protocol/thread/563137-863

- IGP
- Link state protocol, it floods link state information throughout the network (like OSPF)
- Uses Dijkstra for SPF calculation
- The de facto standard for service provider backbone networks
- Not based on IP, it's actually L2 protocol
- Integrated IS-IS supports IP
- Level 1 routing (intra-area): within an area
- Level 2 routing (inter-area): between areas
- Level 1-2 (both)

## OSPF vs IS-IS

- OSPF uses L3 packet to send routing information. OSPFv2 is for IPv4, OSPFv3 is for IPv6
  - IS-IS uses L2 to send routing information, that's why it's independent of the L3 addressing (can do IPv4 or IPv6)
- In OSPF, a interface belongs to an area. So, a router can be in 2 or more areas. This router is called Area Border Router (ABR).
  - In IS-IS, a router belongs to an area, not the interface. So a router is either level 1, level 2, or level 1-2.
- OSPF requires area 0, and inter-area traffic must pass area 0 to avoid loop. It's like spider web with area 0 in the middle. area 0 is also referred to as "backbone".
  - In IS-IS, the level 2 is the "backbone".
- IS-IS is less chatty (TODO: why?)
- OSPF messages are sophisticated.
  - IS-IS only uses [type-length-value (TLV)](https://en.wikipedia.org/wiki/IS-IS) messages

## Why IS-IS is used instead of OSPF

IS-IS is normally used in the backbone network of ISP/data centers (in the backbone network like this, ISIS+BGP is used, or even plus MPLS). OSPF is normally used in an office/campus settings.

- Since IS-IS uses the simple TLV, extending it is less complicated than extending OSPF. To support IPv6, just add a new type instead of rewriting the whole protocol like OSPF.
- IS-IS has less types of Link State Packet (LSP; the routing information message, can conain many TLVs) than OSPF's LSA. So, it's simpler, db structure is simpler, and computation resource usage is low. This can be advantageous for backbone network since it has a lot of traffic.
- IS-IS converges faster than OSPF because ... (TODO)
- ISIS scales better (TODO: why?)
