# Linked List (Python)

Set of programming assignments that are designed to test knowledge of linked list data structure.

### Basic data structure for representing linked list

You may assume that for all programming assignments within this problem set the following data class
will be used to represent elements of linked list:

```python
class LinkedListNode:
    """Dataclass that represents linked list elements."""

    def __init__(
        self,
        value: int = 0,
        next_element: Optional['LinkedListNode'] = None
    ):
        self.value = value
        self.next_element = next_element
```

The implementation above can be found within `tasks/linked_list_node.py` file.

For example the following linked list could be created using the snippet below:

```mermaid
graph LR;
    A[value=5] == next_element ===> B[value=107] == next_element ===> C[value=42]
```

```python
a = LinkedListNode(value=42)
b = LinkedListNode(value=107, next_element=a)
c = LinkedListNode(value=5, next_element=b)
```


## Problem 1: Create Linked List using a given array of values

Given an array of values, return a linked list with all the values (its head element).

**Example:**

Input: [23, 1, 49]

Expected result:
```mermaid
graph LR;
    A[value=23] == next_element ===> B[value=1] == next_element ===> C[value=49]
    style A fill:#f9f,stroke:#333,stroke-width:4px
```

Please use a template for the implementation (`tasks/linked_list:create_linked_list`).


## Problem 2: Remove Linked List elements by value

Given the `head` of a linked list and an integer `value`, remove all the nodes of the linked list that has `LinkedListNode.value == value`, and return *the new head*.


**Example 1:**

```mermaid
graph LR;
    subgraph Result Linked List
    BB[value=107] --> CC[value=42] --> EE[value=23]
    end

    subgraph Input Linked List
    A[value=5] --> B[value=107] --> C[value=42] --> D[value=5] --> E[value=23] --> F[value=5]
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style D fill:#f9f,stroke:#333,stroke-width:4px
    style F fill:#f9f,stroke:#333,stroke-width:4px
    end
```

**Example 2:**

Input: [42, 42, 42]

Expected result: []


**Example 3:**

Input: []

Expected result: []

Please use a template for the implementation (`tasks/linked_list:remove_values`).


## Problem 3: Reverse a given Linked List

Given the `head` of a linked list, reverse the list, and return the reversed list's head.


**Example 1:**

```mermaid
graph LR;
    subgraph Result Linked List
    BB[value=107] --> CC[value=42] --> EE[value=23]
    end

    subgraph Input Linked List
    B[value=23] --> C[value=42] --> E[value=107]
    end
```

**Example 2:**

```mermaid
graph LR;
    subgraph Result Linked List
    BB[value=107] --> CC[value=42] --> EE[value=23] --> AA[value=21] --> DD[value=2] --> FF[value=0]
    end

    subgraph Input Linked List
    F[value=0] --> A[value=2] --> D[value=21] --> B[value=23] --> C[value=42] --> E[value=107]
    end
```

**Example 3:**

Input: []

Expected result: []


Please use a template for the implementation (`tasks/linked_list:reverse_linked_list`).


## Problem 4: Find the middle node of a given linked list

Given the `head` of a linked list, return *the middle node of the linked list*.

If there are two middle nodes, return **the second middle** node.

**Example 1:**

```mermaid
graph LR;
    subgraph Input Linked List
    BB[value=107] --> CC[value=42] --> EE[value=23] --> AA[value=21] --> DD[value=2] --> FF[value=0]
    end

    style AA fill:#f9f,stroke:#333,stroke-width:4px
```

**Example 2:**

```mermaid
graph LR;
    subgraph Input Linked List
    BB[value=107] --> CC[value=42] --> EE[value=23] --> AA[value=21] --> DD[value=2]
    end

    style EE fill:#f9f,stroke:#333,stroke-width:4px
```

**Example 3:**

Input: []

Expected result: []


Please use a template for the implementation (`tasks/linked_list:get_middle_node`).
