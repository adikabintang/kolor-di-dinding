# C and C++

# Python

#### Empty array as default parameter

In Python, don't set the default parameter as an empty array because it is an undefined behavior [[link]](https://stackoverflow.com/questions/366422/what-is-the-pythonic-way-to-avoid-default-parameters-that-are-empty-lists). For example, DON'T DO THIS:

```python
def a_function(some_list = []):
    pass
```

Instead, use like this:

```python
def a_function(some_list = None):
    if some_list is None:
        some_list = []
```

# Java

#### StringBuilder

When to use `String` and `StringBuilder`:
https://stackoverflow.com/questions/1532461/stringbuilder-vs-string-concatenation-in-tostring-in-java

In short:
- `StringBuilder` is mutable, `String` is immutable
- `StringBuilder` is faster, since copying is not done everytime. If we need to concate strings in a loop, use `StringBuilder`. But if it is only `String s = "a" + "b"`, Java compiler will convert that to `StringBuilder` so convert it manually to `StringBuilder` will not affect the performance.