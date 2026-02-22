# Python Data Structures & Algorithms

Educational implementation of common data structures and algorithms in Python.

## Tech Stack

- Python
- pytest (for testing)

## Project Structure

- `data_structures/` – fundamental data structure implementations
- `algorithms/` – sorting and searching algorithm implementations
- `conftest.py` – pytest configuration

## Data Structures

- **Binary Search Tree** – ordered binary tree with search operations
- **Binary Tree** – basic tree structure with traversal methods
- **Doubly Linked List** – linked list with bidirectional traversal
- **Singly Linked List** – basic linked list implementation
- **Graph** – graph structure with adjacency list representation
- **Heap** – base heap implementation
- **Max Heap** – heap with maximum element at root
- **Min Heap** – heap with minimum element at root
- **Priority Queue** – queue ordered by priority
- **Queue** – FIFO data structure
- **Stack** – LIFO data structure
- **Trie** – prefix tree for string operations

## Algorithms

- **Binary Search** – logarithmic search in sorted arrays
- **Linear Search** – sequential search algorithm
- **Bubble Sort** – simple comparison-based sorting
- **Insertion Sort** – builds sorted array one element at a time
- **Selection Sort** – selects minimum and places in order
- **Merge Sort** – divide-and-conquer sorting algorithm
- **Quick Sort** – partition-based sorting algorithm
- **Dijkstra's Algorithm** – shortest path in weighted graphs

## Getting Started

1. Install Python 3.x.
2. Install dependencies:

```bash
pip install pytest
```

3. Run tests:

```bash
pytest
```

## Development

- Each data structure and algorithm has its own module with corresponding test file.
- Tests follow the naming convention `*_test.py`.
- Run specific tests: `pytest data_structures/stack_test.py` or `pytest algorithms/binary_search_test.py`.
