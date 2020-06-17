# Security issues with ARP

- https://moodle.epfl.ch/pluginfile.php/2710119/mod_resource/content/2/ip1.pdf
- https://en.wikipedia.org/wiki/ARP_spoofing

ARP spoofing: attacker aims to associate its MAC address to the IP of the target, like the gateway, so that the traffic will flow through the attacker.

Mitigation:

- DHCP snooping: switch/wifi base station observes all DHCP traffic and remembers the mapping IP addr-MAC
- dynamic ARP inspection: switch filters all ARP and allows only valid answers

