"""
 Python’s built-in list type makes a decent stack data structure as it
  supports push and pop operations in amortized O(1) time.
"""
s = []

s.append('khaled')
s.append('Nada')
s.append('Abood')
print(s)

s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
print(s)

# collections.deque: Fast and Robust Stacks الأفضل
from collections import deque

s = deque()
s.append("eat")
s.append("sleep")
s.append("code")
print(s)
# print(type(s))
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)

# queue.LifoQueue: Locking Semantics for Parallel Computing

from queue import LifoQueue

s = LifoQueue()

s.put('eat')
s.put('sleep')
s.put('code')

print(s)

s.get()
s.get()
s.get()

# s.get_nowait()

# Stack Implementations in Python: Summary
'''
As you’ve seen, Python ships with several implementations for a stack data structure. All of them have slightly different characteristics as well as performance and usage trade-offs.

If you’re not looking for parallel processing support (or if you don’t want to handle locking and unlocking manually), then your choice comes down to the built-in list type or collections.deque. The difference lies in the data structure used behind the scenes and overall ease of use.

list is backed by a dynamic array, which makes it great for fast random access but requires occasional resizing when elements are added or removed.

The list over-allocates its backing storage so that not every push or pop requires resizing, and you get an amortized O(1) time complexity for these operations. But you do need to be careful to only insert and remove items using append() and pop(). Otherwise, performance slows down to O(n).

collections.deque is backed by a doubly-linked list, which optimizes appends and deletes at both ends and provides consistent O(1) performance for these operations. Not only is its performance more stable, the deque class is also easier to use because you don’t have to worry about adding or removing items from the wrong end.

In summary, collections.deque is an excellent choice for implementing a stack (LIFO queue) in Python.
'''