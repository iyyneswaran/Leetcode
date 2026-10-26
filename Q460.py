class Node:
    def __init__(self, key=None, value=None, counter=0):
        self.key = key
        self.value = value
        self.counter = counter
        self.prev = None
        self.next = None

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
    
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None

    def _insert_mfu(self, node):
        curr  = self.right.prev
        while curr != self.left and curr.counter > node.counter:
            curr = curr.prev
        
        next_node = curr.next
        curr.next = node
        node.prev = curr
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node.counter += 1
            self._remove(node)
            self._insert_mfu(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            node.counter += 1
            self._remove(node)
            self._insert_mfu(node)
            return
        
        if len(self.cache) >= self.capacity:
            lfu_node = self.left.next
            self._remove(lfu_node)
            del self.cache[lfu_node.key]
        
        new_node = Node(key, value, 1)
        self.cache[key] = new_node
        self._insert_mfu(new_node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)