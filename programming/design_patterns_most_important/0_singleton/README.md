# Singleton

Be careful. When to use singleton:

- Solving resource contention problem (conflict over access to a shared resource)
- The class has no state
- The class tightly controls its resources
- Only 1 object is permissible

One of the example is the log class. DB connection class *should not be a singleton* (a popular example).

Some notes:

- Singleton is not a wrapper to globals (remember, singleton should have no state)
- If it has state (thus making it a global wrapper), refactor

*It's better to avoid singleton in the first place.*

Credits:

- https://stackoverflow.com/questions/137975/what-is-so-bad-about-singletons
- https://stackoverflow.com/questions/6507687/should-a-db-connection-be-a-singleton
- https://stackoverflow.com/questions/228164/on-design-patterns-when-should-i-use-the-singleton
- https://en.wikipedia.org/wiki/Resource_contention
