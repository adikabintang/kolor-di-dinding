# VRRP

Sources:

- https://networklessons.com/cisco/ccie-routing-switching/introduction-gateway-redundancy/
- https://en.wikipedia.org/wiki/Virtual_Router_Redundancy_Protocol
- https://www.redhat.com/sysadmin/ha-cluster-linux
- https://www.redhat.com/sysadmin/keepalived-basics

```
           internet
            /    \
---------  /      \ -----------home/office/data center----
    ip X  R1       R2  IP Y
           \      /
            \    /
             host
```

There are 2 routers for the host inside home/office/data center to connect to the internet. This is to provide redundancy; so that if one fails, the other can do the backup. For example, if the host uses IP X as the default gateway, the traffic from host to the internet will go through R1. With redundancy, we want to have R2 with IP Y as the back up. But, it's too cumbersome if the host's default gateway needs to be reconfigured every time the main router fails, and that takes time to configure too.

What we can do is to have a virtual gateway that represents routers R1 R2.

```
           internet
            / |  \
---------  /  |   \ -----------home/office/data center----
    ip X  R1--VR--R2  IP Y
           \  |   /
            \ |  /
             host
```

The virtual router VR has IP address VR. The host is configured to use IP address VR as the default gateway. If the main real physical router is R1, then the traffic will go to R1. If R1 fails, traffic goes to R2. But all of this is transparent. The host still sticks the default gateway IP address to VR.

The protocol for this mechanism is called Virtual Router Redundancy Protocol (VRRP).

## How VRRP works

A virtual router must use MAC address 00-00-5E-00-01-XX, the last XX is the virtual router ID. The ID is 1-255, and the 255 is for master and 1-254 is for the backup. Basically, the highest ID is the master. The ARP request for the virtual IP address will return this MAC address.

The physical routers communicate with each other using a multicast IP address 224.0.0.18 port 112. Master periodically sends advertisement to other routers to tell them that it is still alive. if after 3 times the backups do not get anything, they assume the master is down. Then, the next step is the leader election to select the master router.

For Linux server, we can use [Keepalived](https://www.keepalived.org/) to configure the VRRP. FYI, Keepalived can also be used to configure IPVS (L4 load balancer in Linux, not related to VRRP, though).

FRRouting supports [VRRP](http://docs.frrouting.org/en/latest/vrrp.html) (for Linux-based routers).
