# Equal Cost Multipath (ECMP)

Sources:

- https://www.youtube.com/watch?v=KICp-9yXOT0
- https://docs.cumulusnetworks.com/cumulus-linux-41/Layer-3/Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/
- https://support.huawei.com/enterprise/en/doc/EDOC1100086965

When there are multiple same cost routes to the same destination, we can have a per-flow load balancing (per-TCP or UDP flow) flow to avoid the packet re-ordering. Set this in `sysctl` (`sys.net.ipv4.fib_multipath_hash_policy=1`). Read more here: https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt

The idea is something like:

```python
# remember: protocol type is in IP header -> tcp/udp
key = (src ip, dest ip, protocol type, src port, dest port)
n_backend = 6
fwd_interface = hash(key) % n_backend
```

As the above looks like a hash table, it suffers from the problem when adding/removing `n_backend`. We should use "resilient hash", which may utilize consistent hashing as its component.

See above: it uses src port and destination. ICMP does not have these. So, if we need to build a testing tool like ping for an infrastructure that has ECMP, use UDP (like Facebook's [NetNORAD](https://engineering.fb.com/networking-traffic/netnorad-troubleshooting-networks-via-end-to-end-probing/))

## Problem: hash polarization

What is it: see the picture below.

![hash_polarization](https://download.huawei.com/mdl/imgDownload?uuid=557f6af1a2984575ba9f56952b576b90.png)

Image source: https://support.huawei.com/enterprise/en/doc/EDOC1100086965

Now, if the ECMP happens at two levels of routers, and the first level and the second level yields the same hash output, it will not be load balanced on the second level. *This results in an unevenly load balanced traffic*.

In the picture, see the blue and yellow packet. the blue and yellow go to the first 2 egress interface. on the second switch, because the hash yields the same and the number of interfaces are also the same, the packet will go to the first 2 interfaces on the second switch. As a result, the second switch is not really doing the load balancing.

To mitigate hash polarization, each router must have unique seeds that can be used in the hash calculation so that the hash value will be different. This will work on TCP and UDP packet.
