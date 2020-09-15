# Intro to data center networking

Credits:

- [Technologies and protocols for data center and cloud networking](https://ieeexplore.ieee.org/document/6588646)
- [layer 3 switching vs router](https://community.fs.com/blog/layer-3-switch-vs-router-what-is-your-best-bet.html)
- 

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

