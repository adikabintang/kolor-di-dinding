# C and C++

# Python

# Java

#### StringBuilder

When to use `String` and `StringBuilder`:
https://stackoverflow.com/questions/1532461/stringbuilder-vs-string-concatenation-in-tostring-in-java

In short:
- `StringBuilder` is mutable, `String` is immutable
- `StringBuilder` is faster, since copying is not done everytime. If we need to concate strings in a loop, use `StringBuilder`. But if it is only `String s = "a" + "b"`, Java compiler will convert that to `StringBuilder` so convert it manually to `StringBuilder` will not affect the performance.