# Common question 1: connect to a network, open a website

> Explain what happens when you connect to a network via wifi/ethernet cable and open example.com

### Part 1: initialization (obtaining IP address, DNS address, default gateway)

1. My computer sends a **DHCP request message** to the router it connects to. The DHCP message is encapsulated to the UDP and IP.
   1. src: 0.0.0.0 (my computer does not have IP address yet)
   2. dst: 255.255.255.255 (broadcast address)
2. The encapsulated DHCP message is encapsulated within an **Ethernet** frame (layer 2).
   1. src: my computer's MAC address (like 00:16:D3:23:68:8A)
   2. dst: FF:FF:FF:FF:FF:FF (broadcast)
3. Any packet that goes to a switch will be forwarded to all ports of switch because it does not know about IP network
4. When the DHCP server (let's say in this case it's also in the router it connects to) receive the DHCP request message, it will allocate one address from the CIDR block (let's say 192.168.10.0/24). Then, the DHCP server returns a **DHCP ACK message** containing the IP address allocated, DNS IP address, IP address for the default gateway, and subnet block/net mask.
5. When my computer gets the DHCP ACK message, it will use the IP address returned in this ACK message as my computer's IP address and save all other IPs returned in the **IP forwarding table**. We can see the IP forwarding table by executing `sudo route -n`. 
6. My computer will send all datagram with destination address outside the subnet block to the default gateway.

### Part 2: DNS and ARP

7. When my computer opens example.com (with a browser or curl or whatever), it needs to make a DNS request first to know the IP address of example.com
8. My computer makes a **DNS query** message, wraps it in UDP segment, IP packet (src: my IP address, dst: DNS IP address), then Ethernet frame (src: my MAC address, dst: ???). Since the DNS IP address is outside the subnet block, it will send it to the default gateway. So the Ethernet frame destination will be the MAC address of the default gateway. My computer knows the IP address of the default gateway but does not know the MAC address yet.
9. To find out the default gateway MAC address, it makes an **ARP query**, asking *"who is $(default IP address)?"*
   1.  src: my MAC address
   2.  dest: broadcast (FF:FF:FF:FF:FF:FF)
10. The default gateway will reply with **ARP reply** telling it's him and give the MAC address inside the ARP reply message. It saves the associated MAC address to the IP address until the the timeout is reached, it is removed from the ARP table, and the ARP request is made again.
11. Then my computer can send the DNS query to the default gateway.

### Part 3: Routing the packet to the DNS server

12. When the default gateway receives the DNS query packet, it will forward the packet to the border router of the ISP.
13. The border router is actually part of the ISP backbone network. It is a network owned by the ISP. This network consists of a bunch of routers. This network runs a Interior Gateway Protocol (IGP) such as OSPF, RIP, EIGRP, IS-IS, etc. These routers, if connected to another backbone network, can also be BGP routers. See [routing protocol](routing_protocol.md).
14. Typically, the IP address of the DNS returned by the DHCP server is the local DNS server. It acts as a cache as well as *DNS recursive resolver*. If it knows the IP address of example.com, it returns the IP address within a DNS reply message to the DNS resolver (client). Otherwise, it will recursively query the example.com to the *authoritative DNS*. See appendix A.

### Part 4: TCP and HTTP

15. My computer tries to build a TCP session by initializing TCP handshake. First, it sends a **TCP SYN**.
    1. IP addr src: my IP addr
    2. MAC addr src: my MAC addr
    3. IP addr dest: example.com's IP address
    4. MAC addr dest: default gateway MAC address
16. TCP SYN travels through the ISP backbone network, probably goes to another AS network, connected via Tier-1 or IXP, etc. IGP and EGP may be involved. See [this picture](https://en.wikipedia.org/wiki/Tier_1_network#/media/File:Internet_Connectivity_Distribution_&_Core.svg)
17. Example.com's server receives TCP SYN, replies it with TCP SYNACK
18. My computer sends TCP ACK. If my computer does not reply with ACK, it can go wrong. See appendix C.
19. My computer sends a HTTP GET request, server replies.
20. See appendix E for HTTPS/TLS.

# Common question 2: calculating subnet

> how many address available for 192.168.0.0/24

Format: IP/subnet mask

```
all address for that subnet mask = 2 ^ (32 - subnet mask)

all usable address for that subnet mask = 2 ^ (32 - subnet mask) - 2
```

- The first address is the network address
- The last one is broadcast

So, for that question (192.168.0.0/24)

- All addresses = 2 ^ (32 - 24) = 256
- All usable address (excluding network address and broadcast) = 254
- Network address = 192.168.0.0
- Broadcast address = 192.168.0.255
- Usable = 192.168.0.1 - 192.168.0.254

## Appendix A: DNS

#### How DNS is structured

```
client (requesting host) --- local DNS server --- root DNS server
                                          |
                                          |------ TLD DNS server
                                          |
                                          |------ authoritative DNS 
```

Client asks the local DNS server for example.com. If it does not know:

- Root DNS server knows where the Top Level Domain (TLD) DNS server for .com or .edu or .org or whatever.
  - There are 13 logical instances of root DNS server. But they are anycast, so there are > 1000 instances of them [[wiki](https://en.wikipedia.org/wiki/Root_name_server)]
- TLD DNS knows the authoritative DNS for example.com
- Authoritative DNS is the source of truth for the IP address of example.com

#### Why we need recursive DNS (local DNS)

1. To avoid the high load on the authoritative DNS, the local DNS can cache the IP-name translation
2. The local DNS can be put closer to clients: shorter round trip time

Google, Cloudflare, etc offers DNS recursive resolver (Google with 8.8.8.8, etc). We can put it in `resolve.conf`. But why do they offer this?

- The local DNS software provided by ISP is slow
- Privacy violation issue: ISP can sell the history of the browsing history of clients by selling DNS query data. Well..this can be a problem with Google's or Cloudflare's DNSes too. But they say they're not gonna do that. ISP does not say anything.
- Some application require the real IP address of the clients to perform GeoDNS mapping. With recursive resolver, the GeoDNS server sees the recursive resolver. The workaround for this is the DNS ECS which brings the clients' subnets to the recursive queries. But many ISP do not implement this. Google's DNS implement this.

#### Security problem of local DNS

DNS Kaminsky cache poisoning: when the local DNS is performing recursive query, an attacker tries to inject the reply to the local DNS so that the local DNS returns the wrong IP address to the clients. This can be *somewhat* mitigated by randomizing the use of source port of the DNS recursive query so that the response with the wrong source port will be rejected. But it just makes the attack harder, not completely secured. The use of DNSSEC which involves signature on the response is more secure, but harder to manage on a large scale.

Read more here http://unixwiz.net/techtips/iguide-kaminsky-dns-vuln.html

## Appendix B: IPv4 vs IPv6

Advantage of IPv6 over IPv4:

1. IPv4 is 32 bit long, while IPv6 is 128 bit long. IPv6 is very far way from exhaustion
2. IPv4 requires manual or DHCP for addressing. IPv6 requires manual or autoconfiguration, which is less complex than DHCP.
3. IPv4 requires NAT to prevent exhaustion, IPv6 does not need it.

So why we don't use the IPv6 everywhere? It's because it's not backward compatible to IPv4. Therefore, upgrading requires upgrading all IP-based things in the network, which is too many and very hard.

## Appendix C: TCP

TODO

- What can go wrong with TCP handshake: SYNRECV (TCP syn flood attack)
- TCP flow control
- TCP congestion control
- Segmentation offloading

## Appendix D: the flow of a packet in the kernel

https://wiki.linuxfoundation.org/networking/kernel_flow

# Appendix E: TLS handshake

Sources: 

- https://hpbn.co/transport-layer-security-tls/
- https://security.stackexchange.com/questions/6290/how-is-it-possible-that-people-observing-an-https-connection-being-established-w
- https://security.stackexchange.com/questions/20803/how-does-ssl-tls-work
- https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
- https://blog.cloudflare.com/tls-nonce-nse/
- https://crypto.stackexchange.com/questions/3965/what-is-the-main-difference-between-a-key-an-iv-and-a-nonce
- https://crypto.stackexchange.com/questions/25885/why-does-tls-do-authenticate-then-encrypt-instead-of-encrypt-then-authenticate
- https://crypto.stackexchange.com/questions/202/should-we-mac-then-encrypt-or-encrypt-then-mac

> Warning: Oversimplified version

![tls_handshake](https://hpbn.co/assets/diagrams/b83b75dbbf5b7e4be31c8000f91fc1a8.svg)

Image source: https://hpbn.co/transport-layer-security-tls/

1. TCP SYN
2. TCP SYNACK
3. TCP ACK (end of TCP handshake)
4. TLS ClientHello (client -> server)
   1. Brings TLS versions that the client can do
   2. List of supported ciphersuites
5. TLS ServerHello (server -> client)
   1. Brings a certificate
   2. (Optional) requests for client's certificate (for mutual TLS)
6. Client validates certificates:
   1. Is the Common Name (CN) is the same as the IP address it is sent from (check DNS)?
   2. Is it expired?
   3. Is it signed by something client trusts (check issuer)?
7. Client initiates the *key derivation process*. For example, it can use Diffie-Hellman Key Exchange. Given public `g`, public `p`, and secret `a`, the client makes `A = g^a mod p`. `A` is called Pre-master secret key. Client sends the `A`, `MAC(A)`, encrypted with the server public key taken from the server certificate.
   1. At the same time, server with a secret `b` is making `B = g^b mod p`.
8. Server receives `A`. Server computes the symmetric session key `S = A^b mod P`. Server sends `B` to client.
9. Client computer the symmetric session key by `S = B^a mod p`
10. All communication in this TLS session is encrypted and MACed using this `S` symmetric session key.
    1.  TLS 1.3 uses encrypt-then-MAC

Oversimplification:

- MAC = Hash(symmetric key || message)
- Signature = E_privkey(Hash(message))