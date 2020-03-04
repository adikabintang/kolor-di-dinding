- [Basic Scalability Topics](#basic-scalability-topics)
  - [Vertical and Horizontal Scaling](#vertical-and-horizontal-scaling)
  - [Load balancing](#load-balancing)
    - [Methods for load balancing](#methods-for-load-balancing)
    - [Problem: stateful app on top of stateless protocol (HTTP)](#problem-stateful-app-on-top-of-stateless-protocol-http)
  - [Caching](#caching)
  - [Database replication](#database-replication)
  - [Database table partitioning](#database-table-partitioning)
  - [Database indexing](#database-indexing)
  - [Database normalization and denormalization](#database-normalization-and-denormalization)
  - [More database tips](#more-database-tips)
- [Asynchronism](#asynchronism)
- [Performance vs Scalability](#performance-vs-scalability)
- [Latency vs throughput](#latency-vs-throughput)
- [Availability vs Consistency](#availability-vs-consistency)
  - [Consistency pattern](#consistency-pattern)
  - [Availability patterns](#availability-patterns)
    - [Availability in parallel vs sequence](#availability-in-parallel-vs-sequence)
- [DNS](#dns)
- [Contenct Delivery Network (CDN)](#contenct-delivery-network-cdn)
- [Database](#database)
- [NoSQL](#nosql)
- [Cache](#cache)
- [Asynchronism](#asynchronism-1)

Source of my learning: https://github.com/donnemartin/system-design-primer

# Basic Scalability Topics

## Vertical and Horizontal Scaling

Basically, vertical: add more computing power (RAM, CPU, etc); horizontal: add more replica of the servers.

## Load balancing

### Methods for load balancing

Reading materials:

- [nginx](http://nginx.org/en/docs/http/load_balancing.html#nginx_load_balancing_with_ip_hash)

Methods:
- Round robin (can be weighted too)
- Least connected: assign the traffic to the least connected server

### Problem: stateful app on top of stateless protocol (HTTP)

Let's take a look at authentication methods for web applications: session based vs cookie based. This is useful as we will talk about load balancing techniques for these applications.

Useful reading resource:

- [Medium](https://medium.com/@sherryhsu/session-vs-token-based-authentication-11a6c5ac45e4)
- [Stackoverflow, invalidating JWT](https://stackoverflow.com/questions/21978658/invalidating-json-web-tokens)
- [JWT on wikipedia](https://en.wikipedia.org/wiki/JSON_Web_Token)

**Session based authentication**

- Client logs in to the server with the valid username and password. Server generates session id and gives the session id in the [HTTP cookie header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies). _Server stores the session id_.
- Client gets the session ID. Everytime the client makes HTTP request, the client adds the session ID in the cookie as the authentication method to the server.

See [Medium](https://medium.com/@sherryhsu/session-vs-token-based-authentication-11a6c5ac45e4) to see the diagram.

**Token based authentication**

Token based authentication using Json Web Token (JWT).

- Client logs in to the server with the valid username and password. Server generates token and gives the token to the client in HTTP Authentication heder. _Server DOES NOT store the token_
- The token is roughly a `identity, issued time, signature(identity, issued time)`
- Client gets the token. Everytime the client makes HTTP request, the client adds the JWT token as the authentication method to the server. How the server does this? The server:
  - Checks the expiry time of the token
  - Checks the signature of the token
- There are 2 ways to invalidate the token before it expires:
  - Tell the client to forget the token. Not so secure.
  - Black list the token by storing it until it expires. If there is a new request with a token, check this list. After expired, the token is just simply removed from the list because it is already unaccepted.
- There is a criticism saying that we should stop using JWT as a session [[crypto.net](http://cryto.net/~joepie91/blog/2016/06/13/stop-using-jwt-for-sessions/)]. TODO read.

See [Medium](https://medium.com/@sherryhsu/session-vs-token-based-authentication-11a6c5ac45e4) to see the diagram.

There are a few things noticeable from these 2 methods:

- The session based can fill up the memory of the server. In case of having multiple backends behind a load balancer, each request must go to the same backend service because only that backend stores the session ID. There are some approaches to solve this problem:
  -  Session ID is saved on one common DB, such as redis or MySQL. Any service can check the incoming session there. It's a quite expensive operation.
  -  Another session cookie is given by the load balancer, and the load balancer must remember the session must correspond to which backend service [[haproxy](https://www.haproxy.com/blog/load-balancing-affinity-persistence-sticky-sessions-what-you-need-to-know/)]. Let's say, there are 2 servers behind a load balancer. The load balancer will return session id 1 if the client signs in to server ip A, and it will return session id 2 if it signs in to server ip B. The load balancer will match the session 1 or 2 and redirects the traffic to the server accordingly.
-  JWT does not seem to have problems with load balancers.


## Caching

Some cache tools: redis, memcached

Use case example:

Cache `SELECT * FROM user WHERE id=5234` to redis (think like this: the query is the key and the result in the value in a hash table). The server will look at the redis first. If it does not exist, then it goes to the real DB. Redis placed the cache in RAM and it is a key-value store. So it is much faster than looking up at MySQL put in the HDD.

Cache replacement policy [[wikipedia]](https://en.wikipedia.org/wiki/Cache_replacement_policies):

- FIFO, LIFO, LRU, etc...

Cache control validation (max age, `no-cache`, etc) [[developer.google.com](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching)].

Caching HTML page can be done anywhere from the browser to the server.

More articles to read and note: https://www.lecloud.net/post/9246290032/scalability-for-dummies-part-3-cache

Two common ways to cache the DB:
- Commonly used way: caching the query and the result of the query, like the example above
- Instead of caching the DB query, application that makes the query cache the whole object that it builds. For example:
A class `Employee` with `name`, `address`, `phone_number` has its members filled by querying  different queries to 3 different tables. Instead of querying the DB query with the result, cache this whole object of the instantiated class.

Examples of things that are commonly cached:
- User session
- Static HTML
- Activity streams
- user<->friend relationships

Redis: more features.

Memcached: scales better.

## Database replication

Database replication aims to provide availability.

Read:

- https://www.brianstorti.com/replication/
- https://www.geeksforgeeks.org/data-replication-in-dbms/

## Database table partitioning

Read:

- https://www.sqlshack.com/database-table-partitioning-sql-server/

Database table partitioning aims to divide a large table to some smaller table. In this way, if the table is very large, we aim to have faster query since we are looking at smaller tables.

Two approaches:

- Horizontal

A table of `x` columns is divided into smaller tables with different number of columns but the same number of rows. For example: a table of column `username`, `password`, `date_of_birth`, `addres` is divided into 2 tables: the first one contains `username` and `password`, and the second one is `username`, `date_of_birth`, `addres`.

The horizontal scaling is useful to optimize data that is accessed with unbalanced frequency. For example, username and password in a database is more frequently accessed than date of birth. This way, we can provide faster SSD for SQL machine that stores table with username and password and have a cheaper, slower disk for the other one.

- Vertical

A table of `z` rows is divided into smaller tables with the same column but smaller number of rows. For example, a table of `z` columns and 1000 rows is divided into 10 tables, 100 rows each.

## Database indexing

What it is:

- https://www.guru99.com/indexing-in-database.html

How to do it:

- https://www.a2hosting.com/kb/developer-corner/mysql/using-indexes-to-improve-mysql-query-performance
- https://stackoverflow.com/questions/1156/how-do-i-index-a-database-column

How it works:

- https://stackoverflow.com/questions/1108/how-does-database-indexing-work

Basically, it's like this:

if we do `SELECT * FROM username WHERE name=asu_koe` on a `X` rows table, we do linear search. By indexing the `name` column, SQL server (MySQL or PostgreSQL) create an additional table with column `name` and `location of this row in the disk`. The `name` in the indexing table is sorted. When we search and the table has indices, the SQL can do faster searching algorithm to find the location of the row in the disk in the indexing table.

## Database normalization and denormalization

TODO

## More database tips

Article: https://www.lecloud.net/post/7994751381/scalability-for-dummies-part-2-database

- Database sharding [TODO]
- No `JOIN` in SQL (use MySQL like NoSQL). Joining is done in the application code

# Asynchronism

If we are working on blocking task, make it asynchronous. For example, in microservices, we can use Kafka or NATS for this purpose.

# Performance vs Scalability

https://github.com/donnemartin/system-design-primer#performance-vs-scalability

Performance problem: the system is slow for a single user.

Scalability problem: the system is fast for a single user, slow for many users.

# Latency vs throughput

Latency is the time it takes to complete some process.

Throughput is the number of completed tasks per unit of time.

In a synchronous process, we can say roughly `latency = 1 / throuput`.

In an asynchronous process, it is different. Consider the following examples:

A CPU core has small latency. A GPU core has bigger latency. If there is only a single task, or if the task can be done only synchronously, CPU is better. But if the tasks are many (or asynchronous), GPU wins becuase it has more cores (let's say CPU has 4 and GPU has 64) because the GPU's throughput is larger than the CPU's, although the latency of CPU is smaller than that of GPU (don't consider a single core, but as a chip).

This applies to distributed system as well. In order to scale, in general, we want to **build a high throughput system with an acceptable latency**.

# Availability vs Consistency

CAP theorem:

- Consistency (C): all the data in all nodes are consistent, the are the same; a read **must** return the latest data, otherwise it returns error (new data or nothing).
- Availability (A): all read queries **must** return something: data or error. The availability concept does not care if the data returned is the new one or not.
- Partition tolerant: if there is network failure and makes the node partition, the system still works.

CAP theorem says that we only can have 2 of 3 from CAP. Use cases:
- CP: if we need atomic read and write
- AP: log files storage. we can use "eventual consistency" for this.
  
## Consistency pattern

- Weak consistency: After a write, a read may or may not see it. For example, after a write, the reader is disconnected for a minute. The writer keeps writing. The reader, when connected again, cannot see what the writer has written for the last 1 minute. Example: VoIP and realtime multiplayer games.
- Eventual consistency: If we stop write new data, after some time, _eventually_ all replicas will agree on some value. Example: DNS.
- Strong consistency: After a write, the data is replicated synchronously. Example: RDBMS does this via atomic transaction.

## Availability patterns

- Fail-over
  - Active-passive (master-slave): 2 servers (can be more): 1 actively serves and 1 is passively wait. If the active dies, the traffic is redirected to the passive one.
  - Active-active (master-master): 2 servers (can be more): they all serve.
  - Disadvantages of both: need additional hardware to watch who is alive (for active-passive) or to load balance (for active-active); there is a potential of data loss when doing the fail-over
- Replication: see images below

**Master-slave replication**

![master-slave](https://camo.githubusercontent.com/6a097809b9690236258747d969b1d3e0d93bb8ca/687474703a2f2f692e696d6775722e636f6d2f4339696f47746e2e706e67)
Source: [Scalability, availability, stability, patterns](https://www.slideshare.net/jboner/scalability-availability-stability-patterns/)

**Master-master replication**

![master-master](https://camo.githubusercontent.com/5862604b102ee97d85f86f89edda44bde85a5b7f/687474703a2f2f692e696d6775722e636f6d2f6b7241484c47672e706e67)

Disadvantages:

- Potential loss of data if master fails
- The more slaves, the slower is the replication
- Add more hardware and complexity

### Availability in parallel vs sequence

If a system has multiple components, the availability of each component may or may not affect the availability percentage. Example:

2 components, in sequence, depends on one another, have 99% availability each. As a result, the total availability of the whole system is `99% * 99% = 98%`.

2 components in parallel, does not depend on one another, have 99% availability each. The total if the availability is still 99% -> `1 − (1 − 0.99) × (1−0.99) = 99%`.

# DNS

...

# Contenct Delivery Network (CDN)

- Push CDN: Content server actively pushes contents to the CDN.
  - Advantage: the client traffic can go directly to the CDN for the available contents. As a result, less traffic
  - Disadvantage: not disk efficient. It doesn't care if the contents will be asked by the client, just push them to the CDN.
  - Suitable for smaller system, less updated contents.
- Pull CDN: Will put the contents to CDN after a client requests them.
  - Advantage: disk efficient. Put contents to CDN just if someone asks.
  - Disadvantage: more traffic **to** the content server.
  - Suitable for larger system, frequently updated contents.

# Database

Link: https://github.com/donnemartin/system-design-primer#database

Relational database transactions must have ACID properties:

- Atomicity
- Consistency
- Isolation
- Durability

Techniques to scale relational database:

- master-slave replication [[link](https://github.com/donnemartin/system-design-primer#master-slave-replication)]
  - Write only to master, can read from both master or slave
- master-master replication [[link](https://github.com/donnemartin/system-design-primer#master-master-replication)]
  - Write and read can be done to all master (there is no slave)
- federation [[link](https://github.com/donnemartin/system-design-primer#federation)]
  - Splitting DB by function instead of having a monolithic DB. For example: the DB is splitted to user DB, product DB, etc.
- sharding [[link](https://github.com/donnemartin/system-design-primer#sharding)]
  - Distributing data across different databases. For example, there is a load balancer in front of 4 DB to split users by their first letter of their name: user A-C, D-F, G-I, X-Y.
- denormalization [[link](https://github.com/donnemartin/system-design-primer#denormalization)]
  - Making `read` faster by avoiding `JOIN`. The way is to add duplicate data from other tables to another. This way, no `JOIN` is possible. Only makes sense for a system much more `read` than `write`. 
- SQL tuning [[link](https://github.com/donnemartin/system-design-primer#sql-tuning)]
  - use `CHAR` instead of `VARCHAR`
  - use `TEXT` for big texts such as blog posts
  - `INT` for integers up to 2^32 or 4 billion
  - `DECIMAL` for money
  - avoid storing large `BLOBS`. Instead, store the location of these objects
  - set `NOT NULL` constraint where applicable
  - use database indexing
  - avoid `JOIN` for faster reading (denormalize)

# NoSQL

https://github.com/donnemartin/system-design-primer#nosql

Unlike relational database, NoSQL has BASE properties:

- Basically available
- Soft state
- Eventual consistency

Types of NoSQL:

- Key-value store
  - Abstraction: hash table
  - Example: redis, memcached
- Document store
  - Abstraction: Key-value store with documents such as JSON or XML as values
  - The documents' formats, as values' formats, are understood by the DB, so that it can do query on the documents
  - Example: MongoDB, CouchDB, Elasticsearch
- Wide column store
  - TODO: read more and experiment since this is new to me and I don't really understand
  - Example: Cassandra
- Graph database
  - TODO: read more and experiment since this is new to me and I don't really understand
  - Example: Neo4j

Considerations for SQL vs NoSQL: https://github.com/donnemartin/system-design-primer#sql-or-nosql

# Cache

General categories of cache:

- database queries
- objects:
  - serializable objects
  - html
  - user session
  - activity streams
  - user graph data

Avoid file-based caching (hard to scale).

Patterns:

- cache aside: client read->backend->(check cache, if not found, go to DB)->DB
- write through: client write->backend->write to cache->write to DB (result: cache always have data. faster reading, slower writing)
- write-behind (write-back): see [this](https://github.com/donnemartin/system-design-primer#write-behind-write-back)
- refresh-ahead: see [this](https://github.com/donnemartin/system-design-primer#refresh-ahead)

# Asynchronism

https://github.com/donnemartin/system-design-primer#asynchronism

Very good article about backpressure: https://medium.com/@jayphelps/backpressure-explained-the-flow-of-data-through-software-2350b3e77ce7

