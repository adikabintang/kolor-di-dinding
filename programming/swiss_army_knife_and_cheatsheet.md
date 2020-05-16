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

arr.push_back(val);
auto x = arr.at(i);

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
    [](const Person &a, const Person &b) { 
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

# Priority queue/heap

### Python

__this is min heap__, people say we need to multiply by -1 to make a max heap.

```python
import heapq
pq = []
heapq.heappop(pq)
heapq.heappush(pq, val)
```

### C++

Min heap.

```cpp
std::priority_queue<int, std::vector<int>, std::greater<int>> q;

for(int n : {1,8,5,6,3,4,0,9,7,2})
    q.push(n);
int root = q.top();
q.pop();
```

Max heap.

```cpp
std::priority_queue<int> q;

for(int n : {1,8,5,6,3,4,0,9,7,2})
    q.push(n);
int root = q.top();
q.pop();
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

### C++

Oh man....

https://www.fluentcpp.com/2017/04/21/how-to-split-a-string-in-c/

```cpp
std::vector<std::string> split(const std::string& s, char delimiter)
{
   std::vector<std::string> tokens;
   std::string token;
   std::istringstream tokenStream(s);
   while (std::getline(tokenStream, token, delimiter))
   {
      tokens.push_back(token);
   }
   return tokens;
}
```

## Check if string is alphabet/numeric/alphanumeric

### Python

```python
s = "asdasd"
s.isalnum()
s.isalpha()
s.isnumeric()
```

### C++

```cpp
#include <cctype>
#include <algorithm>

// there are also 
// std::isalpha(char) and std::isdigit(char)
bool my_is_alnum(std::string &s) {
    return std::find_if(s.begin(), s.end(), 
        [](char c){ return std::is_alnum(c); });
}
```

## Join array/list of chars to string

### Python

```python
arr = ["a", "sd"]
separator = "."
res = separator.join(arr)
```

### C++

```cpp
```

## String replace

### Python

```python
s = "oh man what is this man"
s.replace("man", "boi")
# s = "oh boi what is this boi"
```

### C++

https://stackoverflow.com/questions/3418231/replace-part-of-a-string-with-another-string

```cpp
std::string haystack = "oh man what is this man";
std::string needle = "man";

std::size_t found = haystack.find(needle);
if (found != std::string::npos) {
    std::cout << "found at idx: " << found;
}
haystack.replace(found, needle.length(), "boi");
```

## Find the first occurrence of a substring

### Python

```python
s = "ah apaan nih anjir"
s.find("nih") # return idx of "nih", 9
```

### C

```c
char *haystack = "ah apaan nih anjir";
char *needle = "nih";
char *r = strstr(haystack, needle);
if (r == NULL)
    return -1;

if ((intptr_t)r == 0)
    return 0;

int location = (intptr_t)r - (intptr_t)haystack;
```

## String to lower, to upper

### Python

```python
s = "str"
b = s.isupper() # returns true or false
b = s.isupper
low = s.lower()
up = s.upper()
```

## More for C

```c
char src[100], dest[100];

// copying string, don't use strcpy as it can cause overflow
memset(dest, '\0', sizeof(dest));
strcpy_s(src, sizeof(src), "nusa damai");
strcpy_s(dest, sizeof(dest), src);

// copying n chars of a string
strncpy_s(dest, sizeof(dest), "nusa damai", n);

// append to the end of a string
strcat_s(dest, sizeof(dest), "addition");

// comparing string
// if equal, return 0
// comparing lexicographically
int res = strcmp(src, dest);

// copy the content of memory, not null terminated like strcpy
// memcpy has an undefined behavior when the memory of src and dest overlaps
int arr[3] = {1, 2, 3};
int brr[3];
memcpy_s(brr, sizeof(brr), arr, sizeof(arr));

// memmove can handle overlapping memory, but it operates
// slower than memcpy
memmove_s(brr, sizeof(brr), arr, sizeof(arr));
```

### C++

```cpp
std::string haystack = "ah apaan nih anjir";
std::string needle = "nih";

std::size_t found = haystack.find(needle);
if (found != std::string::npos) {
    std::cout << "found at idx: " << found;
}
```


# Map and Filter

### Python

https://www.python-course.eu/python3_lambda.php

```python
arr = [1, 2, 3, 4]
list(map(lambda x: x * 2, arr)) # [2, 4, 6, 8]

# filter out arr element if that element % 2 == true
list(filter(lambda x: x % 2, arr)) #[1, 3]
```

### C++

https://stackoverflow.com/questions/40901615/how-to-replicate-map-filter-and-reduce-behaviors-in-c-using-stl

```cpp
std::vector<int> nums{1, 2, 3, 4, 5, 6};
std::vector<int> result;

// std::transform = map
// if we want the result to be in "nums" too (in-place),
// put nums.begin() instead of std::back_inserter(result) as 
// the 3rd parameter
std::transform(nums.begin(), nums.end(), std::back_inserter(result),
    [](int x) {return x * 2; });

for (int i = 0; i < nums.size(); i++) {
    std::cout << result.at(i) << std::endl;
}

std::vector<int> result_copy;

// std::copy_if = filter
std::copy_if(nums.begin(), nums.end(), std::back_inserter(result_copy),
    [](int x){ return x % 2; });

for (int i = 0; i < result_copy.size(); i++) {
    std::cout << result_copy.at(i) << std::endl;
}
```
