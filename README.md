## Linked-List

---

## Linked List Implementation Using Dictionaries in Python

This is a simple implementation of a singly linked list in Python using dictionaries to represent nodes. It demonstrates how to manually build and manipulate a linked list structure without using classes or built-in data structures.

---

## What This Code Does

1. Creates a simple linked list with two nodes (1 -> 2).

2. Prepends a new node (0) to the beginning of the list (0 -> 1 -> 2).

3. Prints the current linked list.

4. Appends a new node (3) to the end of the list (0 -> 1 -> 2 -> 3).

5. Prints the updated linked list.

---

## How It Works

Each node is represented as a Python dictionary : 

```bash

{"val": value, "next": reference_to_next_node}

```

Code Walkthrough:

```bash

# Create initial linked list: 1 -> 2
node2 = {"val": 2, "next": None}
node1 = {"val": 1, "next": node2}
head = node1

# Prepend new node: 0 -> 1 -> 2
new_head = {"val": 0, "next": head}
head = new_head

# Print the current list
current = head
while current is not None:
    print(current["val"], end=' ')
    current = current["next"]
print()

# Append new tail: 0 -> 1 -> 2 -> 3
new_tail = {"val": 3, "next": None}
current = head
while current["next"] is not None:
    current = current["next"]
current["next"] = new_tail

# Print the final list
current = head
while current is not None:
    print(current["val"], end=' ')
    current = current["next"]

```

Output :

```bash

0 1 2
0 1 2 3

```

---

## Why Use Dictionaries?

This example avoids object-oriented programming to provide a clear, minimal demonstration of how linked lists work at a low level. It’s useful for beginners to understand pointer-like structures without jumping into class definitions.

---

## Requirements

- Python 3.x

- No external libraries needed

---

## Files

- Linked List.py — Contains the full code.

- README.md — You're reading it.

---

## Try It Yourself

You can run the code in any Python environment :

```bash

python Linked List.py

```

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License.

---

