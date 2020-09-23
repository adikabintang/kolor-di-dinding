# GRE tunneling

source:

- https://networkdirection.net/articles/routingandswitching/gretunnels/
- https://www.youtube.com/watch?v=ytAqv7qHGyU&ab_channel=NetworkDirection

GRE: Generic Routing Encapsulation.

```
Edge Router 1 -- [core network] -- Edge router 2
```

We cannot do anything on the core network. Edge routers can be 2 separate office or data center.

We can build a GRE tunnel to connect edge router 1 and 2 "directly". It makes an encapsulation of L3 packet. One of the use cases is when the core network has IPv4 but we want to connect the network behind edge router 1 and 2 which is IPv6. Creating GRE involves making a virtual interface (VTI).
