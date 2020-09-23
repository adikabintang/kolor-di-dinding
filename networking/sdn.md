# Intro to SDN

Sources:

- https://networklessons.com/cisco/ccna-routing-switching-icnd2-200-105/introduction-to-sdn-software-defined-networking/
- https://www.youtube.com/watch?v=WEdDQsyXT6E
- https://www.youtube.com/watch?v=DiChnu_PAzA
- https://networklessons.com/cisco/ccna-routing-switching-icnd2-200-105/introduction-to-sdn-opendaylight

## Traditional Networking

All in a router/switch: control plane, data plane management plane.

- Control plane: Running and building IP routing table, MAC table, ARP table, running STP. 
- Data plane: forward packet, dropping traffic (because of access lists with netfilter, for example)
- Management plane: telnet/ssh to provide CLI, SNMP, Netconf

In other words, control plane is the logic for controlling forward behavior. Data plane forwards traffic according to control plane logic.

![traditional](https://cdn.networklessons.com/wp-content/uploads/2014/10/xcontrol-vs-data-plane.png.pagespeed.ic.wAd7DuCXqu.webp)

Image source: https://networklessons.com/cisco/ccna-routing-switching-icnd2-200-105/introduction-to-sdn-software-defined-networking/

## Software Defined Networking (SDN)

With SDN, the control plan is *logically* centralized, named the SDN controller. The routers/switches only have the data plane. The SDN controller feeds the data plane to the forwarding devices via protocols like OpenFlow. Illustration:

![sdn_illustration](https://cdn.networklessons.com/wp-content/uploads/2016/09/xsdn-controller-data-plane-switches.png.pagespeed.ic.gi8AY0r2-_.webp)

Image source: https://networklessons.com/cisco/ccna-routing-switching-icnd2-200-105/introduction-to-sdn-software-defined-networking/

SDN controller has 2 interfaces: northbound and southbound interface.

![interfaces](https://cdn.networklessons.com/wp-content/uploads/2016/09/xsdn-controller-northbound-southbound.png.pagespeed.ic.JgyV1neHAT.webp)

Image source: https://networklessons.com/cisco/ccna-routing-switching-icnd2-200-105/introduction-to-sdn-software-defined-networking/

SDN controller feeds the forwarding plane (routers/switches) through the southbound interface. One of the protocol that runs on the southbound interface is OpenFlow.

The northbound interface is for accessing the SDN controller. One of the protocol for the northbound interface is RESTConf. The network automation software or GUI for admins access the SDN controller via the northbound interface. For example, this interface provides list of info from all network devices, status, make a new VLAN, show topology, configure IP address, routing, etc.

Example of application:

In a data center, everytime a new VM instance is created, it triggers a software for automation. This software speaks to SDN controller to configure the network so that this VM instance can operate. The things that it can ask might be adding IP address to the instance, advertising route for this VM, setting VLAN for this machine, etc.

One of the most popular SDN controller framework is OpenDaylight. On the southbound, OpenDaylight supports OpenFlow. It also supports RESTConf for the northbound itnerface. We can use mininet to experiment with it [TODO].

Note: SDN is not that successful for data center because of its complexity. However, Google uses SDN for their DC. (source: https://cumulusnetworks.com/lp/cloud-native-data-center-networking/).

SDN is more well used for WAN.
