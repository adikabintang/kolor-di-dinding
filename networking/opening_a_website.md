> Explain what happens when you connect to a network via wifi/ethernet cable and open example.com

# Part 1: initialization (obtaining IP address, DNS address, default gateway)

1. My computer sends a **DHCP request message** to the router it connects to. The DHCP message is encapsulated to the UDP datagram, IP packet, then to MAC frame.
   1. IP layer:
      1. src: 0.0.0.0 (my computer does not have IP address yet)
      2. dst: 255.255.255.255 (broadcast address)
   2. Layer 2:
         1. src: my computer's MAC address (like 00:16:D3:23:68:8A)
         2. dst: FF:FF:FF:FF:FF:FF (broadcast)
2. When the DHCP server (let's say in this case it's also in the router it connects to) receives the DHCP request message, it will allocate one address from the CIDR block (let's say 192.168.10.0/24). Then, the DHCP server returns a **DHCP ACK message** containing the IP address allocated, DNS IP address, IP address for the default gateway, and subnet block/net mask.
3. When my computer gets the DHCP ACK message, it will use the IP address returned in this ACK message as my computer's IP address and save all other IPs returned in the **IP forwarding table**. We can see the IP forwarding table by executing `sudo route -n`. 
4. My computer will send all datagram with destination address outside the subnet block to the default gateway.

# Part 2: DNS and ARP

7. When my computer opens example.com (with a browser or curl or whatever), it needs to make a DNS request first to know the IP address of example.com
8. My computer makes a **DNS query** message, wraps it in a UDP segment, IP packet (src: my IP address, dst: DNS IP address), then Ethernet frame (src: my MAC address, dst: ???). Since the DNS IP address is outside the subnet block, it will send it to the default gateway. So the Ethernet frame destination will be the MAC address of the default gateway. My computer knows the IP address of the default gateway but does not know the MAC address yet.
9. To find out the default gateway MAC address, it makes an **ARP query**, asking *"who has $(default IP address)?"*
   1. src: my MAC address
   2. dest: broadcast (FF:FF:FF:FF:FF:FF)
10. The default gateway will reply with **ARP reply** telling it's him and give the MAC address inside the ARP reply message. It saves the associated MAC address to the IP address until the the timeout is reached. When the lifetime is reached, the MAC address is removed from the ARP table, and the ARP request is made again.
11. Then my computer can send the DNS query to the default gateway.

# Part 3: Routing the packet to the DNS server

12. The local router that we have is connected to the Point of Presence (PoP) of the ISP. PoP is a place to connect users to the backbone network. Inside PoP, there are many routers, switches, etc.
13. When the default gateway receives the DNS query packet, it will forward the packet to the border router (inside PoP) of the ISP. The traffic will then be forwarded to the backbone network.
14. Backbone network is the main network owned by an ISP. This network runs a Interior Gateway Protocol (IGP) such as OSPF, RIP, EIGRP, IS-IS, etc., as well as iBGP and eBGP (if connected to other network). See [routing protocol](routing_protocol.md).
15. Typically, the IP address of the DNS returned by the DHCP server is the local DNS server. It acts as a cache as well as *DNS recursive resolver*. If it knows the IP address of example.com, it returns the IP address within a DNS reply message to the DNS resolver (client). Otherwise, it will recursively query the example.com to the *authoritative DNS*. See appendix A.

# Part 4: TCP and HTTP

15. My computer tries to build a TCP session by initializing a TCP handshake. First, it sends a **TCP SYN**.
    1. IP addr src: my IP addr
    2. MAC addr src: my MAC addr
    3. IP addr dest: example.com's IP address
    4. MAC addr dest: default gateway MAC address
16. TCP SYN travels through the ISP backbone network, probably goes to another AS network, connected via Tier-1 or IXP, etc. IGP and EGP may be involved. See [this picture](https://en.wikipedia.org/wiki/Tier_1_network#/media/File:Internet_Connectivity_Distribution_&_Core.svg)
17. Example.com's server receives TCP SYN, replies it with TCP SYNACK
18. My computer sends TCP ACK. If my computer does not reply with ACK, it can go wrong. See [more on TCP](tcp.md).
19. My computer sends a HTTP GET request, server replies.
20. See appendix E for HTTPS/TLS.

References:

- https://computer.howstuffworks.com/internet/basics/internet-infrastructure1.htm
- (book) computer networking a top-down approach
- (book) Advanced Network Programming – Principles and Techniques: Network Application Programming with Java (Computer Communications and Networks) -> https://books.google.fi/books?id=3qq8BAAAQBAJ&pg=PA24&lpg=PA24&dq=my+router+is+connected+to+isp+pop+or+backbone&source=bl&ots=FxcPrIh3p7&sig=ACfU3U2nQABy2KWj2X1LcxyRG_DYFz_-mw&hl=en&sa=X&ved=2ahUKEwjZ_NCd7qLqAhVRAxAIHU8oA3YQ6AEwCXoECAkQAQ#v=onepage&q=my%20router%20is%20connected%20to%20isp%20pop%20or%20backbone&f=false