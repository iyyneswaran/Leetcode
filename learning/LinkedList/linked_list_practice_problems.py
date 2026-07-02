"""
LINKED LIST — PRACTICE PROBLEMS
============================================================
Four classic interview problems, each with:
  - Problem statement
  - The key insight
  - A working solution
  - A demo

Try solving each one yourself BEFORE reading the solution.
Cover the solution function with your hand/scroll past it,
write your own attempt, then compare.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_list(values):
    """Helper: turn a Python list into a linked list. Returns head node."""
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def print_list(head, max_nodes=20):
    """Helper: print a linked list. max_nodes guards against infinite loops."""
    current = head
    elements = []
    count = 0
    while current is not None and count < max_nodes:
        elements.append(str(current.data))
        current = current.next
        count += 1
    suffix = " -> ... (truncated, likely a cycle)" if current is not None else ""
    print(" -> ".join(elements) + suffix if elements else "Empty list")


# ==================================================================
# PROBLEM 1: Reverse a Linked List
# ==================================================================
"""
Statement: Given the head of a singly linked list, reverse it
in place and return the new head.

Key insight: You need 3 pointers moving together — prev, current,
and next_node — because once you flip current.next, you'd lose
access to the rest of the list unless you saved it first.

Time: O(n)   Space: O(1)
"""
def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next   # save before overwriting
        current.next = prev        # flip the arrow backward
        prev = current
        current = next_node
    return prev   # prev is the new head


# ==================================================================
# PROBLEM 2: Find the Middle Node
# ==================================================================
"""
Statement: Given the head of a singly linked list, return the
middle node. If there are two middle nodes (even length), return
the second one.

Key insight: slow/fast pointers. Move slow by 1, fast by 2.
When fast reaches the end, slow is at the middle — because
slow has covered exactly half the distance fast has.

Time: O(n)   Space: O(1)
(The brute-force alternative — count length, then walk length//2
steps — also works but takes two full passes instead of one.)
"""
def find_middle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next        # 1 step
        fast = fast.next.next   # 2 steps
    return slow


# ==================================================================
# PROBLEM 3: Detect a Cycle
# ==================================================================
"""
Statement: Given the head of a linked list, determine if it
contains a cycle (some node's 'next' eventually points back to
an earlier node instead of ending in None).

Key insight: same slow/fast pointers. If there's no cycle, fast
will hit None and we return False. If there IS a cycle, fast
will eventually "lap" slow inside the loop and they'll land on
the exact same node — that equality is your proof of a cycle.

Why they're guaranteed to meet: think of it like two runners on
a circular track — the faster one will always eventually catch
up to the slower one from behind.

Time: O(n)   Space: O(1)
(This is called Floyd's Cycle Detection Algorithm.)
"""
def has_cycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:   # they met -> cycle confirmed
            return True
    return False   # fast hit None -> no cycle


# ==================================================================
# PROBLEM 4: Merge Two Sorted Linked Lists
# ==================================================================
"""
Statement: Given the heads of two sorted linked lists, merge
them into one sorted linked list and return its head.

Key insight: this is just the "merge" step from merge sort,
adapted to linked lists. Use a dummy head node to avoid messy
edge-case handling for "what if the merged list is empty so far."
At each step, compare the two current nodes and attach the
smaller one to your result, then advance only that pointer.

Time: O(n + m)   Space: O(1) extra (we reuse existing nodes,
just relink them — no new nodes created)
"""
def merge_sorted_lists(head1, head2):
    dummy = Node(None)   # placeholder, makes logic below much cleaner
    tail = dummy

    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    # attach whichever list still has leftover nodes
    tail.next = head1 if head1 is not None else head2

    return dummy.next   # skip the dummy, return the real head


# ==================================================================
# DEMOS
# ==================================================================
if __name__ == "__main__":
    print("=== Problem 1: Reverse ===")
    head = build_list([1, 2, 3, 4, 5])
    print("Before:", end=" ")
    print_list(head)
    reversed_head = reverse_list(head)
    print("After: ", end=" ")
    print_list(reversed_head)

    print("\n=== Problem 2: Find Middle ===")
    head = build_list([1, 2, 3, 4, 5])
    print("List:", end=" ")
    print_list(head)
    print("Middle node:", find_middle(head).data)   # 3

    head = build_list([1, 2, 3, 4, 5, 6])
    print("List:", end=" ")
    print_list(head)
    print("Middle node (even length -> 2nd middle):", find_middle(head).data)  # 4

    print("\n=== Problem 3: Detect Cycle ===")
    head = build_list([1, 2, 3, 4, 5])
    print("No cycle:", has_cycle(head))   # False

    # manually create a cycle: last node points back to node with data=3
    head2 = build_list([1, 2, 3, 4, 5])
    current = head2
    node_3 = None
    while current is not None:
        if current.data == 3:
            node_3 = current
        if current.next is None:
            current.next = node_3   # create the loop
            break
        current = current.next
    print("With cycle:", has_cycle(head2))   # True

    print("\n=== Problem 4: Merge Two Sorted Lists ===")
    list1 = build_list([1, 3, 5, 7])
    list2 = build_list([2, 4, 6, 8, 10])
    print("List 1:", end=" ")
    print_list(list1)
    print("List 2:", end=" ")
    print_list(list2)
    merged = merge_sorted_lists(list1, list2)
    print("Merged: ", end=" ")
    print_list(merged)
