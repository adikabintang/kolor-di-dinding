https://github.com/donnemartin/system-design-primer

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

## Database normalization

TODO

## More database tips

Article: https://www.lecloud.net/post/7994751381/scalability-for-dummies-part-2-database

- Database sharding [TODO]
- No `JOIN` in SQL (use MySQL like NoSQL). Joining is done in the application code

# Asynchronism

If we are working on blocking task, make it asynchronous. For example, in microservices, we can use Kafka or NATS for this purpose.