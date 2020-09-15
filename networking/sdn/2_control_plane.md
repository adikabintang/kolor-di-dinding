# The control plane

Source: coursera

## Control plane basics

```
controller ---> openflow switch (contains flow table)
```

1. OpenFlow controller communicaes to the openflow switch (can be over a secure channel). The logic is executed at controller. The switch is now only forwards packet, not building the flow table, since this is done by the controller.
2. Switch components:
   1. Flow table: performs packet lookup. If there is a match, do the actions as the table says. *If no match, send the traffic to the controller*.
   2. The 12-tuple is used for the flow table lookup: switch port, MAC src & dst, Eth type, VLAN ID, IP src & dst, TCP spor & dport, VLAN priority, ToS.

SDN controller examples: NOX, POX (easiest), Ryu, OpenDaylight (complex, steep learning curve).
