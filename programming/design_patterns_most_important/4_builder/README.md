# Builder pattern

We have a class that have too many constructors. There are many constructors because we want to instantiate different kinds of objects from that class. This can be confusing.

The builder pattern's intent is to minimize the number of constructors.

Let's say we have a `Pizza` class:

```python
class Pizza:
    dough_type: str
    sauce_type: str
    topping: str
```

In order to make different types of pizza, we can have different constructors (for example, `Pizza(dough)`, `Pizza(sauce, dough)`, etc). Also, should we have a default constructor? If we use the default constructor, what pizza it will make? What if the client code is mistakenly calling the default constructor and not really sure what object is that?

The idea of the builder pattern is to have "builders" who build the object for the client code. The constructor of the product class (in this case, the pizza), can be only 1. The builder builds it by calling the setters.

The client code can build the object by talking to the concrete builders. Alternatively, there can be a director (like a consultant), the client talks to the director, the director talks to the builders.

Credits:

- https://medium.com/@andreaspoyias/design-patterns-a-quick-guide-to-builder-pattern-a834d7cacead
- https://sourcemaking.com/design_patterns/builder
