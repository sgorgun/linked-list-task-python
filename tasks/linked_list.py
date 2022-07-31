"""Templates for programming assignments: operations with linked list."""


from typing import List, Optional

from tasks.linked_list_node import LinkedListNode


def create_linked_list(values: List[int]) -> Optional[LinkedListNode]:
    """Returns a head element of the linked list for given values.

    NOTE: returns None, if a given list is empty.

    Args:
        values: List, values that should be inserted into the result linked list.

    Returns:
        LinkedListNode, the head element.
    """
    pass


def remove_values(head: Optional[LinkedListNode], value_to_remove: int) -> Optional[LinkedListNode]:
    """Returns a head element of the new linked list after removal of all 'value_to_remove' nodes.

    NOTE: returns None, if after the removal there are no elements left.

    Args:
        head: LinkedListNode, the head element of a given linked list.
        value_to_remove: int, target value that should be eliminated from the list.

    Returns:
        LinkedListNode, the head element after the removal.
    """
    pass


def reverse_linked_list(head: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
    """Returns a head element of the new linked list after reversing a given linked list.

    NOTE: returns None, if a given linked list is empty.

    Args:
        head: LinkedListNode, the head element of a given linked list.

    Returns:
        LinkedListNode, the head element after the reversal.
    """
    pass


def get_middle_node(head: Optional[LinkedListNode]) -> Optional[LinkedListNode]:
    """Returns the middle element of a given linked list.

    NOTE: If there are two middle nodes, returns the second middle node.
    NOTE: returns None, if a given linked list is empty.

    Args:
        head: LinkedListNode, the head element of a given linked list.

    Returns:
        LinkedListNode, the middle element (node).
    """
    pass
