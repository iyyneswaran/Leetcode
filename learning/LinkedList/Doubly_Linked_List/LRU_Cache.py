class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")

        self.capacity = capacity
        self.cache = {}

        # Sentinels: left is the LRU boundary,
        # right is the MRU boundary.
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = None
        node.next = None

    def _insert_mru(self, node):
        prev_node = self.right.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.right
        self.right.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # This access makes the node most recently used.
        self._remove(node)
        self._insert_mru(node)

        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        # Update an existing key.
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self._remove(node)
            self._insert_mru(node)
            return

        # Add a new key.
        node = Node(key, value)
        self.cache[key] = node
        self._insert_mru(node)

        # Evict the least recently used item.
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self._remove(lru_node)
            del self.cache[lru_node.key]