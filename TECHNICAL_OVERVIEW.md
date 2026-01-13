# Python Algorithms & Data Structures Repository — Technical Overview

> A comprehensive reference document for tech interviewers and talent hunters evaluating software engineering proficiency.

---

## 📌 Repository Summary

This repository demonstrates **hands-on mastery** of fundamental computer science concepts through clean, well-documented Python implementations. It covers the core data structures and algorithms that form the backbone of technical interviews at leading technology companies.

| Category | Count | Implementation Style |
|----------|-------|---------------------|
| Data Structures | 10+ | Object-Oriented Python with Type Hints |
| Search/Sort Algorithms | 6+ | Iterative & Recursive Approaches |
| Exercises | 15+ | Real-world problem solving scenarios |
| Jupyter Notebooks | 12+ | Interactive demonstrations |

---

## 🧱 Data Structures Implemented

### 1. Linked Lists

**Singly Linked List** — Full CRUD operations with pointer manipulation

```python
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def insert_at_beginning(self, data): ...
    def insert_at_end(self, data): ...
    def insert_at(self, index, data): ...
    def remove_at(self, index): ...
    def get_length(self): ...
```

**Doubly Linked List** — Bidirectional traversal with prev/next pointers

```python
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def insert_at_begining(self, data): ...
    def insert_at_end(self, data): ...
    def insert_at(self, index, data): ...
    def print_forward(self): ...
    def print_backward(self): ...
```

**Key Skills Demonstrated:**
- Pointer manipulation and memory management concepts
- Index-based insertion and deletion
- Bidirectional traversal algorithms

---

### 2. Hash Tables

Two collision resolution strategies implemented from scratch:

**Separate Chaining (Linked List Buckets)**

```python
class HashTable:
    def __init__(self, max=100):
        self.MAX = max
        self.arr = [[] for i in range(self.MAX)]  # Array of lists

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value): ...  # Pythonic operator overloading
    def __getitem__(self, key): ...
    def __delitem__(self, key): ...
```

**Linear Probing (Open Addressing)**

```python
class HashTable:
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]
    
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception('Hashmap full')
```

**Key Skills Demonstrated:**
- Hash function design using ASCII values
- Collision resolution: Chaining vs. Open Addressing
- Python magic methods (`__setitem__`, `__getitem__`, `__delitem__`)

---

### 3. Trees

**General Tree Structure** — Hierarchical data representation

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child: TreeNode) -> TreeNode:
        child.parent = self
        self.children.append(child)
        return self
    
    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level
```

**Binary Search Tree** — Complete BST with all traversal methods

```python
class BinarySearchTreeNode:
    def add_child(self, data): ...        # O(log n) average
    def delete(self, value): ...          # O(log n) with subtree restructuring
    def search(self, value): ...          # O(log n) average
    def find_min(self): ...               # Leftmost node
    def find_max(self): ...               # Rightmost node
    def calculate_sum(self): ...          # Recursive tree sum
    
    # Traversal Methods
    def in_order_traversal(self): ...     # Left → Root → Right (sorted order)
    def pre_order_traversal(self): ...    # Root → Left → Right
    def post_order_traversal(self): ...   # Left → Right → Root
```

**Key Skills Demonstrated:**
- Recursive tree algorithms
- BST properties and invariant maintenance
- Node deletion with successor/predecessor replacement
- Three standard tree traversal patterns

---

### 4. Stack

LIFO data structure with practical applications:

```python
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value): ...
    def pop(self): ...
    def peek(self): ...       # View top without removal
    def is_empty(self): ...
    def size(self): ...
```

**Practical Applications Implemented:**
- **String Reversal** — Using stack's LIFO property
- **Balanced Parentheses Checker** — Expression validation for `()`, `[]`, `{}`, `<>`

```python
def is_balanced(string):
    """Validates matching parentheses in mathematical expressions"""
    parenthesis = [['(', ')'], ['[', ']'], ['{', '}'], ['<', '>']]
    s = Stack()
    for character in string:
        if character in opened:
            s.push(character)
        if character in closed:
            if s.size() == 0 or not is_match(character, s.pop(), parenthesis):
                return False
    return s.size() == 0
```

---

### 5. Queue

FIFO data structure with multi-threaded example:

```python
class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, value): ...
    def dequeue(self): ...
    def is_empty(self): ...
    def size(self): ...
```

**Practical Application: Food Ordering System with Threading**

```python
import time, threading

class Order:
    def __init__(self):
        self.orders = Queue()
    
    def place_orders(self, orders):
        for order in orders:
            self.orders.enqueue(order)
            time.sleep(0.5)  # Simulate order placement
    
    def serve_orders(self):
        while self.orders.size():
            self.serve_order()
            time.sleep(2)    # Simulate serving time

# Multi-threaded execution
t1 = threading.Thread(target=o.place_orders, args=(orders,))
t2 = threading.Thread(target=o.serve_orders)
```

**Key Skills Demonstrated:**
- Python's `collections.deque` for O(1) operations
- Producer-consumer pattern with threading
- Real-world simulation modeling

---

### 6. Graphs

Directed graph implementation with pathfinding:

```python
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}  # Adjacency list representation
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
    
    def get_paths(self, start, end, path=[]):
        """Find ALL possible paths between two nodes"""
        ...
    
    def shortest_path_by_stops(self, start, end, path=[]):
        """Find shortest path (minimum hops) using DFS"""
        ...
```

**Sample Use Case: Flight Route Planning**

```python
routes = [
    ('Mumbai', 'Paris'), 
    ('Mumbai', 'Dubai'), 
    ('Paris', 'Dubai'), 
    ('Paris', 'New York'), 
    ('Dubai', 'New York'), 
    ('New York', 'Toronto'), 
]

route_graph = Graph(routes)
route_graph.get_paths('Mumbai', 'New York')
# Returns all possible flight routes between cities
```

---

## 🔍 Algorithms Implemented

### Binary Search — O(log n)

**Iterative Implementation:**

```python
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]
        
        if mid_number == number_to_find: 
            return mid_index
        if mid_number < number_to_find: 
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
            
    return -1
```

**Recursive Implementation with All Occurrences:**

```python
def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]
    
    if mid_number == number_to_find: 
        return mid_index
    if mid_number < number_to_find:
        return binary_search_recursive(numbers_list, number_to_find, mid_index + 1, right_index)
    else:
        return binary_search_recursive(numbers_list, number_to_find, left_index, mid_index - 1)

def find_all_occurances(numbers, number_to_find):
    """Extends binary search to find ALL indices of duplicate values"""
    index = binary_search_recursive(numbers, number_to_find, 0, len(numbers))
    # Expand left and right from found index
    ...
```

---

### Graph Traversal Algorithms

**Depth-First Search (DFS)** — Stack-based exploration  
**Breadth-First Search (BFS)** — Queue-based level-order exploration

Both implementations included with practical exercise solutions.

---

### Sorting Algorithms

| Algorithm | Time Complexity | Space Complexity | Stability |
|-----------|-----------------|------------------|-----------|
| Bubble Sort | O(n²) | O(1) | Stable |
| Quick Sort | O(n log n) avg | O(log n) | Unstable |
| Merge Sort | O(n log n) | O(n) | Stable |
| Insertion Sort | O(n²) | O(1) | Stable |
| Selection Sort | O(n²) | O(1) | Unstable |
| Shell Sort | O(n log n) ~ O(n²) | O(1) | Unstable |

---

## 💡 Technical Skills Demonstrated

### Python Proficiency

- **Type Hints** — Modern Python 3.x typing syntax (`from __future__ import annotations`)
- **Magic Methods** — Operator overloading for intuitive APIs (`__setitem__`, `__getitem__`, `__delitem__`)
- **Collections Module** — Efficient use of `deque` for O(1) append/pop operations
- **Multi-threading** — Producer-consumer patterns with `threading` module

### Computer Science Fundamentals

- **Big O Analysis** — Time and space complexity documented in comments
- **Recursion** — Extensive use in tree traversals, binary search, and graph algorithms
- **Pointer/Reference Manipulation** — Linked list operations requiring careful node management
- **Algorithm Design Patterns** — Divide and conquer, two-pointer technique, sliding window

### Software Engineering Practices

- **Clean Code** — Readable, self-documenting function and variable names
- **Modular Design** — Separation of data structure classes and driver code
- **Interactive Documentation** — Jupyter notebooks for step-by-step learning
- **Exercise-Driven Learning** — Theory → Implementation → Exercises → Solutions pattern

---

## 📁 Repository Structure

```
python-algorithms/
├── data_structures/
│   ├── LinkedList.py          # Singly linked list
│   ├── DoublyLinkedList.py    # Doubly linked list
│   ├── HashTableChaining.py   # Hash table with separate chaining
│   ├── HashTableProbing.py    # Hash table with linear probing
│   ├── BinarySearchTree.py    # BST with traversals
│   ├── Tree.py                # General tree structure
│   ├── Graph.py               # Directed graph with pathfinding
│   ├── Stack-excercise.py     # Stack with practical applications
│   ├── Queue-excercise.py     # Queue with threading example
│   ├── *.ipynb                # Interactive Jupyter notebooks
│   └── resources/             # CSV files for exercises
│
├── search_algorithms/
│   ├── BinarySearch.py        # Iterative binary search
│   ├── BinarySearch-excercise.py  # Recursive + find all occurrences
│   ├── BubbleSort.ipynb       # Sorting algorithm notebook
│   └── *.ipynb                # Interactive exercises
│
└── _resources/
    ├── algorithms/            # Reference implementations
    │   ├── BinarySearch/
    │   ├── BubbleSort/
    │   ├── QuickSort/
    │   ├── MergeSort/
    │   ├── InsertionSort/
    │   ├── SelectionSort/
    │   ├── ShellSort/
    │   ├── DepthFirstSearch/
    │   └── BreadthFirstSearch/
    │
    └── data_structures/       # Exercise materials
        ├── Arrays/
        ├── LinkedList/
        ├── HashTable/
        ├── Stack/
        ├── Queue/
        ├── Tree/
        ├── Binary_Tree/
        └── Graph/
```

---

## 🎯 Value for Technical Interviewers

This repository demonstrates:

1. **Foundational Knowledge** — Not just using Python's built-in structures, but understanding how they work internally
2. **Problem-Solving Approach** — Breaking down complex problems into manageable components
3. **Code Quality** — Clean, readable implementations with appropriate documentation
4. **Learning Mindset** — Structured approach with theory, practice, and exercises
5. **Practical Application** — Real-world examples (flight routing, food ordering, expression parsing)

### Complexity Analysis Summary

| Data Structure | Insert | Delete | Search | Access |
|---------------|--------|--------|--------|--------|
| Linked List | O(1)* | O(1)* | O(n) | O(n) |
| Hash Table | O(1) avg | O(1) avg | O(1) avg | O(1) avg |
| Binary Search Tree | O(log n) avg | O(log n) avg | O(log n) avg | O(log n) avg |
| Stack | O(1) | O(1) | O(n) | O(n) |
| Queue | O(1) | O(1) | O(n) | O(n) |

*\* At known position*

---

## 🔗 How to Explore

```bash
# Clone the repository
git clone <repository-url>
cd python-algorithms

# Run standalone Python files
python data_structures/BinarySearchTree.py
python data_structures/Graph.py

# Launch Jupyter notebooks for interactive learning
jupyter notebook data_structures/
```

---

## 📚 Learning Path Covered

1. **Arrays** — Foundation of sequential data storage
2. **Linked Lists** → **Doubly Linked Lists** — Pointer-based structures
3. **Hash Tables** — Key-value storage with collision handling
4. **Stacks & Queues** — LIFO/FIFO abstract data types
5. **Trees** → **Binary Search Trees** — Hierarchical data organization
6. **Graphs** — Network/relationship modeling with DFS/BFS
7. **Sorting Algorithms** — Comparison-based sorting techniques
8. **Search Algorithms** — Efficient data retrieval patterns

---

*Repository maintained by [libe.dev](https://libe.dev)*
