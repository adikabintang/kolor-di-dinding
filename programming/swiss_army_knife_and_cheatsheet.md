Some of the most important use of Python `collections` and C++ `STL`.

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
arr.reverse() # in-place
split_arr_half = arr[:len(arr) // 2]

# get index of a value
try:
    idx = arr.index(val)
except ValueError as err:
    print("not found: %s" % (err))
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

std::reverse(arr.begin(), arr.end()); // reverse in-place
// for the real array:
std::reverse(std::begin(real_arr), std::end(real_arr));

// get index of a value
auto it = std::find(arr.begin(), arr.end(), val);
if (it != arr.end()) {
    int idx = std::distance(arr.begin(), it);
} else {
    // not found
}
```

# Stack

### Python

```python
# use list
arr = []

arr.append(val) # push
arr.pop()       # pop 
```

### C++

```cpp
#include <stack>
std::stack<type> a_stack;
a_stack.push(val);
a_stack.top();          // peek at the top value
a_stack.empty();        // check if empty
a_stack.pop();
```

# Queue

Bare in mind that using array as queue is not that optimal. Use doubly linked list to support O(1) operations.

### Python

More detail here: https://dbader.org/blog/queues-in-python

```python
from collections import deque

q = deque()
q.append(val)
try:
    front_val = q.popleft()
except IndexError:
    print("queue is empty")
```

### C++

```cpp
#include <queue>
std::queue<type> q;
q.push(val);
q.empty();      // check if empty
auto val = q.pop();
```

# Set

### Python

```python
s = set()
s.add(val)
if val in s:
    pass
for val in s:
    pass
s.remove(val)
arr = list(s)
to_set = set(arr)
```

### C++

```cpp
#include <set>

std::set<type> s;
s.insert(val);
unsigned int size = s.size();
for (auto val : s) {
    std::cout << val << std::endl;
}

s.erase(val);
if (s.find(val) != s.end()) {
    // found
}

// get the first element of the set
auto it = std::next(s.begin(), 0);
std::cout << *it;

std::vector<type> v;
std::set<type> s(v.begin(), v.end());
std::vector<type> arr(s.begin(), s.end());
```

# Hash Table

### Python

```python
hash_table = dict()
hash_table[key] = value
for key, value in hash_table.items():
    pass
if key in hash_table:
    pass
del hash_table[key]
```

### C++

```cpp
#include <map>

std::map<key_type, value_type> hash_table;
hash_table.insert(std::make_pair(key, value));
hash_table[key] = value;
for (auto element : hash_table) {
    auto key = element.first;
    auto val = element.second;
}

if (hash_table.find(key) != hash_table.end()) {
    // found
} else {
    // not found
}

hash_table.erase(key);
```

# Bit Vector

See: [bit_array.c](programming/basics/crackingthecodinginterview/sorting_and_searching/bit_array.c)

### Python

No built-in. See here: https://wiki.python.org/moin/BitArrays

### C++

```cpp
#include <bitset>
```

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

## Check if string is alphabet/numeric/alphanumeric

## Join array/list of chars to string

## String replace

## Strstr

# Map, reduce, zip
