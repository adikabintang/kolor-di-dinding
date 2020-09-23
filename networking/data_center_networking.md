# Intro to data center (DC) networking

Credits:

- [Technologies and protocols for data center and cloud networking](https://ieeexplore.ieee.org/document/6588646)
- [layer 3 switching vs router](https://community.fs.com/blog/layer-3-switch-vs-router-what-is-your-best-bet.html)
- [Cloud Native Data Center Networking](https://cumulusnetworks.com/lp/cloud-native-data-center-networking/)

![dc_network](../images/dc_network.png)

- Backbone: MPLS
- vswitch: virtual switches, virtualized in the hosts inside the rack
- ToR: hardware, may support VLAN
- DC gateway: to outside. connected to PE router
  - virtual routing, IP-VPN/L2 VPN provider edge
  - may use VRRP for redundancy

It should be noted that the "switch" inside the data center does not only mean L2 switch, but it can also be a L3 switch (read [here](https://community.fs.com/blog/layer-3-switch-vs-router-what-is-your-best-bet.html)). Both can do the L3 routing such as OSPF, BGP, RIP, etc. The main difference between L3 swithces and routers:

- Routers usually run on processors, L3 switches run on ASIC (faster)
- Routers can do NAT, L3 switches cannot do it
- Routers can have WAN interfaces, L3 switches do not have it

L3 switch in a DC has processors and switching silicon (ASIC). The packet forwarding is not handled by processor, thus, the Network Operating System (NOS) does not handle the packet forwarding. The packet forwarding is handled by the switching silicon.

## Intra-DC

![inside_dc](../images/inside_dc.png)

Topology: spine-leaf (or clos). The above image is only one example of scaling clos topology with super spines. See the [Cloud Native Data Center Networking](https://cumulusnetworks.com/lp/cloud-native-data-center-networking/) book for more info.

The best practice is to use BGP with MRAI set to 0 inside the data center with this AS numbering scheme:

- All leaves has different ASN
- Spines within the same pod have the same ASN, but different ASN for different pod
- Super spines have the same ASN

This way of AS numbering avoids BGP path hunting. What is BGP path hunting?

BGP path hunting is a tendency of BGP to hunt a path, making it longer and longer, before it converges. Typically this happens after a BGP prefix withdrawal. The main culprit is the 30 seconds MRAI. The AS numbering as the above rule alleviates the BGP path hunting because BGP will not forward advertisement that comes from its' own AS number. Another thing to do to avoid path hunting is to set the MRAI to 0 second. Read more about path hunting on [noction.com](https://www.noction.com/blog/bgp-path-hunting) and [Paul Jakma's blog](https://paul.jakma.org/2020/01/21/bgp-path-hunting/).

## Inter-DC

https://sites.google.com/site/amitsciscozone/home/data-center/data-center-interconnect-part-1

BGP IP MPLS. MPLS over GRE? read https://sites.google.com/site/amitsciscozone/home/data-center/data-center-interconnect-part-1

https://www.networkcomputing.com/networking/network-automation-using-python-bgp-configuration

https://www.batfish.org/

Just a note:

- MPLS separates route in L2.5
- GRE in L3
- VRF just builds a virtual table inside a router
