Source: https://www.youtube.com/watch?v=HqPJF2L5h9U

# Heap

Max heap: a complete binary tree, filled left to right, that every parent is greater than their children. Root node is the greatest.

Max heap example:

```
    5
   / \
  3   4
 / \
1   2
```

Represented as an array: `[5, 3, 4, 1, 2]`

Min heap: a complete binary tree, filled left to right, that every parent is smaller than their children. Root node is the smallest.

Min heap example:

```
    1
   / \
  2   3
 / \ /
4  5 6
```

Represented as an array: `[1, 2, 3, 4, 5, 6]`

Heap height is `log n`.

In the array, a node at index `i`:

- The left child is `2 * i + 1`
- The right child is `2 * i + 2`
- The parent is `floor(i / 2)`

## Heap operation for max heap (change the comparison operation for min heap)

### Insert

How:

1. Insert at the last leaf (last index in the array)
2. Keep comparing with the parent to root. Swap if the parent is smaller. Stop when it's no longer smaller.

```python
def insert(val: int):
    i = len(arr)
    parent_idx = i // 2
    arr.append(val)
    while i > 0 and arr[i] > arr[parent_idx]:
        temp = arr[i]
        arr[i] = arr[parent_idx]
        arr[parent_idx] = temp
        i = parent_idx
        parent_idx = i // 2
```

Takes at most `O(log n)` to crawl from the last leaf to the root.

The key to remember: insert at last, bring it to top.

### Delete/poll

How: 

1. Delete the root (first element of the array)
2. Take the last leaf (last index of the array) to the root (first index)
3. Keep comparing:
   1. Largest child index = take the index of the largest child
   2. If the largest child is greater than the current, swap.
   3. Stop if the largest child is no longer greater than the current.

```python
def poll() -> int:
    ret_val = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    i = 0
    left_child_idx = 2 * i + 1
    right_child_idx = 2 * i + 2
    while i < len(arr) and \
        (arr[i] < arr[left_child_idx] or arr[i] < arr[right_child_idx]):

        largest_idx = right_child_idx \
            if arr[right_child_idx] > arr[left_child_idx] \
            else left_child_idx

        temp = arr[i]
        arr[i] = arr[largest_idx]
        arr[largest_idx] = temp
        i = largest_idx
        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2

    return ret_val
```

Takes at most `O(log n)` operation, depends on the height.

The key to remember: delete the root, take the last one to top, keep comparing it down to the leaf.

### Create a heap from an array: the O(n log n) way

Take an array, do insert operation. Takes `O(n log n)`.

```python
def create_heap(input: [int]):
    for val in input:
        insert(val)
```

### Heapify: the O(n) way

How: Go from the leaf right (last index of the array) to the root (first index). Do heap adjustment along the way.

Takes `O(n)`. Read more: https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity

```python
def heapify(arr: [int]):
    i = len(arr) - 1
    while i >= 0:
        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2
        j = i
        while left_child_idx < len(arr) or right_child_idx < len(arr):
            largest_idx = 0
            if left_child_idx < len(arr) \
                and right_child_idx < len(arr):
                largest_idx = right_child_idx \
                    if arr[right_child_idx] > arr[left_child_idx] \
                    else left_child_idx
            else:
                largest_idx = right_child_idx \
                    if right_child_idx < len(arr) \
                    else left_child_idx

            if arr[j] < arr[largest_idx]:
                temp = arr[j]
                arr[j] = arr[largest_idx]
                arr[largest_idx] = temp
                j = largest_idx
                left_child_idx = 2 * j + 1
                right_child_idx = 2 * j + 2
            else:
                break

        i -= 1
```

# Priority queue

Priority queue is an abstract data structure that can be implemented with heap.

If we want to have a queue with a priority: smallest number gets out first, use min heap.

If we want to have a queue with a priority: greatest number gets out first, use max heap.
