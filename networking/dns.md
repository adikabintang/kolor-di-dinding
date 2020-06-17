# DNS

## How DNS is structured

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

## Why we need recursive DNS (local DNS)

1. To avoid the high load on the authoritative DNS, the local DNS can cache the IP-name translation
2. The local DNS can be put closer to clients: shorter round trip time

Google, Cloudflare, etc offers DNS recursive resolver (Google with 8.8.8.8, etc). We can put it in `resolve.conf`. But why do they offer this?

- The local DNS software provided by ISP is slow
- Privacy violation issue: ISP can sell the history of the browsing history of clients by selling DNS query data. Well..this can be a problem with Google's or Cloudflare's DNSes too. But they say they're not gonna do that. ISP does not say anything.
- Some application require the real IP address of the clients to perform GeoDNS mapping. With recursive resolver, the GeoDNS server sees the recursive resolver. The workaround for this is the DNS ECS which brings the clients' subnets to the recursive queries. But many ISP do not implement this. Google's DNS implement this.

## Security problem of local DNS

DNS Kaminsky cache poisoning: when the local DNS is performing recursive query, an attacker tries to inject the reply to the local DNS so that the local DNS returns the wrong IP address to the clients. This can be *somewhat* mitigated by randomizing the use of source port of the DNS recursive query so that the response with the wrong source port will be rejected. But it just makes the attack harder, not completely secured. The use of DNSSEC which involves signature on the response is more secure, but harder to manage on a large scale.

Read more here http://unixwiz.net/techtips/iguide-kaminsky-dns-vuln.html

## Debugging (TODO)

dig

nslookup
