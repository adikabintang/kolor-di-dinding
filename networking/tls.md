# TLS handshake

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
9. Client computes the symmetric session key by `S = B^a mod p`
10. All communication in this TLS session is encrypted and MACed using this `S` symmetric session key.
    1. TLS 1.3 uses encrypt-then-MAC

Oversimplification:

- MAC = Hash(symmetric key || message)
- Signature = E_privkey(Hash(message))
