# Dynamic array/list

### Python

```python
arr = []

for val in arr:
    visit(val)

i = 0
while i < len(arr):
    visit_or_manipulate(arr[i])
    i += 1

arr.sort(reverse=True)
arr.sort(key=lambda x: x) 
# if arr=[(a,b)] key=lambda x: x[0] 
# if the first el of tuple is the key

reversed_arr = arr[::-1]
split_arr_half = arr[:len(arr) // 2]
```

### C

No built-in dynamic array. There is a static-sized array.

```c

```

### C++

```cpp
std::vector<type> arr;

for (int i = 0; i < arr.size(); i++) {
    visit_or_manipulate(arr.at(i));
}

for (auto val : arr) {
    visit(arr.at(i))
}

// #include <algorithm>
std::sort(arr.begin(), arr.end()); // ascending
std::sort(arr.begin(), arr.end(), std::greater<>()); // descending

class Person {
public:
    int age;
};

std::vector<Person> people;

// ascending sort, give the key
std::sort(people.begin(), people.end(), 
    [](const people &a, const people &b) { 
        return a.age < b.age;
    }
);

std::reverse(arr.begin(), arr.end()); // reverse in memory
// for the real array:
std::reverse(std::begin(real_arr), std::end(real_arr));
```

### Java

```java
ArrayList<type> arr;
```

# Set

# Hash Table


# Bit Vector

# String operations

## Split strings by character

### Python

```python
array = string.split(delimiters)
```

### C

```C
char *p = strtok(string, delimiter)
```

### Java

```java
String parts[] = string.splits(delimiter)
```

## Check if string is alphabet/numeric/alphanumeric

## Join array/list of chars to string

## Strstr
