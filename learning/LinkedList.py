"""
SINGLY LINKED LIST — from scratch, for DSA interview prep
============================================================
Read this top to bottom. Each method has a docstring explaining
WHAT it does, HOW it does it, and its TIME COMPLEXITY.
Run this file directly to see everything in action.
"""


class Node:
    """
    A single 'link' in the chain.
    Holds one piece of data, and a pointer to the next Node (or None).
    """
    def __init__(self, data):
        self.data = data
        self.next = None   # every new node starts pointing to nothing


class LinkedList:
    def __init__(self):
        self.head = None   # empty list = no head yet

    # ------------------------------------------------------------
    # 1. TRAVERSE / PRINT — the operation you'll reuse constantly
    # ------------------------------------------------------------
    def display(self):
        """
        Walk from head to end, printing each node's data.
        Time: O(n) — must visit every node once.
        """
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")

    # ------------------------------------------------------------
    # 2. INSERT AT THE END (append)
    # ------------------------------------------------------------
    def append(self, data):
        """
        Add a new node at the end of the list.
        Time: O(n) — we have to walk to the last node first
        (unless you maintain a separate 'tail' pointer, which
        many production implementations do to make this O(1)).
        """
        new_node = Node(data)

        if self.head is None:          # list was empty
            self.head = new_node
            return

        current = self.head
        while current.next is not None:   # walk till the last node
            current = current.next
        current.next = new_node        # last node now points to new node

    # ------------------------------------------------------------
    # 3. INSERT AT THE START (prepend)
    # ------------------------------------------------------------
    def prepend(self, data):
        """
        Add a new node at the beginning.
        Time: O(1) — no walking needed, this is the linked list's
        superpower compared to arrays (which need O(n) shifting).
        """
        new_node = Node(data)
        new_node.next = self.head   # new node points to old head
        self.head = new_node        # new node becomes the head

    # ------------------------------------------------------------
    # 4. INSERT AT A GIVEN POSITION (0-indexed)
    # ------------------------------------------------------------
    def insert_at(self, index, data):
        """
        Insert new data at a specific index.
        Time: O(n) — must walk to the node just before that index.
        """
        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        if current is None:
            raise IndexError("Index out of range")

        new_node.next = current.next
        current.next = new_node

    # ------------------------------------------------------------
    # 5. DELETE BY VALUE
    # ------------------------------------------------------------
    def delete_value(self, value):
        """
        Remove the first node containing this value.
        Time: O(n) — search + relink.
        Key trick: keep a 'previous' pointer so you can
        reroute prev.next around the node you're removing.
        """
        current = self.head
        previous = None

        while current is not None:
            if current.data == value:
                if previous is None:        # deleting the head
                    self.head = current.next
                else:
                    previous.next = current.next   # skip over 'current'
                return True   # deleted successfully
            previous = current
            current = current.next

        return False   # value not found

    # ------------------------------------------------------------
    # 6. SEARCH
    # ------------------------------------------------------------
    def search(self, value):
        """
        Check whether a value exists in the list.
        Time: O(n) — no shortcuts, must check node by node
        (this is the big weakness vs arrays with indexing).
        """
        current = self.head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    # ------------------------------------------------------------
    # 7. LENGTH
    # ------------------------------------------------------------
    def length(self):
        """Time: O(n)."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    # ------------------------------------------------------------
    # 8. REVERSE — the single most-asked linked list interview question
    # ------------------------------------------------------------
    def reverse(self):
        """
        Reverse the list in place.
        Time: O(n), Space: O(1) — no extra data structure used.

        The trick: walk forward, but at each node flip its
        'next' pointer to point BACKWARD instead of forward.
        You need 3 pointers to do this without losing the chain:
            prev, current, next_node
        """
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next   # save the next node before we overwrite it
            current.next = prev        # flip the pointer backward
            prev = current              # move prev forward
            current = next_node         # move current forward

        self.head = prev   # prev is the new head after reversal


# ==================================================================
# DEMO — run this file to see it all work
# ==================================================================
if __name__ == "__main__":
    ll = LinkedList()

    print("Appending 10, 20, 30:")
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.display()   # 10 -> 20 -> 30

    print("\nPrepending 5:")
    ll.prepend(5)
    ll.display()   # 5 -> 10 -> 20 -> 30

    print("\nInserting 15 at index 2:")
    ll.insert_at(2, 15)
    ll.display()   # 5 -> 10 -> 15 -> 20 -> 30

    print("\nDeleting value 15:")
    ll.delete_value(15)
    ll.display()   # 5 -> 10 -> 20 -> 30

    print("\nSearching for 20:", ll.search(20))   # True
    print("Searching for 99:", ll.search(99))     # False

    print("\nLength:", ll.length())   # 4

    print("\nReversing the list:")
    ll.reverse()
    ll.display()   # 30 -> 20 -> 10 -> 5