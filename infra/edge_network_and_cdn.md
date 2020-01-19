Reading material:

- https://blogs.dropbox.com/tech/2018/10/dropbox-traffic-infrastructure-edge-network/
- https://blogs.dropbox.com/tech/2017/06/evolution-of-dropboxs-edge-network/
- https://blogs.dropbox.com/tech/2020/01/intelligent-dns-based-load-balancing-at-dropbox/
- https://blog.paessler.com/cdn-architectures 
- https://networkencyclopedia.com/point-of-presence-pop/ 

# Edge Network, CDN, Global Server Load Balancer

Global Server Load Balancer (GSLB) is the mechanism of load balancing traffic in a multi-cloud environments so that the traffic can be directed to the intended server. For example, GSLB can be used to direct the traffic from the client to the nearest Content Delivery Network (CDN) server which is inside a Point of Presence (PoP). PoP is a point (let's say, a very small data center consisting of some small server machines and other sets of network equipment) to which users of the ISP is connected to.

There are two ways to implement GSLB: **BGP anycast** and **GeoDNS**.

Anycast is a network addressing and routing methodology in which a single address has multiple routes to many endpoint destinations [[wikipedia](https://en.wikipedia.org/wiki/Anycast)]. With BGP anycast, all PoP advertises the same IP address. All requests from clients will be directed to the nearest PoP, thanks to BGP routing.

- Anycast load balancing is sometimes not optimal in directing the traffic to the nearest PoP (although rarely happens)
- It limits the control over traffic

In GeoDNS approach, each PoP has different IP address. GeoDNS will return the IP address of the PoP based on the geo location of the clients' IPs.

- GeoDNS gives full control over the traffic
- DNS TTL can be problematic
- In some cases, GeoDNS fails to locate the real geo location of the client. Consider this scenario: client makes a DNS query to the DNS of the ISP. This DNS does not have the answer. So, it makes a request to the authoritative DNS. This way, the authoritative DNS receives the IP address of the ISP's DNS IP instead of the client's IP.

BGP anycast and GeoDNS can be made hybrid. Read [how Dropbox does this](https://blogs.dropbox.com/tech/2018/10/dropbox-traffic-infrastructure-edge-network/).

Dropbox uses latency-based DNS routing for their CDN [[blogs.dropbox.com](https://blogs.dropbox.com/tech/2020/01/intelligent-dns-based-load-balancing-at-dropbox/)].