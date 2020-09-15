# Control and data plane separation

Source: coursera

## Benefit/opportunities of control and data plane separation

### Interdomain routing: constrained policies

**Example 1:**

```
R1-----------R2----|
    |              |---
    ---R3-----R4---|
```

Default route: R1-R2. Now for some reason, like maintenance, the operator wants the route is R1-R3-R4. We can change the configuration in *every router* to change many knobs of the protocol (like in BGP, change the weight or something for influencing the best path selection). It's much easier to manage if we have a centralized controller.

**Example 2: Better BGP security**

If the IDS detects a suspicious route advertisement (in an attempt of BGP hijacking), the centralized controller can ask all of the routers to avoid that route.

**Example 3: data center addressing**

How to address hosts in a data center?

## Challenges in separating control and data plane

- scalability: routing decisions for many routers
- reliability: correct operation under failure
- consistency: ensuring consistency accross multiple control replicas

## 4D network archiecture

```
---
Decision
---
dissemination
---
discovery
---
data
```

- Decision: all management and control, logically centralized controllers that convert objectives into packet-handling state
- Dissemination: communication to/from routers, insalling packet processing rules
- Discovery: topology and traffic monitoring, for collecing topology and traffic
- Data: traffic handling, packet processing
