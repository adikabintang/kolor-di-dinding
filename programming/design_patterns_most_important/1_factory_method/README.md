# Factory Method Pattern

Used when the application depends on an interface to perform a task and there are multiple concrete implementation of that interface.

If we have:

```java
myObj = new ThatClass();
```

The code is now tightly coupled with `ThatClass`. What we can do to make it better is _to code to an interface and not to an implementation_. The factory method pattern provides an interface for object creation, but leaves the actual instantiation of objects to subclass. 

Credits:

- https://realpython.com/factory-method-python/
- educative.io
- 