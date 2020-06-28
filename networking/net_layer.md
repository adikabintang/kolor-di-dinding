# IP addressing

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

## IPv4 vs IPv6

Sources:

- https://moodle.epfl.ch/pluginfile.php/2710119/mod_resource/content/2/ip1.pdf
- https://en.wikipedia.org/wiki/IPv6

Advantage of IPv6 over IPv4:

1. IPv4 is 32 bit long, while IPv6 is 128 bit long. IPv6 is very far way from exhaustion
2. IPv4 requires manual or DHCP for addressing. IPv6 requires manual or autoconfiguration (SLAAC), which is less complex than DHCP.
3. IPv4 requires NAT to prevent exhaustion, IPv6 does not need it.
4. IPv6 is faster to process in router. Why:
   1. In IPv4, there is a checksum. When the router decrement the TTL, the checksum is re-computed.
   2. In IPv6, there is no checksum. The hop limit (=IPv4's TTL) is subtracted, the router does not have to re-compute the checksum. IPv6 just relies on checksum by L2 and L4 (checksum header on TCP/UDP) for integrity check.
5. IPsec is more welcomed: AH and ESP are implemented as IPv6 extension headers.

So why we don't use the IPv6 everywhere? It's because it's not backward compatible to IPv4. Therefore, upgrading requires upgrading all IP-based things in the network, which is too many and very hard.

1. the autoconfiguration of IPv6: Stateless Address Autoconfiguration (SLAAC). How? roughly:
   1. Host derive an IPv6 addr from MAC addr
   2. Host performs duplication test by sending a multicast packet
   3. Host tries to add gobally valid address by obtaining net prefix from routers if any present
2. But why there is DHCPv6? becuase SLAAC does not return the DNS address. DHCP gives the DNS address to the host. So DHCPv6 is stateless. So, SLAAC first, then do the DHCPv6 to get the DNS address.
3. Why there is a private IPv6 address? is there any local network? then we need NAT? but you say we don't need NAT. what?
   1. See page 59 of https://moodle.epfl.ch/pluginfile.php/2710119/mod_resource/content/2/ip1.pdf
   2. DHCP with prefix delegation. See that link. In short:
      1. ISP assigns the network prefix that the home/office/anything router can delegate to its devices. So to the ISP, the router's network is the network prefix that the ISP gives. this network prefix is the public addresses. So all devices behind the router will have public IPv6 address. But NATs might still be used for isolation: keep local addresses private.

TODO: learn IPv6 https://youtu.be/ck5bR1WlOo0?t=1454

# IP Multicast

Sources:

- https://en.wikipedia.org/wiki/IP_multicast
- https://networklessons.com/multicast/introduction-to-multicast
- http://cisco.num.edu.mn/CCNA_R&S1/course/module5/5.1.3.5/5.1.3.5.html#:~:text=As%20with%20the%20unicast%20and,%2D00%2D5E%20in%20hexadecimal.
- https://networklessons.com/multicast/multicast-ip-address-to-mac-address-mapping

Multicast is for sending to *some* members (like a group). IPv4 addresses for multicast are 224.0.0.0 to 239.255.255.255.

The receivers form a multicast group. The protocol to join the group is called Internet Group Management Protocol (IGMP).

The MAC addresses that associates with the IP multicast are 01:00:5e:00:00:00–01:00:5e:7f:ff:ff (remember, broadcast is FF:FF:FF:FF:FF:FF, and multicast does not use this). If the switch understands multicast, when receiving a packet with special multicast, the switch will forward to the group. If the router does not understand multicast, it will flood to all interface, and the NIC of the destination that will filter it (if the destination is not the member).

The IP-MAC translation in IP multicast is done locally. It involves converting a reserved multicast IP address to the reserved MAC address for multicast. The NIC is then configured with this MAC. Due to the bit difference, some multicast IP address can be associated with a single MAC address. See [networklessons.com](https://networklessons.com/multicast/multicast-ip-address-to-mac-address-mapping) for details.
