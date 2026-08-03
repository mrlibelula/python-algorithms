<div align="center">

# Data Structures & Algorithms in Python

### A Comprehensive Interview Preparation Repository

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Portfolio](https://img.shields.io/badge/Portfolio-libe.dev-blue?style=for-the-badge&logo=googlechrome&logoColor=white)](https://libe.dev)

<br>

*From-scratch implementations of essential data structures and algorithms, designed for technical interview mastery and deep understanding of computer science fundamentals.*

<br>

[Explore Notebooks](#data-structures) · [🧪 Run Exercises](#-getting-started) · [Complexity Analysis](#complexity-analysis-cheat-sheet) · [Technical Overview](TECHNICAL_OVERVIEW.md)

---

</div>

## About This Repository

This repository demonstrates **hands-on mastery** of fundamental computer science concepts through clean, well-documented Python implementations. Unlike library-dependent code, every data structure and algorithm here is **built from scratch** to showcase deep understanding of how things work under the hood.

<table>
<tr>
<td width="50%">

### Repository Stats

| Category | Count |
|:---------|:-----:|
| Data Structures | **10+** |
| Algorithms | **9+** |
| Interactive Notebooks | **15+** |
| Practice Exercises | **20+** |
| Lines of Code | **2,500+** |

</td>
<td width="50%">

### Key Highlights

- **No External Dependencies** — Pure Python implementations
- **Interview-Ready** — Covers FAANG-style questions
- **Well-Documented** — Clear explanations & comments
- **Interactive** — Jupyter notebooks for step-by-step learning
- **Practical Examples** — Real-world use cases

</td>
</tr>
</table>

---

## Data Structures

<details open>
<summary><b>Linear Structures</b></summary>

<br>

| Structure | Implementation | Key Operations | Notebook |
|:----------|:---------------|:---------------|:---------|
| **Singly Linked List** | [LinkedList.py](data_structures/LinkedList.py) | Insert, Delete, Traverse, Search | — |
| **Doubly Linked List** | [DoublyLinkedList.py](data_structures/DoublyLinkedList.py) | Bidirectional traversal, Insert at any position | — |
| **Stack** | [Stack.ipynb](data_structures/Stack.ipynb) | Push, Pop, Peek, IsEmpty | [📓](data_structures/Stack.ipynb) |
| **Queue** | [Queue.ipynb](data_structures/Queue.ipynb) | Enqueue, Dequeue, Producer-Consumer pattern | [📓](data_structures/Queue.ipynb) |

</details>

<details open>
<summary><b>Hash-Based Structures</b></summary>

<br>

| Structure | Implementation | Collision Strategy | Notebook |
|:----------|:---------------|:-------------------|:---------|
| **Hash Table (Chaining)** | [HashTableChaining.py](data_structures/HashTableChaining.py) | Separate Chaining with Linked Lists | [📓](data_structures/HashTable-chaining.ipynb) |
| **Hash Table (Probing)** | [HashTableProbing.py](data_structures/HashTableProbing.py) | Linear Probing (Open Addressing) | [📓](data_structures/HashTable-linear-probing.ipynb) |

</details>

<details open>
<summary><b>Tree Structures</b></summary>

<br>

| Structure | Implementation | Key Operations | Notebook |
|:----------|:---------------|:---------------|:---------|
| **General Tree** | [Tree.py](data_structures/Tree.py) | Add child, Get level, Print hierarchy | [📓](data_structures/Tree.ipynb) |
| **Binary Search Tree** | [BinarySearchTree.py](data_structures/BinarySearchTree.py) | Insert, Delete, Search, Min/Max, Traversals | [📓](data_structures/BinarySearchTree.ipynb) |

</details>

<details open>
<summary><b>Graph Structures</b></summary>

<br>

| Structure | Implementation | Key Operations | Notebook |
|:----------|:---------------|:---------------|:---------|
| **Directed Graph** | [Graph.py](data_structures/Graph.py) | Adjacency List, Find all paths, Shortest path | [📓](data_structures/Graph.ipynb) |

</details>

---

## Algorithms

### Search Algorithms

| Algorithm | Time Complexity | Implementation | Description |
|:----------|:---------------:|:---------------|:------------|
| **Binary Search** | O(log n) | [BinarySearch.py](search_algorithms/BinarySearch.py) | Iterative & Recursive implementations |
| **Binary Search (Find All)** | O(log n + k) | [BinarySearch-excercise.py](search_algorithms/BinarySearch-excercise.py) | Find all occurrences of duplicates |

### Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|:----------|:----:|:-------:|:-----:|:-----:|:------:|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| **Shell Sort** | O(n log n) | O(n^1.25) | O(n²) | O(1) | ❌ |

### Graph Algorithms

| Algorithm | Implementation | Use Case |
|:----------|:---------------|:---------|
| **Depth-First Search (DFS)** | [dfs.py](_resources/algorithms/8_DepthFirstSearch/dfs.py) | Path finding, Cycle detection, Topological sort |
| **Breadth-First Search (BFS)** | [bfs.py](_resources/algorithms/9_BreadthFirstSearch/bfs.py) | Shortest path (unweighted), Level-order traversal |

---

## Complexity Analysis Cheat Sheet

<div align="center">

| Data Structure | Access | Search | Insert | Delete | Space |
|:--------------|:------:|:------:|:------:|:------:|:-----:|
| **Array** | O(1) | O(n) | O(n) | O(n) | O(n) |
| **Linked List** | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| **Stack** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Queue** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Hash Table** | — | O(1)† | O(1)† | O(1)† | O(n) |
| **Binary Search Tree** | O(log n)† | O(log n)† | O(log n)† | O(log n)† | O(n) |
| **Graph (Adj. List)** | O(V) | O(V) | O(1) | O(E) | O(V+E) |

<sub>*At known position &nbsp;&nbsp; †Average case</sub>

</div>

---

## 🧪 Practice Exercises

Each topic includes hands-on exercises with solutions:

<details>
<summary><b>Arrays</b> — Manipulation, searching, sorting</summary>

- Finding max/min elements
- Marvel heroes data processing
- Odd/even number separation
- Expense tracking system

</details>

<details>
<summary><b>Linked Lists</b> — Pointer manipulation mastery</summary>

- Implement singly linked list from scratch
- Add doubly linked list functionality
- Insert/delete at any position
- Reverse a linked list

</details>

<details>
<summary><b>Hash Tables</b> — Collision handling strategies</summary>

- Weather data analysis with hash tables
- Word occurrence counter (poem analysis)
- Stock price lookup system
- Custom hash function design

</details>

<details>
<summary><b>Stacks</b> — LIFO applications</summary>

- String reversal
- Balanced parentheses checker `()[]{}` 
- Expression evaluation

</details>

<details>
<summary><b>Queues</b> — FIFO applications</summary>

- Binary number generator
- Food ordering system (with threading!)
- Producer-consumer pattern

</details>

<details>
<summary><b>Trees</b> — Hierarchical data mastery</summary>

- Management hierarchy visualization
- Location hierarchy system
- BST operations (CRUD)
- Tree traversals (Inorder, Preorder, Postorder)

</details>

<details>
<summary><b>Graphs</b> — Network algorithms</summary>

- Flight route planning system
- Find all paths between nodes
- Shortest path (by hops)
- DFS/BFS implementations

</details>

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Jupyter Notebook (optional, for interactive notebooks)

### Installation

```bash
# Clone the repository
git clone https://github.com/mrlibelula/python-algorithms.git
cd python-algorithms

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Jupyter for interactive notebooks
pip install jupyter

# Launch Jupyter
jupyter notebook
```

### Quick Start

```bash
# Run standalone Python implementations
python data_structures/BinarySearchTree.py
python data_structures/Graph.py
python data_structures/HashTableChaining.py

# Or explore interactively
jupyter notebook data_structures/
```

---

## Project Structure

```
python-algorithms/
│
├── 📂 data_structures/           # Main implementations
│   ├── 📄 LinkedList.py          # Singly linked list
│   ├── 📄 DoublyLinkedList.py    # Doubly linked list
│   ├── 📄 HashTableChaining.py   # Hash table (chaining)
│   ├── 📄 HashTableProbing.py    # Hash table (linear probing)
│   ├── 📄 BinarySearchTree.py    # BST with traversals
│   ├── 📄 Tree.py                # General tree
│   ├── 📄 Graph.py               # Directed graph
│   └── 📓 *.ipynb                # Interactive notebooks
│
├── 📂 search_algorithms/         # Search & sort algorithms
│   ├── 📄 BinarySearch.py        # Iterative binary search
│   ├── 📓 BubbleSort.ipynb       # Sorting notebook
│   └── 📓 *.ipynb                # More notebooks
│
├── 📂 _resources/                # Learning materials
│   ├── 📂 algorithms/            # Algorithm exercises & solutions
│   │   ├── BinarySearch/
│   │   ├── BubbleSort/
│   │   ├── QuickSort/
│   │   ├── MergeSort/
│   │   ├── InsertionSort/
│   │   ├── SelectionSort/
│   │   ├── ShellSort/
│   │   ├── DepthFirstSearch/
│   │   └── BreadthFirstSearch/
│   │
│   └── 📂 data_structures/       # Data structure exercises
│       ├── Arrays/
│       ├── LinkedList/
│       ├── HashTable/
│       ├── Stack/
│       ├── Queue/
│       ├── Tree/
│       └── Graph/
│
├── 📄 TECHNICAL_OVERVIEW.md      # Detailed technical documentation
└── 📄 README.md                  # You are here!
```

---

## Technical Skills Demonstrated

<table>
<tr>
<td width="33%">

### Python Proficiency
- Type hints & annotations
- Magic methods (`__setitem__`, `__getitem__`)
- Collections module (`deque`)
- Multi-threading

</td>
<td width="33%">

### CS Fundamentals
- Big O complexity analysis
- Recursion & iteration
- Pointer manipulation
- Algorithm design patterns

</td>
<td width="33%">

### Software Engineering
- Clean, readable code
- Modular architecture
- Interactive documentation
- Test-driven exercises

</td>
</tr>
</table>

---

## Learning Path

```
Recommended order for studying this repository:

1. Arrays           → Foundation of sequential data
         ↓
2. Linked Lists     → Understanding pointers/references
         ↓
3. Hash Tables      → Key-value storage & collision handling
         ↓
4. Stacks & Queues  → LIFO/FIFO abstract data types
         ↓
5. Trees & BST      → Hierarchical data organization
         ↓
6. Graphs           → Network modeling with DFS/BFS
         ↓
7. Sorting          → Comparison-based algorithms
         ↓
8. Searching        → Efficient data retrieval
```

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues).

---

<div align="center">

**Built with 💙 by [libe.dev](https://libe.dev)**

[![Portfolio](https://img.shields.io/badge/Portfolio-libe.dev-blue?style=flat-square)](https://libe.dev)
[![GitHub](https://img.shields.io/badge/GitHub-@mrlibelula-181717?style=flat-square&logo=github)](https://github.com/mrlibelula)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/mrlibelula/)

---

<sub>⭐ Star this repository if you found it helpful!</sub>

</div>
